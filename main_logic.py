# 导入PyQt6相关模块和你的Ui_MainWindow类
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6.QtCore import QTimer
from test import Ui_MainWindow  # 确保导入了正确的Ui_MainWindow类
import os
import json
from colorama import Fore, Style
import time
from tqdm import tqdm



def get_problems():
    """获取benchmark中所有的题目
    """
    all_data = {}
    benchmark_path = "/Users/yeyn/data/git_repos/DebugBench-Prototype/benchmark_data"
    for file_name in tqdm(os.listdir(benchmark_path), desc="loading data..."):
        if file_name.endswith(".json"):
            programming_language = file_name.split("_")[0]
            buggy_type = file_name.split("_")[1].split(".")[0]
            with open(os.path.join(benchmark_path,file_name)) as reader:
                file_problems = json.load(reader)
            for problem in file_problems:

                problem_name = problem["slug"]
                problem_name = problem_name.replace("-"," ")
                if problem_name not in all_data.keys():
                    all_data[problem_name] = {"code": [],
                                              }
                for key in ["description", "release_time", "level", "constraints"]:
                    if key in problem.keys() and key not in all_data[problem_name].keys():
                        all_data[problem_name][key] = problem[key]
                item = {
                    "oracle_code": problem["oracle_code"],
                    "buggy_code": problem["buggy_code"],
                    "examples": problem["examples"],
                    "buggy_type": buggy_type,
                    "language": programming_language,
                }
                if "explanations" in problem.keys():
                    item["explanations"] = problem["explanations"]
                all_data[problem_name]["code"].append(item)
    return all_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 初始化界面
        self.setupUi(self)
        # 在这里添加业务逻辑，例如按钮的点击事件
        self.stackedWidget.setCurrentIndex(0)

        self.orcale_code.setMinimumWidth(self.orcale_code_scrollArea.viewport().width())
        self.orcale_code.setMinimumHeight(self.orcale_code_scrollArea.viewport().height())

        self.back_to_problem_set.clicked.connect(self.go_to_problem_set)
        self.back_to_problem_detail.clicked.connect(self.go_to_problem_detail)
        self.go_to_debug.clicked.connect(self.render_debug)
        self.reset.clicked.connect(self.reset_debug)
        self.submit.clicked.connect(self.submit_debug)
        self.leaderBoard.clicked.connect(self.show_leaderboard)

        self.problem_table.cellClicked.connect(self.click_a_problem)

        self.all_problems = get_problems()
    
        self.load_problem_set()

        self.debugging_start_time = time.time()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)  # 设置定时器每1000毫秒（1秒）触发一次

    def updateTimer(self):
        now_time = time.time()
        if self.debugging_start_time != None:
            self.debug_time.setText(f"Debug...{int(now_time-self.debugging_start_time)}s")

    def click_a_problem(self, row, column):
        """点进了题目详情页
        """ 
        print(f"click {row} {column}")
        assert row < len(self.row_reflection)

        self.last_choosed_problem = self.row_reflection[row]
        self.stackedWidget.setCurrentIndex(2)

        self.render_problem(self.last_choosed_problem)
    
    def render_problem(self, choosed_problem):

        self.problem_head.setText(choosed_problem['name'])
        self.hardness.setText(choosed_problem['problem']['level'])
        self.language.setText(choosed_problem['code']['language'])
        description = choosed_problem["problem"]["description"]
        if "examples" in choosed_problem["code"].keys():
            if isinstance(choosed_problem["code"]["examples"], str):
                description += "\n" + choosed_problem["code"]["examples"]
            elif isinstance(choosed_problem["code"]["examples"], list):
                description += "\n" + "\n".join(choosed_problem["code"]["examples"])
        if "constraints" in choosed_problem["problem"].keys():
            description += "\n" + choosed_problem["problem"]["constraints"]
        self.problem_description.setText(description)


        self.orcale_code.setText(choosed_problem["code"]["oracle_code"])
        self.buggy_code.setText(choosed_problem["code"]["buggy_code"])
        if "explanations" in choosed_problem["code"].keys():
            self.buggy_reason.setText("Buggy Code: "+choosed_problem["code"]["explanations"])
        else:
            self.buggy_reason.setText("Buggy Code")

    def render_debug(self):
        assert self.last_choosed_problem != None
        self.debugging_start_time = time.time()
        self.stackedWidget.setCurrentIndex(1)

        # TODO: 在QT里显示代码高亮？
        self.buggy_code_instance.setText(self.last_choosed_problem["code"]["buggy_code"])

        self.now_code.setPlainText(self.last_choosed_problem["code"]["buggy_code"])
    def reset_debug(self):
        self.now_code.setPlainText(self.last_choosed_problem["code"]["buggy_code"])


    def submit_debug(self):
        print("提交代码")
        self.stackedWidget.setCurrentIndex(3)
        end_time = time.time()
        self.submit_info.setText(f"Time Cost: {int(end_time-self.debugging_start_time)}s")

        # TODO: check the submitted code
        now_code = self.now_code.toPlainText()
        print(now_code)

        self.submit_result.setText("Waiting for the online judger...")

    def load_problem_set(self):
        self.problem_table.clearContents()
        problem_count = 0
        for k, (problem_name, item) in enumerate(self.all_problems.items()):
            problem_count += len(item["code"])
        self.problem_table.setRowCount(problem_count)

        self.row_reflection = []

        now_item_position = 0
        for k, (problem_name, item) in enumerate(self.all_problems.items()):
            hardness = item["level"] if "level" in item.keys() else "Unknown"
            if "release_time" in item.keys():

                release_date = item["release_time"]
                time_struct = time.gmtime(release_date)
                release_date = time.strftime('%Y-%m-%d', time_struct)
            else:
                release_date = "Unknown"
            for cont in item["code"]:
                
                self.problem_table.setItem(now_item_position, 0, QTableWidgetItem(problem_name))
                self.problem_table.setItem(now_item_position, 1, QTableWidgetItem(hardness))
                self.problem_table.setItem(now_item_position, 2, QTableWidgetItem(cont["buggy_type"]))
                self.problem_table.setItem(now_item_position, 3, QTableWidgetItem(release_date))
                self.problem_table.setItem(now_item_position, 4, QTableWidgetItem(cont["language"]))
                self.row_reflection.append({
                    "name": problem_name,
                    "problem": item,
                    "code": cont,
                })
                now_item_position += 1

    def go_to_problem_set(self):
        # 这里是按钮点击事件的处理逻辑
        print("回到题目列表页")
        self.stackedWidget.setCurrentIndex(0)

    
    def go_to_problem_detail(self):
        print("回到题目详情页")
        self.stackedWidget.setCurrentIndex(2)
        self.render_problem(self.last_choosed_problem)

    def show_leaderboard(self):
        print("显示所有模型Performance")
        self.stackedWidget.setCurrentIndex(4)
        #TODO 在这里显示一个echart？

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())