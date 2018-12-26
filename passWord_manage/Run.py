from passWord_manage.mdata import Mdata
from passWord_manage.create import CreateData
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = Mdata()
    md.show()
    sys.exit(app.exec_())