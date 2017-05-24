# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.nav = QtWidgets.QStackedWidget(self.centralwidget)
        self.nav.setObjectName("nav")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.textEdit = QtWidgets.QTextEdit(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.start_btn = QtWidgets.QPushButton(self.page)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.nav.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem5)
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.no_btn_1 = QtWidgets.QPushButton(self.page_2)
        self.no_btn_1.setObjectName("no_btn_1")
        self.horizontalLayout_3.addWidget(self.no_btn_1)
        self.yes_btn_1 = QtWidgets.QPushButton(self.page_2)
        self.yes_btn_1.setObjectName("yes_btn_1")
        self.horizontalLayout_3.addWidget(self.yes_btn_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.nav.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem6)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_3.addWidget(self.textEdit_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.no_btn_2 = QtWidgets.QPushButton(self.page_3)
        self.no_btn_2.setObjectName("no_btn_2")
        self.horizontalLayout_4.addWidget(self.no_btn_2)
        self.test_btn_2 = QtWidgets.QPushButton(self.page_3)
        self.test_btn_2.setObjectName("test_btn_2")
        self.horizontalLayout_4.addWidget(self.test_btn_2)
        self.yes_btn_2 = QtWidgets.QPushButton(self.page_3)
        self.yes_btn_2.setObjectName("yes_btn_2")
        self.horizontalLayout_4.addWidget(self.yes_btn_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.nav.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_4.addWidget(self.textEdit_4, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem7)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.no_btn_3 = QtWidgets.QPushButton(self.page_4)
        self.no_btn_3.setObjectName("no_btn_3")
        self.horizontalLayout_5.addWidget(self.no_btn_3)
        self.test_btn_3 = QtWidgets.QPushButton(self.page_4)
        self.test_btn_3.setObjectName("test_btn_3")
        self.horizontalLayout_5.addWidget(self.test_btn_3)
        self.yes_btn_3 = QtWidgets.QPushButton(self.page_4)
        self.yes_btn_3.setObjectName("yes_btn_3")
        self.horizontalLayout_5.addWidget(self.yes_btn_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.nav.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.no_btn_b = QtWidgets.QPushButton(self.page_5)
        self.no_btn_b.setObjectName("no_btn_b")
        self.horizontalLayout_6.addWidget(self.no_btn_b)
        self.test_btn_b = QtWidgets.QPushButton(self.page_5)
        self.test_btn_b.setObjectName("test_btn_b")
        self.horizontalLayout_6.addWidget(self.test_btn_b)
        self.yes_btn_b = QtWidgets.QPushButton(self.page_5)
        self.yes_btn_b.setObjectName("yes_btn_b")
        self.horizontalLayout_6.addWidget(self.yes_btn_b)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_6.addItem(spacerItem8)
        self.gridLayout_5.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.page_5)
        self.textEdit_5.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_5.addWidget(self.textEdit_5, 1, 0, 1, 1)
        self.nav.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem9)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.page_6)
        self.textEdit_6.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_6.addWidget(self.textEdit_6, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.no_btn_4 = QtWidgets.QPushButton(self.page_6)
        self.no_btn_4.setObjectName("no_btn_4")
        self.horizontalLayout_7.addWidget(self.no_btn_4)
        self.test_btn_4 = QtWidgets.QPushButton(self.page_6)
        self.test_btn_4.setObjectName("test_btn_4")
        self.horizontalLayout_7.addWidget(self.test_btn_4)
        self.yes_btn_4 = QtWidgets.QPushButton(self.page_6)
        self.yes_btn_4.setObjectName("yes_btn_4")
        self.horizontalLayout_7.addWidget(self.yes_btn_4)
        self.gridLayout_6.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.nav.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit_7 = QtWidgets.QTextEdit(self.page_7)
        self.textEdit_7.setStyleSheet("background:rgb(189, 204, 255)")
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_7.addWidget(self.textEdit_7, 1, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_8.addItem(spacerItem10)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.restart_btn = QtWidgets.QPushButton(self.page_7)
        self.restart_btn.setObjectName("restart_btn")
        self.horizontalLayout_8.addWidget(self.restart_btn)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.exit_btn = QtWidgets.QPushButton(self.page_7)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_8.addWidget(self.exit_btn)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.nav.addWidget(self.page_7)
        self.gridLayout.addWidget(self.nav, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.nav.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to the dbToolkit Normalization tool!"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The goal of decomposing a relation into normal forms is to achieve the following properties:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-style:italic;\">1. Lossless joins</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-style:italic;\">2. No anomalies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-style:italic;\">3. Dependency preservation</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Through a series of questions you will be guided towards achieving those properties.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">At each stage, clicking the \'does not satisfy\' button will give you suggestions and/or tools for satisfying the respective normal form.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clicking the \'satisfies\' button will proceed to the next strictest normal form.</p></body></html>"))
        self.start_btn.setText(_translate("MainWindow", "Begin"))
        self.label_2.setText(_translate("MainWindow", "1st Normal Form (1NF) Criteria"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Properties of 1<span style=\" vertical-align:super;\">st</span> Normal Form:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">No multi-valued attributes</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Example 1: email : &quot;user1@domain1.com, user2@domain2.com&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Example 2: phoneNo : &quot;(XXX)-XXX-XXXX, (XXX)-XXX-XXXX&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Alternatives:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Decompose email/phoneNo into a separate table</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\">Ideally, the intersection of the attributes between the two new tables should functionally determine the entirety of one of the tables</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Why are multi-valued attributes disadvantageous?</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Repeating groups of data are often stored like this (redundancy)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Individual values \'within\' the attribute cannot be easily modified</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Deletion of the key can cause loss of information</p></body></html>"))
        self.no_btn_1.setText(_translate("MainWindow", "My schema does not satisfy 1NF"))
        self.yes_btn_1.setText(_translate("MainWindow", "Yes, my schema satisfies 1NF"))
        self.label_3.setText(_translate("MainWindow", "2nd Normal Form (2NF) Criteria"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Properties of 2<span style=\" vertical-align:super;\">nd</span> Normal Form:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Meets all conditions of 1NF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">All non-prime attributes depend on candidate keys</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-style:italic;\">More specifically:</span><span style=\" font-weight:600;\"> </span><span style=\" text-decoration: underline;\">All non-key attributes depend on </span><span style=\" font-weight:600; text-decoration: underline;\">entire</span><span style=\" text-decoration: underline;\"> candidate keys</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Formal Definition:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">∀A ∃X → A where A is a non-prime attribute and X is a candidate key</p></body></html>"))
        self.no_btn_2.setText(_translate("MainWindow", "My schema does not satisfy 2NF"))
        self.test_btn_2.setText(_translate("MainWindow", "Test my schema"))
        self.yes_btn_2.setText(_translate("MainWindow", "Yes, my schema satisfies 2NF"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Properties of 3<span style=\" vertical-align:super;\">rd</span> Normal Form:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Meets conditions of 2NF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Non-prime attributes depend <span style=\" font-weight:600;\">only</span> on entire candidate keys and <span style=\" font-weight:600;\">no</span> non-prime attributes</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Disambiguation:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Non-prime attributes cannot be transitively dependent upon a candidate key (via a non-prime attribute)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Non-prime attributes cannot simultaneously depend upon a candidate key and a non-prime attribute</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">What are the advantages of 3NF?</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Reduced data duplication and assurance of referential integrity</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:8pt;\">* It is always possible to convert a schema to a lossless join, dependency preserving 3NF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:8pt;\">**</span><span style=\" font-size:8pt; font-style:italic;\">It is always possible to create 3NF schemas for which these do not hold - hence the importance of good design</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "3rd Normal Form (3NF) Criteria"))
        self.no_btn_3.setText(_translate("MainWindow", "My schema does not satisfy 3NF"))
        self.test_btn_3.setText(_translate("MainWindow", "Test my schema"))
        self.yes_btn_3.setText(_translate("MainWindow", "Yes, my schema satisfies 3NF"))
        self.no_btn_b.setText(_translate("MainWindow", "My schema does not satisfy BCNF"))
        self.test_btn_b.setText(_translate("MainWindow", "Test my schema"))
        self.yes_btn_b.setText(_translate("MainWindow", "Yes, my schema satisfies BCNF"))
        self.label_5.setText(_translate("MainWindow", "Boyce-Codd Normal Form (BCNF) Criteria"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Properties of Boyce-Codd Normal Form:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Meets conditions of 3NF</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">∀X → Y (that is non-trivial), X is a superkey for relational schema R</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Advantages of BCNF:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Guarantees lossless joins and no anomalies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Removes redundancies related to functional dependencies</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">* does not guarantee dependency preservation</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "4th Normal Form (4NF) Criteria"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Properties of 4</span><span style=\" font-size:9pt; vertical-align:super;\">th</span><span style=\" font-size:9pt;\"> Normal Form:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Meets the conditions of BCNF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">∀X</span><span style=\" font-size:12pt;\"> </span><span style=\" font-size:11pt;\">↠ </span><span style=\" font-size:9pt;\">Y (where </span><span style=\" font-size:12pt;\">↠</span><span style=\" font-size:9pt;\"> signifies a multi-valued dependency), X is a superkey</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">*A multivalued dependency is one where X → Y and for any instance of (x</span><span style=\" font-size:8pt; vertical-align:sub;\">i</span><span style=\" font-size:8pt;\">, y, z), x</span><span style=\" font-size:8pt; vertical-align:sub;\">i</span><span style=\" font-size:8pt;\"> → y regardless of z</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Advantages of 4NF:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Eliminates more redundancy in the data</span></p></body></html>"))
        self.no_btn_4.setText(_translate("MainWindow", "My schema does not satisfy 4NF"))
        self.test_btn_4.setText(_translate("MainWindow", "Test my schema"))
        self.yes_btn_4.setText(_translate("MainWindow", "Yes, my schema satisfies 4NF"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Properties of 5</span><span style=\" font-size:9pt; vertical-align:super;\">th</span><span style=\" font-size:9pt;\"> Normal Form:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Cannot have a lossless decomposition into any number of smaller tables</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Every non-trivial join dependency is implied by the candidate keys</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">* See this </span><a href=\"http://www.bkent.net/Doc/simple5.htm#label4.2\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">technical report</span></a><span style=\" font-size:9pt;\"> by W. Kent for an in-depth explanation of 5NF</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Advantages of 5NF:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Fewer record occurrences (despite more record types)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt;\">Size of normalized files increases additively rather than multiplicatively</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">* Note: The major tradeoff of 5NF is number of joins required to reconstruct a full piece of information</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "5th Normal Form (5NF) / Project-join Normal Form (PJ/NF) Criteria"))
        self.restart_btn.setText(_translate("MainWindow", "Start from beginning"))
        self.exit_btn.setText(_translate("MainWindow", "Exit application"))

