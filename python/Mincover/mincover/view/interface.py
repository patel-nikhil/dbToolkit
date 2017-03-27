# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 620)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.schemaLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.schemaLabel.setFont(font)
        self.schemaLabel.setStyleSheet("")
        self.schemaLabel.setObjectName("schemaLabel")
        self.gridLayout_2.addWidget(self.schemaLabel, 0, 0, 1, 1)
        self.schemaLine = QtWidgets.QLineEdit(self.centralwidget)
        self.schemaLine.setAcceptDrops(False)
        self.schemaLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.schemaLine.setReadOnly(True)
        self.schemaLine.setObjectName("schemaLine")
        self.gridLayout_2.addWidget(self.schemaLine, 1, 0, 1, 1)
        self.fdText = QtWidgets.QListView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fdText.setFont(font)
        self.fdText.setStyleSheet("")
        self.fdText.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fdText.setObjectName("fdText")
        self.gridLayout_2.addWidget(self.fdText, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mincoverLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mincoverLabel.setFont(font)
        self.mincoverLabel.setStyleSheet("")
        self.mincoverLabel.setObjectName("mincoverLabel")
        self.horizontalLayout_2.addWidget(self.mincoverLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.genBtn = QtWidgets.QPushButton(self.centralwidget)
        self.genBtn.setStyleSheet("")
        self.genBtn.setObjectName("genBtn")
        self.horizontalLayout_2.addWidget(self.genBtn)
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_2.addWidget(self.saveBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mincoverText = QtWidgets.QListView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mincoverText.setFont(font)
        self.mincoverText.setStyleSheet("")
        self.mincoverText.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mincoverText.setObjectName("mincoverText")
        self.verticalLayout.addWidget(self.mincoverText)
        self.gridLayout_2.addLayout(self.verticalLayout, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fdLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.fdLabel.setFont(font)
        self.fdLabel.setStyleSheet("")
        self.fdLabel.setObjectName("fdLabel")
        self.horizontalLayout_6.addWidget(self.fdLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.splitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.splitBtn.setObjectName("splitBtn")
        self.horizontalLayout_6.addWidget(self.splitBtn)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout_6.addWidget(self.clearBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.addSchemaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addSchemaBtn.setStyleSheet("")
        self.addSchemaBtn.setObjectName("addSchemaBtn")
        self.gridLayout.addWidget(self.addSchemaBtn, 0, 0, 1, 1)
        self.addFDBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addFDBtn.setStyleSheet("")
        self.addFDBtn.setObjectName("addFDBtn")
        self.gridLayout.addWidget(self.addFDBtn, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.schemaLabel.setText(_translate("MainWindow", "Schema"))
        self.mincoverLabel.setText(_translate("MainWindow", "Minimal Cover"))
        self.genBtn.setToolTip(_translate("MainWindow", "Generate a minimal cover from the FDs"))
        self.genBtn.setText(_translate("MainWindow", "Generate Cover"))
        self.saveBtn.setToolTip(_translate("MainWindow", "Export minimal cover to file in comma-separated format"))
        self.saveBtn.setText(_translate("MainWindow", "Export..."))
        self.fdLabel.setText(_translate("MainWindow", "Functional Dependencies"))
        self.splitBtn.setToolTip(_translate("MainWindow", "Simplify FDs by splitting RHS"))
        self.splitBtn.setText(_translate("MainWindow", "Split RHS"))
        self.clearBtn.setToolTip(_translate("MainWindow", "Clear all functional dependencies"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.addSchemaBtn.setToolTip(_translate("MainWindow", "Add/Remove attributes from current schema"))
        self.addSchemaBtn.setText(_translate("MainWindow", "Edit Schema"))
        self.addFDBtn.setToolTip(_translate("MainWindow", "Add/remove functional dependencies"))
        self.addFDBtn.setText(_translate("MainWindow", "Edit Functional Dependencies"))

