# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entry_box.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 306)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.schemaView = QtWidgets.QListView(Dialog)
        self.schemaView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.schemaView.setObjectName("schemaView")
        self.gridLayout.addWidget(self.schemaView, 3, 0, 4, 1)
        self.attrLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.attrLabel.setFont(font)
        self.attrLabel.setObjectName("attrLabel")
        self.gridLayout.addWidget(self.attrLabel, 0, 0, 1, 1)
        self.attrEntry = QtWidgets.QLineEdit(Dialog)
        self.attrEntry.setObjectName("attrEntry")
        self.gridLayout.addWidget(self.attrEntry, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.removeBtn = QtWidgets.QPushButton(Dialog)
        self.removeBtn.setObjectName("removeBtn")
        self.gridLayout.addWidget(self.removeBtn, 3, 1, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(Dialog)
        self.confirmBtn.setObjectName("confirmBtn")
        self.gridLayout.addWidget(self.confirmBtn, 1, 1, 1, 1)
        self.schemaLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.schemaLabel.setFont(font)
        self.schemaLabel.setObjectName("schemaLabel")
        self.gridLayout.addWidget(self.schemaLabel, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(Dialog)
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout.addWidget(self.clearBtn, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Entry Form"))
        self.attrLabel.setText(_translate("Dialog", "Enter Attribute"))
        self.removeBtn.setText(_translate("Dialog", "Remove"))
        self.confirmBtn.setText(_translate("Dialog", "Add"))
        self.schemaLabel.setText(_translate("Dialog", "Schema"))
        self.clearBtn.setText(_translate("Dialog", "Clear"))

