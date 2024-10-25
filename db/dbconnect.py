from utils import cache
import pymysql

class DBConnect:
    def __init__(self):
        self.cache = cache.Cache()
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="Bangbangbang123/",
            database="bms"
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            response = self.cursor.fetchall()
            self.cache.add(sql,response)
        except:
            self.conn.rollback()
            response = self.cache.query(sql)
        print(response)
        return response

    def updateBook(self, Book):
        sql = f"UPDATE book SET number = '{Book.number}',author = '{Book.author}', " \
              f"publisher = '{Book.publisher}',pdate = '{Book.pdate}', price = '{Book.price}' where name = '{Book.name}'"
        self.execute(sql)

    def updateUser(self, name, pwd, admin):
        sql = f"UPDATE user SET pwd = '{pwd}', admin = '{admin}' WHERE userId = '{name}'"
        self.execute(sql)

    def insertBook(self, Book):
        sql = (f"INSERT INTO book VALUES ('{Book.number}','{Book.name}','{Book.author}','{Book.publisher}',"
               f"'{Book.pdate}','{Book.price}','{Book.quantity}')")
        print(sql)
        self.execute(sql)

    def insertUser(self, User):
        sql = f"INSERT INTO user VALUES ('{User.username}','{User.password}','{'1' if User.admin else '0'}',0)"
        self.execute(sql)

    def insertRecord(self, Record):
        sql = (f"INSERT INTO record VALUES ('{Record.uuid}','{Record.bookname}','{Record.userid}',{Record.operation},"
               f"'{Record.time}')")
        self.execute(sql)

    def selectBook(self, name):
        if name == '':
            sql = "SELECT * FROM book"
        else:
            sql = f"SELECT * FROM book WHERE name LIKE '%{name}%' or author LIKE '%{name}%'"
        return self.execute(sql)

    def selectBookaccurate(self, name):
        sql = f"SELECT * FROM book WHERE name = '{name}'"
        return self.execute(sql)

    def selectUser(self):
        sql = "SELECT * FROM user"
        return self.execute(sql)

    def selectRecord(self):
        sql = "SELECT * FROM record order by time desc"
        return self.execute(sql)

    def deleteBook(self, name):
        if name == '':
            return
        sql = f"DELETE FROM book WHERE name = '{name}'"
        self.execute(sql)

    def deleteUser(self, name):
        if name == '':
            return
        sql = f"DELETE FROM  user WHERE userId = '{name}'"
        self.execute(sql)

    def deleteRecord(self, uuid):
        if uuid == '':
            return
        sql = f"DELETE FROM record WHERE uuid = '{uuid}'"
        self.execute(sql)

    def selectRecordWithBook(self, name):
        sql = f"SELECT sum(operation) FROM record WHERE bookname = '{name}'"
        print(sql)
        return self.execute(sql)

    def selectRecordWithUser(self, userid):
        sql = f"SELECT sum(operation) FROM record WHERE userid = '{userid}'"
        return self.execute(sql)

    def selectRecordWithUserandBook(self, userid, bookname):
        sql = f"SELECT sum(operation) FROM record WHERE userid = '{userid}' AND bookname = '{bookname}'"
        return self.execute(sql)

    def selectRecordByUser(self, userid):
        sql = f"SELECT * FROM record WHERE userid = '{userid}' ORDER BY time DESC "
        return self.execute(sql)

    def selcetRecordTimeout(self, userid, time):
        sql = f"SELECT bookname FROM record WHERE userid = '{userid}' AND operation = -1 AND time < '{time}' EXCEPT " \
              f"SELECT bookname FROM record WHERE userid = '{userid}' AND operation = 1 "
        return self.execute(sql)

    def selectBookadditional(self):
        sql = 'SELECT bookname,sum(operation) FROM record GROUP BY bookname'
        return self.execute(sql)

    def Online(self, userid):
        sql = f"UPDATE user SET status = '1' WHERE userId = '{userid}'"
        self.execute(sql)

    def Offline(self, userid):
        sql = f"UPDATE user SET status = '0' WHERE userId = '{userid}'"
        self.execute(sql)
