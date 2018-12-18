# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(50, 30, 93, 28))
        self.openButton.setObjectName("openButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(180, 30, 93, 28))
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 72, 15))
        self.label.setObjectName("label")
        self.showText = QtWidgets.QTextEdit(self.centralwidget)
        self.showText.setGeometry(QtCore.QRect(50, 110, 361, 371))
        self.showText.setObjectName("showText")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(430, 110, 321, 371))
        self.groupBox.setObjectName("groupBox")


        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "服务器(端口号:8888)"))
        self.openButton.setText(_translate("MainWindow", "打开服务器"))
        self.closeButton.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "接收数据"))
        self.groupBox.setTitle(_translate("MainWindow", "绘图区"))

