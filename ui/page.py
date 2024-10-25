from models.record import *
from utils.tools import *
from .component import *
from PyQt5.QtWidgets import *
from models.book import *
from models.user import *
from conf.const import *


class Page(QWidget):
    def __init__(self, buttons, functions, window):
        super().__init__()
        self.window = window
        self.conn = self.window.conn
        self.main_widget = window.main_widget
        self.text_widget = window.text_widget
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0, 0, 1024, 80)
        self.hLayout.setSpacing(30)
        self.hLayout.addSpacing(10)
        self.font = font(20)
        self.total = []
        self.message = {}
        self.ButtonGroup = QButtonGroup(self)
        for i in range(len(buttons)):
            btn = QPushButton(self)
            btn.setStyleSheet("QPushButton{background-color:rgb(255,255,255);border:none;}"
                              "QPushButton:pressed{background-color:rgb(33, 150, 243);border:none;}")
            btn.setFont(self.font)
            btn.setText(buttons[i])
            btn.setFixedSize(20 * len(buttons[i]), 30)
            btn.setParent(self)
            btn.setChecked(True)
            btn.clicked.connect(functions[i])
            self.hLayout.addWidget(btn)
            self.ButtonGroup.addButton(btn, i)
        self.ButtonGroup.setExclusive(True)

    def clear(self):
        for i in self.total:
            if isinstance(i,scanner):
                i.clear()


class Page0(Page):  # 图书管理
    def __init__(self, window):
        super().__init__(['查询', '借还', '插入', '删除', '修改'],
                         [self.select, self.borrow_return, self.insert, self.delete, self.modify],
                         window)
        # 查询界面的显示 0,1,2
        # 插入界面 3,4,5,6,7,8,9,10,11,12,13,14,15
        # 删除界面 16,17
        # 借还界面 18,19,20
        self.total = [tabler(self.main_widget),
                      scanner([20, 20], self.main_widget, self.tgr0),
                      buttoner([400, 30], self.main_widget, self.submission0),
                      buttoner([460, 400], self.main_widget, self.submit0),
                      scanner([100, 100], self.main_widget, self.Onchange0),
                      printer([230, 60], self.main_widget, "编号", height=40, width=56),
                      scanner([520, 100], self.main_widget, self.Onchange1),
                      printer([650, 60], self.main_widget, "书名", 40, 56),
                      scanner([100, 200], self.main_widget, self.Onchange2),
                      printer([230, 160], self.main_widget, "作者", 40, 56),
                      scanner([520, 200], self.main_widget, self.Onchange3),
                      printer([640, 160], self.main_widget, "出版社", 40, 3 * 28),
                      scanner([100, 300], self.main_widget, self.Onchange4),
                      printer([210, 260], self.main_widget, "出版时间", 40, 4 * 28),
                      scanner([520, 300], self.main_widget, self.Onchange5),
                      printer([650, 260], self.main_widget, "价格", 40, 56),
                      buttoner([460, 340], self.main_widget, self.submit1),
                      scanner([320, 270], self.main_widget, self.Onchange6),
                      buttoner([520, 370], self.main_widget, self.submit2, text='借书'),
                      buttoner([400, 370], self.main_widget, self.submit3, text='还书'),
                      scanner([320, 300], self.main_widget, self.Onchange7),  # 20

                      printer([70, 40], self.main_widget, "书名", 40, 56),
                      scanner([150, 30], self.main_widget, self.Onchange8),
                      buttoner([520, 40], self.main_widget, self.submit4),
                      scanner([100, 200], self.main_widget, self.Onchange9),
                      printer([230, 160], self.main_widget, "编号", height=40, width=56),
                      scanner([520, 200], self.main_widget, self.Onchange10),
                      printer([650, 160], self.main_widget, "作者", 40, 56),
                      scanner([100, 300], self.main_widget, self.Onchange11),
                      printer([230, 260], self.main_widget, "出版社", 40, 84),
                      scanner([520, 300], self.main_widget, self.Onchange12),
                      printer([640, 260], self.main_widget, "出版时间", 40, 112),
                      scanner([100, 400], self.main_widget, self.Onchange13),
                      printer([210, 360], self.main_widget, "价格", 40, 2 * 28),
                      ]
        self.message = {
            'selectname': '',
            'number': '',
            'name': '',
            'author': '',
            'publisher': '',
            'pdate': '',
            'price': '',
            'delname': '',
            'bookname': '',
            'upname': '',
            'upid': '',
            'upauthor': '',
            'uppublish': '',
            'update': '',
            'upprice': ''
        }

    def tgr0(self, text):
        self.message['selectname'] = text

    # 查询书籍
    def submission0(self):
        self.total[0].make(bookheader, convertBook(self.conn.selectBook(self.message['selectname']),
                                                   self.conn.selectBookadditional()))
        self.main_widget.repaint()

    def Onchange0(self, text):
        self.message['number'] = text

    def Onchange1(self, text):
        self.message['name'] = text

    def Onchange2(self, text):
        self.message['author'] = text

    def Onchange3(self, text):
        self.message['publisher'] = text

    def Onchange4(self, text):
        self.message['pdate'] = text

    def Onchange5(self, text):
        self.message['price'] = text

    def Onchange6(self, text):
        self.message['delname'] = text

    def Onchange7(self, text):
        self.message['bookname'] = text

    def Onchange8(self, text):
        self.message['upname'] = text

    def Onchange9(self, text):
        self.message['upid'] = text

    def Onchange10(self, text):
        self.message['upauthor'] = text

    def Onchange11(self, text):
        self.message['uppublish'] = text

    def Onchange12(self, text):
        self.message['update'] = text

    def Onchange13(self, text):
        self.message['upprice'] = text

    # 插入书籍
    def submit0(self):
        try:
            self.conn.insertBook(Book(self.message['number'], self.message['name'], self.message['author'],
                                      self.message['publisher'], self.message['pdate'], self.message['price'], 3))
            self.window.warn("Added successfully")
        except:
            self.window.warn("Added failed")

    # 删除书籍
    def submit1(self):
        try:
            self.conn.deleteBook(self.message['delname'])
            self.window.warn("Delete successfully")
        except:
            self.window.warn("Delete failed")

    # 借书
    def submit2(self):
        # 没有库存
        var = self.conn.selectRecordWithBook(self.message['bookname'])[0][0]
        if var is not None:
            if (self.conn.selectBookaccurate(self.message['bookname'])[0][6]
                    + var == 0):
                self.window.warn(f"There are no extra 《{self.message['bookname']}》 in the library")
                return
        # 借过这本书
        if self.conn.selectRecordWithUserandBook(self.window.manage.user.username, self.message['bookname'])[0][0] == -1:
            self.window.warn(f"You have already borrowed 《{self.message['bookname']}》")
            return
        # 有书未还

        if len(self.conn.selcetRecordTimeout(self.window.manage.user.username, diff_time())) != 0:
            self.window.warn("You still have books to return")
            return
        # 接了两本书
        if self.conn.selectRecordWithUser(self.window.manage.user.username)[0][0] == -2:
            self.window.warn("Exceeding maximum limit")
            return
        try:
            books = self.conn.selectBook('')
            for book in books:
                if self.message['bookname'] == book[1]:
                    self.conn.insertRecord(
                        Record(generate_u_uid(), self.message['bookname'], self.window.manage.user.username, -1,
                               get_time()))
                    self.window.warn("Borrowed successfully")
                    return
        except:
            self.window.warn("Borrowed failed")

    # 还书
    def submit3(self):
        book = self.conn.selectRecordWithUserandBook(self.window.manage.user.username, self.message['bookname'])[0][0]
        if book is None or int(book) == 0:
            self.window.warn(f"You havn't borrowed 《{self.message['bookname']}》 before")
            return
        else:
            try:
                self.conn.insertRecord(
                    Record(generate_u_uid(), self.message['bookname'], self.window.manage.user.username, 1,
                           get_time()))
                self.window.warn("Successfully returned the book")
                return
            except:
                self.window.warn("Book return failed")

    # 更新书籍
    def submit4(self):
        books = self.conn.selectBookaccurate(self.message['upname'])
        if books[0][0] is None:
            self.window.warn("No Book")
            return
        oldbook = books[0]
        try:
            self.conn.updateBook(
                Book(self.message['upid'] if self.message['upid'] != '' else oldbook[0],
                     self.message['upname'] if self.message['upname'] != '' else oldbook[1],
                     self.message['upauthor'] if self.message['upauthor'] != '' else oldbook[2],
                     self.message['uppublish'] if self.message['uppublish'] != '' else oldbook[3],
                     self.message['update'] if self.message['update'] != '' else oldbook[4],
                     self.message['upprice'] if self.message['upprice'] != '' else oldbook[5]
                     , oldbook[6]))
            self.window.warn("Book update successful")
        except:
            self.window.warn("Book update failed")

    def select(self):
        self.window.recycle.update(self.total[0:3])
        self.total[0].make(bookheader, convertBook(self.conn.selectBook(''), self.conn.selectBookadditional()))
        self.main_widget.repaint()

    def insert(self):
        self.window.recycle.update(self.total[3:16])
        self.main_widget.repaint()

    def delete(self):
        self.window.recycle.update(self.total[16:18])
        self.main_widget.repaint()

    def borrow_return(self):
        self.window.recycle.update(self.total[18:21])
        self.main_widget.repaint()

    def modify(self):
        self.window.recycle.update(self.total[21:])
        self.main_widget.repaint()


class Page1(Page):  # 记录管理
    def __init__(self, window):
        super().__init__(['查询', '删除'], [self.select, self.delete], window)
        self.total = [tabler(self.main_widget),
                      scanner([320, 260], self.main_widget, self.Onchange0),
                      buttoner([460, 340], self.main_widget, self.submit0)]

    def Onchange0(self, text):
        self.message['uuid'] = text

    def submit0(self):
        try:
            self.conn.deleteRecord(self.message['uuid'])
            self.window.warn("Record deleted successfully")
        except:
            self.window.warn("Record deletion failed")

    def select(self):
        self.window.recycle.update(self.total[0:1])
        try:
            if self.window.manage.user.admin:
                self.total[0].make(recordheader, convertRecord(self.conn.selectRecord()))
            else:
                self.total[0].make(recordheader,
                                   convertRecord(self.conn.selectRecordByUser(self.window.manage.user.username)))
            self.main_widget.repaint()
        except:
            self.main_widget.repaint()

    def delete(self):
        self.window.recycle.update(self.total[1:])
        self.main_widget.repaint()


class Page2(Page):  # 用户管理
    def __init__(self, window):
        super().__init__(['查询', '删除', '更新'], [self.select, self.delete, self.modify], window)
        self.total = [tabler(self.main_widget),
                      scanner([320, 260], self.main_widget, self.Onchange0),
                      buttoner([460, 340], self.main_widget, self.submit0),
                      scanner([320, 200], self.main_widget, self.Onchange1),
                      scanner([320, 260], self.main_widget, self.Onchange2),
                      buttoner([460, 340], self.main_widget, self.submit1),
                      buttoner([700, 240], self.main_widget, self.Onchange3, text='管理员')]
        self.message = {
            'name': '',
            'updatename': '',
            'updatepwd': '',
            'admin': '0',
        }

    def Onchange0(self, text):
        self.message['name'] = text

    def Onchange1(self, text):
        self.message['updatename'] = text

    def Onchange2(self, text):
        self.message['updatepwd'] = text

    def Onchange3(self):
        if self.message['admin'] == '0':
            self.message['admin'] = '1'
        else:
            self.message['admin'] = '0'

    def submit0(self):
        if self.message['name'] == superadministrator:
            self.window.warn("You can't delete super administrator")
            return
        var = self.conn.selectRecordWithUser(self.message['name'])[0][0]
        if var is not None and var != 0:
            self.window.warn("需要先还书")
            return
        for user in self.conn.selectUser():
            if user[0] == self.message['name']:
                if user[0] == self.window.manage.user.username:
                    self.window.warn("You can't delete yourself")
                    return
                self.conn.deleteUser(self.message['name'])
                self.conn.execute(f"update record set userid = '' where userid = '{self.message['name']}'")
                self.window.warn("Operation successful")
                return
        self.window.warn(f"user '{self.message['name']}' does not exist!")

    def submit1(self):
        for user in self.conn.selectUser():
            if user[0] == self.message['updatename']:
                self.conn.updateUser(self.message['updatename'],
                                     encrypted(self.message['updatepwd']) if self.message['updatepwd'] != '' else user[1],
                                     self.message['admin'])
                self.window.warn("updated")
                return
        self.window.warn(f"user '{self.message['updatename']}' does not exist!")

    def select(self):
        self.window.recycle.update([self.total[0]])
        try:
            self.total[0].make(userheader, convertUser(self.conn.selectUser()))
            self.main_widget.repaint()
        except:
            self.total[0].make(userheader, [[]])
            self.main_widget.repaint()

    def delete(self):
        self.window.recycle.update(self.total[1:3])
        self.main_widget.repaint()

    def modify(self):
        self.window.recycle.update(self.total[3:])
        self.main_widget.repaint()


class Page3(Page):  # 登录
    def __init__(self, window):
        super().__init__([], [], window)
        self.total = [scanner([340, 200], self.main_widget, self.Onchanged0),
                      scanner([340, 280], self.main_widget, self.Onchanged1),
                      buttoner([480, 360], self.main_widget, self.submit)]
        self.total[1].setEchoMode(QLineEdit.Password)
        self.message = {
            'userid': '',
            'pwd': ''
        }

    def Onchanged0(self, text):
        self.message['userid'] = text

    def Onchanged1(self, text):
        self.message['pwd'] = text

    def submit(self):
        if self.message['userid'] == '' or self.message['pwd'] == '':
            self.window.warn('Id or pwd is empty')
            return
        users = self.conn.selectUser()
        for user in users:
            if user[0] == self.message['userid']:
                if user[1] == encrypted(self.message['pwd']):
                    if user[3] == 0:
                        self.window.setuser(user[0], user[1], True if user[2] == '1' else False)
                        self.window.recycle.update([])
                        self.clear()
                        self.window.modify_page(0)
                        return
                    else:
                        self.window.warn("You account is online")
                        return
                else:
                    self.window.warn("The password is incorrect!")
                    return
        self.window.warn(f"User '{self.message['userid']}' does not exist")

    def login(self):
        self.window.recycle.update(self.total)
        self.main_widget.repaint()


class Page4(Page):  # 注册管理
    def __init__(self, window):
        super().__init__([], [], window)
        self.total = [scanner([340, 200], self.main_widget, self.Onchanged0),
                      scanner([340, 280], self.main_widget, self.Onchanged1),
                      buttoner([480, 360], self.main_widget, self.submit)]

    def Onchanged0(self, text):
        self.message['userid'] = text

    def Onchanged1(self, text):
        self.message['pwd'] = text

    def submit(self):
        if self.message['userid'] == '' or self.message['pwd'] == '':
            self.window.warn('Id or pwd is empty')
            return
        for user in self.conn.selectUser():
            if self.message['userid'] == user[0]:
                self.window.warn(f"User '{self.message['userid']}' already exists!")
                return
        try:
            self.conn.insertUser(User(self.message['userid'], encrypted(self.message['pwd'])))
            self.window.setuser(self.message['userid'], encrypted(self.message['pwd']))
            self.window.modify_page(0)
            self.window.warn("Registered successful")
            self.clear()
        except:
            self.window.warn("Registered failed!")

    def logup(self):
        self.window.recycle.update(self.total)
        self.main_widget.repaint()
