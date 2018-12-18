from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.showText = QtWidgets.QTextEdit(Form)
        self.showText.setReadOnly(True)
        self.showText.setObjectName("showText")
        self.gridLayout.addWidget(self.showText, 0, 0, 1, 3)
        self.sendEdit = QtWidgets.QTextEdit(Form)
        self.sendEdit.setObjectName("sendEdit")
        self.gridLayout.addWidget(self.sendEdit, 1, 0, 1, 3)
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setObjectName("sendButton")
        self.gridLayout.addWidget(self.sendButton, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 2, 2, 1, 1)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "服务器(端口号:8888)"))
        self.sendButton.setText(_translate("Form", "send"))
        self.closeButton.setText(_translate("Form", "close"))

