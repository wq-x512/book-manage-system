from ui.page import *
from utils.recycle import *


class MainWindow(QMainWindow):
    def __init__(self, manage):
        super().__init__()
        self.manage = manage
        self.conn = self.manage.conn
        self.recycle = Recycle()
        self.setWindowIcon(QIcon("../pic/icon.ico"))
        self.setWindowTitle("图书管理后台")
        self.setFixedSize(size[0], size[1])
        self.setStyleSheet("background-color:rgb(255,255,255)")
        self.init_widget()

    def init_widget(self):
        # 主菜单
        self.widget_menu = QWidget(self)
        self.widget_menu.setObjectName("widget_menu")
        self.widget_menu.setGeometry(QRect(0, 0, 1024, 50))
        self.widget_menu.setStyleSheet("QWidget{background-color:rgb(255,255,255);border:1px solid balck;}")
        # 主窗口
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(QRect(0, 80, 1024, 600))
        self.main_widget.setStyleSheet("QWidget{background-color:rgb(244,244,244);border:none}")

        # 底部文本框
        self.text_widget = QWidget(self)
        self.text_widget.setGeometry(QRect(0, 680, 1024, 40))
        self.text_widget.setStyleSheet("QWidget{background-color:rgb(200,223,200);border:none}")
        # 底部文字显示
        self.notice = QPlainTextEdit()
        self.notice.setReadOnly(True)
        self.notice.setFont(font(20))
        self.notice.setStyleSheet("QPlainTextEdit{background-color:rgb(200,223,200);border:none});}")
        self.notice.setGeometry(QRect(320, 2, 600, 40))
        self.notice.setParent(self.text_widget)

        self.menuLayout = QHBoxLayout(self.widget_menu)
        self.menuLayout.setSpacing(30)
        self.menuLayout.addSpacing(30)
        self.menuButtonGroup = QButtonGroup(self)
        menuStr = ["图书", "记录", "用户", "登录", "注册"]
        self.font = QFont()
        self.font.setFamily("fira code")
        self.font.setBold(True)
        self.font.setPixelSize(30)
        for i in range(len(menuStr)):
            menuBtn = QPushButton()
            menuBtn.setStyleSheet("QPushButton{color:rgb(0,0,0);border:none;}"
                                  "QPushButton::checked{color:rgb(0,80,180);border:none;}")
            menuBtn.setFont(self.font)
            menuBtn.setText(menuStr[i])
            menuBtn.setParent(self.widget_menu)
            menuBtn.setCheckable(True)
            self.menuLayout.addWidget(menuBtn)
            self.menuButtonGroup.addButton(menuBtn, i)
            if i == 2:
                self.menuLayout.addSpacing(500)
        self.menuButtonGroup.setExclusive(True)
        self.menuLayout.addStretch(True)
        self.slot_functions = [self.Book, self.Record, self.User, self.Login, self.Logup]
        for i in range(len(self.slot_functions)):
            self.menuButtonGroup.button(i).clicked.connect(self.slot_functions[i])
        self.menuLayout.addSpacing(40)
        self.stackedWidget_func = QStackedWidget(self)
        self.stackedWidget_func.setObjectName("stackedWidget_func")
        self.stackedWidget_func.setGeometry(QRect(0, 50, 1280, 40))
        self.stackedWidget_func.setStyleSheet("QWidget {background-color:RGB(255,255,255);border:none;}")
        self.pages = [Page0(self), Page1(self), Page2(self), Page3(self), Page4(self)]
        for _ in self.pages:
            self.stackedWidget_func.addWidget(_)
        self.stackedWidget_func.setCurrentWidget(self.stackedWidget_func)
        self.Login()

    def closeEvent(self, event):
        if self.stackedWidget_func.currentIndex() == 3:
            self.conn.close()
            event.accept()
        else:
            self.warn("Please log out first")
            event.ignore()

    def warn(self, text):
        self.notice.setPlainText(text)
        self.notice.setGeometry(QRect(512 - len(text) * 7, 2, 600, 40))
        self.recycle.queue[self.recycle.idx].append(self.notice)
        self.text_widget.repaint()

    def modify_page(self, idx):
        self.recycle.update([])
        self.stackedWidget_func.setCurrentIndex(idx)
        self.main_widget.repaint()

    def Book(self):
        if self.manage.user is None:
            self.Login()
        else:
            self.modify_page(0)

    def Record(self):
        if self.manage.user is None:
            self.Login()
        else:
            self.modify_page(1)

    def User(self):
        if self.manage.user is None:
            self.Login()
        else:
            self.modify_page(2)

    def Login(self):
        self.buttonmodel(False)
        self.modify_page(3)
        if self.manage.user is not None:
            for i in self.pages:
                i.clear()
            self.resetuser()
        self.pages[3].login()

    def Logup(self):
        self.buttonmodel(False)
        self.modify_page(4)
        for i in self.pages:
            i.clear()
        self.resetuser()
        self.pages[4].logup()

    def setuser(self, userid, pwd, admin=False):
        self.conn.Online(userid)
        self.manage.setuser(userid, pwd, admin)
        self.menuButtonGroup.button(3).setText("登出")
        if self.manage.user.admin is True:
            self.buttonmodel(True)
        self.widget_menu.repaint()

    def resetuser(self):
        if self.manage.user is not None:
            self.conn.Offline(self.manage.user.username)
        self.manage.resetuser()
        self.menuButtonGroup.button(3).setText("登录")
        self.widget_menu.repaint()

    def buttonmodel(self, flag):
        if flag:
            self.menuButtonGroup.button(2).setStyleSheet("QPushButton{color:rgb(0,0,0);border:none;}"
                                                         "QPushButton::checked{color:rgb(0,80,180);border:none;}")
        elif not flag:
            self.menuButtonGroup.button(2).setStyleSheet("QPushButton{color:rgb(255,255,255);border:none;}")
        self.pages[0].ButtonGroup.button(2).setVisible(flag)
        self.pages[0].ButtonGroup.button(3).setVisible(flag)
        self.pages[0].ButtonGroup.button(4).setVisible(flag)
        self.pages[1].ButtonGroup.button(1).setVisible(flag)
        self.menuButtonGroup.button(2).setEnabled(flag)
