from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QComboBox, QMessageBox, QMenu, QAction, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIcon, QPixmap


from passWord_manage.UI_mainUI import Ui_MainWindow
from passWord_manage.create import CreateData

from passWord_manage.datamanagement import DataManagement


from PyQt5.QtWidgets import QApplication
import sys

class Mdata(QMainWindow, Ui_MainWindow):
    """数据管理"""
    datadb = DataManagement()
    datalist = []
    def __init__(self, parent=None):
        super(Mdata, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        searchkey = ["网站名称", "账号", "密码"]
        self.comboBox.addItems(searchkey)
        self.showtable()
    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """双击修改"""
        self.pushButton_2.setEnabled(True)

    def on_tableWidget_itemActivated(self, item):
        """按住Enter键时"""
        row = self.tableWidget.row(item)
        column = self.tableWidget.column(item)
        totalrow = self.tableWidget.rowCount()
        if row + 1 < totalrow:
            row = self.tableWidget.row(item) + 1
            self.tableWidget.setCurrentCell(row, column)
        elif row + 2 == totalrow:
            self.tableWidget.setCurrentCell(totalrow, column)
    @pyqtSlot(int, int, int, int)
    def on_tableWidget_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        """当前单元格改变"""

        if previousColumn == 1:
            webname = self.tableWidget.item(previousRow, previousColumn).text()
            self.datalist[previousRow]["webname"] = webname
        if previousColumn == 2:
            username = self.tableWidget.item(previousRow, previousColumn).text()
            self.datalist[previousRow]["username"] = username
        if previousColumn == 3:
            password = self.tableWidget.item(previousRow, previousColumn).text()
            self.datalist[previousRow]["password"] = password

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """查找数据"""


        searchtext = self.lineEdit.text()
        if searchtext:
            if self.comboBox.currentText() == "网站名称":
                index = self.datadb.query_db(webname=searchtext)
            elif self.comboBox.currentText() == "账号":
                index = self.datadb.query_db(username=searchtext)
            elif self.comboBox.currentText() == "密码":
                index = self.datadb.query_db(password=searchtext)
            if index > -1:
                self.tableWidget.selectRow(index)
            else:
                QMessageBox.information(self, "提示", "没有找到本条数据记录")
        else:
            QMessageBox.information(self, "提示", "搜索内容为空！")
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """新增数据"""
        try:
            datainfo = CreateData()
            r = datainfo.exec_()
            if r > 0:
                self.showtable()
        except:
            print("66666666")

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """保存修改"""
        self.datadb.save_db(self.datadb)
        QMessageBox.information(self, "提示", "保存成功！")
        self.pushButton_2.setEnabled(False)


    def showtable(self):
        """表格呈现"""
        self.datalist = self.datadb.load()
        print(self.datalist)
        list_rows = len(self.datalist)
        table_rows = self.tableWidget.rowCount()
        if table_rows == 0 and list_rows > 0:
            self.selectTable(self.datalist, table_rows)
        elif table_rows > 0 and list_rows > 0:
            self.removeRows(table_rows)
            self.selectTable(self.datalist, table_rows)

    def selectTable(self, datalist, table_rows):
        """表格呈现具体数据"""
        print(datalist)
        for i, data in enumerate(datalist):
            webname = data["webname"]
            username = data["username"]
            password = data["password"]

            self.tableWidget.insertRow(i)

            webname_item = QTableWidgetItem(webname)
            webname_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            username_item = QTableWidgetItem(username)
            username_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            password_item = QTableWidgetItem(password)
            password_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget.setItem(i, 0, webname_item)
            self.tableWidget.setItem(i, 1, username_item)
            self.tableWidget.setItem(i, 2, password_item)

    def contextMenuEvent(self, event):
        """右键菜单删除行"""
        pmenu = QMenu(self)
        pDeleteAct = QAction('删除行', self.tableWidget)
        pmenu.addAction(pDeleteAct)
        pDeleteAct.triggered.connect(self.deleterows)
        pmenu.popup(self.mapToGlobal(event.pos()))

    def deleterows(self):
        """
        删除行
        """
        rr = QMessageBox.warning(self, "注意", "删除可不能恢复了哦！", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if rr == QMessageBox.Yes:
            curow = self.tableWidget.currentRow()
            selections = self.tableWidget.selectionModel()
            selectedsList = selections.selectedRows()
            rows = []
            for r in selectedsList:
                rows.append(r.row())
            if len(rows) == 0:
                rows.append(curow)
                self.removeRows(rows, isdel_list = 1)
            else:
                self.removeRows(rows, isdel_list = 1)

    def removeRows(self, rows, isdel_list=0):
        """
        删除单元格
        """
        if isdel_list != 0:
            rows.reverse()
            for i in rows:
                self.tableWidget.removeRow(i)
                del self.datalist[i]
            self.bookdb.save_db(self.datalist)
        else:
            for i in range(rows - 1, -1, -1):
                self.tableWidget.removeRow(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = Mdata()
    md.show()
    sys.exit(app.exec_())