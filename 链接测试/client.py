from PyQt5.QtWidgets import QApplication, QWidget
from TcpClient.client import Ui_Form
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
import sys

#客户端与服务器端代码逻辑类似，注释省略

class TcpClient(QWidget, Ui_Form):
    def __init__(self):
        super(TcpClient, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tcpSocket = QTcpSocket(self)
        self.ui.connectButton.clicked.connect(self.buttonConnect)
        self.tcpSocket.connected.connect(self.sucessConnect)
        self.ui.sendButton.clicked.connect(self.sendMessage)
        self.tcpSocket.readyRead.connect(self.showMessage)
        self.ui.closeButton.clicked.connect(self.closeConnect)

    def buttonConnect(self):
        ip = self.ui.IPLineEdit.text()
        port = self.ui.portLineEdit.text()
        self.tcpSocket.connectToHost(QHostAddress(ip), int(port))

    def sucessConnect(self):
        self.ui.showText.setText("成功和服务器建立连接")

    def sendMessage(self):
        message = self.ui.sendText.toPlainText()
        # self.communication = QByteArray()
        # stream = QDataStream(self.communication, QIODevice.WriteOnly)
        # stream.writeQString(message)
        # self.tcpSocket.write(self.communication)
        # self.ui.sendText.clear()
        message = message.encode(encoding='utf-8')
        self.tcpSocket.write(message)
        self.ui.sendText.clear()

    def showMessage(self):
        # stream = QDataStream(self.tcpSocket)
        # stream.setVersion(QDataStream.Qt_5_10)
        # message = stream.readQString()
        # self.ui.showText.append(message)
        self.message = QByteArray()
        self.message = self.tcpSocket.readAll()
        self.message = str(self.message, encoding='utf-8')          #找遍世界，终于找到可用的方法
        print(self.message)
        self.ui.showText.append(self.message)

    def closeConnect(self):
        self.tcpSocket.disconnectFromHost()
        self.tcpSocket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpClient = TcpClient()
    tcpClient.show()
    sys.exit(app.exec())
