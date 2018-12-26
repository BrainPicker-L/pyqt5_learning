import pickle
import codecs
import os


class DataManagement:
    """
    数据操作类
    """
    datas = []

    def insert_db(self, datainfo):
        """
        新增一条数据记录
        """
        self.datas = self.load()
        for data in self.datas:
            if data["webname"] == datainfo["webname"]:
                return -1
        else:
            self.datas.append(datainfo)
            with codecs.open("data.dat", "wb") as f:
                pickle.dump(self.datas, f)
            return 1

    def save_db(self, datainfo):
        """
        保存所有数据档案
        """
        with codecs.open("data.dat", "wb") as f:
            pickle.dump(datainfo, f)

    def query_db(self, webname = "",username = "",password = ""):
        """
        查找某条密码记录
        """
        if webname:
            for i, data in enumerate(self.datas):
                if data["webname"] == webname:
                    return i
            else:
                return -1
        if username:
            for i, data in enumerate(self.datas):
                if data["username"] == username:
                    return i
            else:
                return -1
        if password:
            for i, data in enumerate(self.datas):
                if data["password"] == password:
                    return i
            else:
                return -1

    def load(self):
        """
        载入数据
        """
        pathname = "data.dat"

        if not(os.path.exists(pathname) and os.path.isfile(pathname)):
            with codecs.open("data.dat", "wb") as f:
                pickle.dump(self.datas, f)

        with codecs.open("data.dat", "rb") as f:
            self.datas = pickle.load(f)
        return self.datas
