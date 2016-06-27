# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogbutton2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 239)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 5)
        self.NOpushButton_2 = QtWidgets.QPushButton(Dialog)
        self.NOpushButton_2.setObjectName("NOpushButton_2")
        self.gridLayout.addWidget(self.NOpushButton_2, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.OKpushButton = QtWidgets.QPushButton(Dialog)
        self.OKpushButton.setObjectName("OKpushButton")
        self.gridLayout.addWidget(self.OKpushButton, 2, 1, 1, 1)
        self.CancelpushButton_3 = QtWidgets.QPushButton(Dialog)
        self.CancelpushButton_3.setObjectName("CancelpushButton_3")
        self.gridLayout.addWidget(self.CancelpushButton_3, 2, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.NOpushButton_2.setText(_translate("Dialog", "No"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.OKpushButton.setText(_translate("Dialog", "OK"))
        self.CancelpushButton_3.setText(_translate("Dialog", "Cancel"))

