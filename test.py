# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 748)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 20, 801, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(20, -10, 211, 51))
        self.label.setObjectName("label")
        self.problem_table = QtWidgets.QTableWidget(parent=self.page)
        self.problem_table.setGeometry(QtCore.QRect(10, 100, 761, 481))
        self.problem_table.setObjectName("problem_table")
        self.problem_table.setColumnCount(5)
        self.problem_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.problem_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.problem_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.problem_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.problem_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.problem_table.setHorizontalHeaderItem(4, item)
        self.frame_2 = QtWidgets.QFrame(parent=self.page)
        self.frame_2.setGeometry(QtCore.QRect(20, 50, 751, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.rank_method = QtWidgets.QComboBox(parent=self.frame_2)
        self.rank_method.setGeometry(QtCore.QRect(0, 0, 181, 41))
        self.rank_method.setObjectName("rank_method")
        self.rank_method.addItem("")
        self.rank_method.addItem("")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.debug_time = QtWidgets.QLabel(parent=self.page_3)
        self.debug_time.setGeometry(QtCore.QRect(20, -20, 151, 61))
        self.debug_time.setObjectName("debug_time")
        self.frame_3 = QtWidgets.QFrame(parent=self.page_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 30, 781, 511))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_3)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 371, 483))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buggy_code_instance = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.buggy_code_instance.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.buggy_code_instance.setWordWrap(True)
        self.buggy_code_instance.setObjectName("buggy_code_instance")
        self.horizontalLayout_5.addWidget(self.buggy_code_instance)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.frame_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 370, 483))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.now_code = QtWidgets.QTextEdit(parent=self.scrollAreaWidgetContents_4)
        self.now_code.setObjectName("now_code")
        self.horizontalLayout_4.addWidget(self.now_code)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_3.addWidget(self.scrollArea_2)
        self.submit = QtWidgets.QPushButton(parent=self.page_3)
        self.submit.setGeometry(QtCore.QRect(650, 570, 121, 41))
        self.submit.setObjectName("submit")
        self.reset = QtWidgets.QPushButton(parent=self.page_3)
        self.reset.setGeometry(QtCore.QRect(430, 570, 121, 41))
        self.reset.setObjectName("reset")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.problem_head = QtWidgets.QLabel(parent=self.page_2)
        self.problem_head.setGeometry(QtCore.QRect(10, 20, 161, 51))
        self.problem_head.setObjectName("problem_head")
        self.hardness = QtWidgets.QLabel(parent=self.page_2)
        self.hardness.setGeometry(QtCore.QRect(430, 20, 161, 51))
        self.hardness.setObjectName("hardness")
        self.language = QtWidgets.QLabel(parent=self.page_2)
        self.language.setGeometry(QtCore.QRect(620, 20, 161, 51))
        self.language.setObjectName("language")
        self.buggy_reason = QtWidgets.QLabel(parent=self.page_2)
        self.buggy_reason.setGeometry(QtCore.QRect(390, 260, 381, 51))
        self.buggy_reason.setObjectName("buggy_reason")
        self.problem_description_area = QtWidgets.QScrollArea(parent=self.page_2)
        self.problem_description_area.setGeometry(QtCore.QRect(0, 70, 771, 191))
        self.problem_description_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.problem_description_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.problem_description_area.setWidgetResizable(True)
        self.problem_description_area.setObjectName("problem_description_area")
        self.ScrollWidgets = QtWidgets.QWidget()
        self.ScrollWidgets.setGeometry(QtCore.QRect(0, 0, 769, 189))
        self.ScrollWidgets.setObjectName("ScrollWidgets")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ScrollWidgets)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.problem_description = QtWidgets.QLabel(parent=self.ScrollWidgets)
        self.problem_description.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.problem_description.setWordWrap(True)
        self.problem_description.setObjectName("problem_description")
        self.horizontalLayout_2.addWidget(self.problem_description)
        self.problem_description_area.setWidget(self.ScrollWidgets)
        self.orcale_code_scrollArea = QtWidgets.QScrollArea(parent=self.page_2)
        self.orcale_code_scrollArea.setGeometry(QtCore.QRect(0, 310, 381, 321))
        self.orcale_code_scrollArea.setAutoFillBackground(False)
        self.orcale_code_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.orcale_code_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.orcale_code_scrollArea.setWidgetResizable(True)
        self.orcale_code_scrollArea.setObjectName("orcale_code_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.orcale_code = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.orcale_code.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.orcale_code.setWordWrap(True)
        self.orcale_code.setObjectName("orcale_code")
        self.verticalLayout.addWidget(self.orcale_code)
        self.orcale_code_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.buggy_code_scroll_area = QtWidgets.QScrollArea(parent=self.page_2)
        self.buggy_code_scroll_area.setGeometry(QtCore.QRect(400, 310, 371, 321))
        self.buggy_code_scroll_area.setWidgetResizable(True)
        self.buggy_code_scroll_area.setObjectName("buggy_code_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 369, 319))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buggy_code = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.buggy_code.setScaledContents(False)
        self.buggy_code.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.buggy_code.setWordWrap(True)
        self.buggy_code.setObjectName("buggy_code")
        self.horizontalLayout.addWidget(self.buggy_code)
        self.buggy_code_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 131, 31))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.submit_info = QtWidgets.QLabel(parent=self.page_4)
        self.submit_info.setGeometry(QtCore.QRect(30, 30, 291, 141))
        self.submit_info.setObjectName("submit_info")
        self.submit_result = QtWidgets.QLabel(parent=self.page_4)
        self.submit_result.setGeometry(QtCore.QRect(20, 210, 291, 141))
        self.submit_result.setObjectName("submit_result")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_3 = QtWidgets.QLabel(parent=self.page_5)
        self.label_3.setGeometry(QtCore.QRect(60, 0, 161, 81))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_5)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 141, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.back_to_problem_set = QtWidgets.QPushButton(parent=self.frame)
        self.back_to_problem_set.setGeometry(QtCore.QRect(10, 60, 121, 41))
        self.back_to_problem_set.setObjectName("back_to_problem_set")
        self.back_to_problem_detail = QtWidgets.QPushButton(parent=self.frame)
        self.back_to_problem_detail.setGeometry(QtCore.QRect(10, 110, 121, 41))
        self.back_to_problem_detail.setObjectName("back_to_problem_detail")
        self.go_to_debug = QtWidgets.QPushButton(parent=self.frame)
        self.go_to_debug.setGeometry(QtCore.QRect(10, 160, 121, 41))
        self.go_to_debug.setObjectName("go_to_debug")
        self.leaderBoard = QtWidgets.QPushButton(parent=self.frame)
        self.leaderBoard.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.leaderBoard.setObjectName("leaderBoard")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Problem Sets in DebugBench"))
        item = self.problem_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "problem_name"))
        item = self.problem_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "hardness"))
        item = self.problem_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "bug_type"))
        item = self.problem_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "release_date"))
        item = self.problem_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "language"))
        self.rank_method.setItemText(0, _translate("MainWindow", "Rank by Problem name"))
        self.rank_method.setItemText(1, _translate("MainWindow", "Rank by Hardness"))
        self.debug_time.setText(_translate("MainWindow", "Debugging..."))
        self.buggy_code_instance.setText(_translate("MainWindow", "TextLabel"))
        self.submit.setText(_translate("MainWindow", "Submit!"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.problem_head.setText(_translate("MainWindow", "题目名称"))
        self.hardness.setText(_translate("MainWindow", "难度"))
        self.language.setText(_translate("MainWindow", "语言"))
        self.buggy_reason.setText(_translate("MainWindow", "buggy_reason"))
        self.problem_description.setText(_translate("MainWindow", "TextLabel"))
        self.orcale_code.setText(_translate("MainWindow", "orcale code"))
        self.buggy_code.setText(_translate("MainWindow", "orcale code"))
        self.label_2.setText(_translate("MainWindow", "Oracle Code"))
        self.submit_info.setText(_translate("MainWindow", "submit Info"))
        self.submit_result.setText(_translate("MainWindow", "submit Result"))
        self.label_3.setText(_translate("MainWindow", "leaderBoard"))
        self.back_to_problem_set.setText(_translate("MainWindow", "Problem List"))
        self.back_to_problem_detail.setText(_translate("MainWindow", "Problem Details"))
        self.go_to_debug.setText(_translate("MainWindow", "Debug!"))
        self.leaderBoard.setText(_translate("MainWindow", "LeaderBoard"))