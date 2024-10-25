from ui import window
from db import dbconnect
import sys
from models import user


class Manage:
    def __init__(self):
        self.user = None
        self.app = window.QApplication(sys.argv)
        self.conn = dbconnect.DBConnect()
        self.window = window.MainWindow(self)
        self.window.show()
        sys.exit(self.app.exec())

    def setuser(self, userid, pwd, admin=False):
        self.user = user.User(userid, pwd, admin)

    def resetuser(self):
        self.user = None
