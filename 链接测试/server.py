from TcpServer.server import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtNetwork import QTcpSocket, QTcpServer, QHostAddress
from PyQt5.QtCore import QByteArray, QDataStream, QIODevice
from TcpClient.TCPClient import TcpClient
import sys



class TcpServer(QWidget, Ui_Form):

    def __init__(self):
        super(TcpServer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tcpServer = QTcpServer(self)                             #指定父对象自动回收空间 监听套接字
        self.tcpSocket = QTcpSocket(self)                             #通信套接字

        self.tcpServer.listen(QHostAddress.Any, 8888)                 #any默认绑定当前网卡的所有IP
        self.tcpServer.newConnection.connect(self.handleNewConnection)
        self.ui.sendButton.clicked.connect(self.sendMessage)
        self.ui.closeButton.clicked.connect(self.closeConnect)

    def handleNewConnection(self):
        self.tcpSocket = self.tcpServer.nextPendingConnection()       #取出建立好链接的套接字
        #获取对方IP和端口
        ip = self.tcpSocket.peerAddress().toString()                  #获取对方的IP地址
        port = self.tcpSocket.peerPort()                              #获取对方的端口号

        self.ui.showText.setText("[{IP}:{Port}]".format(IP=ip, Port=port))
        self.tcpSocket.readyRead.connect(self.showMessage)

    def sendMessage(self):
        # message = self.ui.sendEdit.toPlainText()                      # 获取编辑区内容
        # self.request = QByteArray()                                   #由于write函数的参数是QByteArray, bytes, bytearray所以在这里通过QByteArray来传递参数
        # stream = QDataStream(self.request, QIODevice.WriteOnly)       #创建数据流，和QByteArray关联，并且以只写的方式
        # stream.setVersion(QDataStream.Qt_5_10)                        #设置数据流所对应的PyQt5版本
        # stream.writeQString(message)                                  #向数据流中写入数据，亦即向request中写入数据
        # self.tcpSocket.write(self.request)
        # self.ui.sendEdit.clear()                                      #每次数据发送后，将当前的输入text区域清空

        message = self.ui.sendEdit.toPlainText()
        message = message.encode('utf-8')                                      #encode()转换为bytes类型
        self.tcpSocket.write(message)
        self.ui.sendEdit.clear()


    def showMessage(self):
        # stream = QDataStream(self.tcpSocket)                          #发送数据是以QByteArray数据类型发送过来的，所以接收数据也应该以此接收
        # stream.setVersion(QDataStream.Qt_5_10)                        #发送和接收数据以相同的编码形式传输
        # message = stream.readQString()                                #写入使用writeString, 对应读取使用readQString
        # self.ui.showText.append(message)
        message = QByteArray()
        message = self.tcpSocket.readAll()
        message = str(message, 'utf-8')
        self.ui.showText.setText(message)

    def closeConnect(self):
        self.tcpSocket.disconnectFromHost()
        self.tcpSocket.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tcpClient = TcpClient()
    tcpServer = TcpServer()
    tcpClient.move(100, 100)
    tcpServer.move(600, 100)
    tcpClient.show()
    tcpServer.show()
    sys.exit(app.exec())
