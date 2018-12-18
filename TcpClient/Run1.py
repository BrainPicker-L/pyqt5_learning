from PyQt5.QtWidgets import QApplication, QWidget
from TcpClient.client import Ui_MainWindow
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
import sys


# 客户端与服务器端代码逻辑类似，注释省略

class TcpClient(QWidget, Ui_MainWindow):
    def __init__(self):
        super(TcpClient, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tcpSocket = QTcpSocket(self)
        self.ui.connectButton.clicked.connect(self.buttonConnect)
        #self.tcpSocket.connected.connect(self.sucessConnect)
        self.ui.sendButton.clicked.connect(self.sendInfoMessage)
        #self.tcpSocket.readyRead.connect(self.showMessage)
        #self.ui.closeButton.clicked.connect(self.closeConnect)

    def buttonConnect(self):
        ip = self.ui.IPLineEdit.text()
        port = self.ui.portLineEdit.text()
        print(ip, port)
        self.tcpSocket.connectToHost(QHostAddress(ip), int(port))

    def sucessConnect(self):
        self.ui.showText.setText("成功和服务器建立连接")

    def sendMessage(self):
        message = self.ui.sendText.toPlainText()
        self.communication = QByteArray()
        stream = QDataStream(self.communication, QIODevice.WriteOnly)
        stream.writeQString(message)
        self.tcpSocket.write(self.communication)
        self.ui.sendText.clear()

    def sendInfoMessage(self):
        name = self.ui.lineEdit_3.text()
        sno = self.ui.lineEdit_4.text()
        major = self.ui.lineEdit_5.text()
        message = '姓名: ' + name + '学号: ' + sno + '专业: ' + major
        print(message)
        self.communication = QByteArray()
        stream = QDataStream(self.communication, QIODevice.WriteOnly)
        stream.writeQString(message)
        self.tcpSocket.write(self.communication)
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
    def showMessage(self):
        stream = QDataStream(self.tcpSocket)
        stream.setVersion(QDataStream.Qt_5_10)
        message = stream.readQString()
        self.ui.showText.append(message)

    def closeConnect(self):
        self.tcpSocket.disconnectFromHost()
        self.tcpSocket.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpClient = TcpClient()
    tcpClient.show()
    sys.exit(app.exec())
