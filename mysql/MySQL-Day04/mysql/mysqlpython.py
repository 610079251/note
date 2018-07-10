from pymysql import *

class mysqlpython:
    def __init__(self,host,port,database,user,
                 password,charset="utf8"):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,
          port=self.port,database=self.database,
          user=self.user,password=self.password,
          charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def zhixing(self,sql):
        self.open()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("ok")
        except Exception as e:
            self.conn.rollback()
            print("Failed",e)
        self.close()






