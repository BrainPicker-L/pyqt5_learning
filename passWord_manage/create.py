from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap

from passWord_manage.UI_infoUI import Ui_MainWindow
from passWord_manage.datamanagement import DataManagement

from PyQt5.QtWidgets import QApplication
import sys

class CreateData(QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CreateData, self).__init__(parent)
        self.setupUi(self)
        self.webname = ""
        self.userame = ""
        self.password = ""
    def accept(self):
        if self.lineEdit.text() == "":
            QMessageBox.information(self, "提示", "网站名称为空!")
        elif self.lineEdit_2.text() == "":
            QMessageBox.information(self, "提示", "账号为空!")
        elif self.lineEdit_3.text() == "":
            QMessageBox.information(self, "提示", "密码为空!")
        else:
            webname = self.lineEdit.text()
            username = self.lineEdit_2.text()
            password = self.lineEdit_3.text()
            data = self.get_datainfo(webname, username, password)
            dm = DataManagement()
            r = dm.insert_db(data)
            if r>0:
                self.done(1)
            else:
                QMessageBox.information(self, "提示", "新增数据项失败貌似已有相同网站存在")
    def reject(self):
        """
        点击取消后
        """

        self.done(-1)
    def get_datainfo(self, webname, username, password):

        data = {"webname": webname, "username": username, "password": password}
        return data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = CreateData()
    md.show()
    sys.exit(app.exec_())