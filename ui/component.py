from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from conf.const import *


class font(QFont):
    def __init__(self, Size):
        super().__init__()
        self.setFamily("fira code")
        self.setBold(True)
        self.setPixelSize(Size)


class scanner(QLineEdit):
    def __init__(self, pos, main_widget, tgr):
        super().__init__()
        self.setFont(font(30))
        self.hide()
        self.setGeometry(QRect(pos[0], pos[1], editor[0], editor[1]))
        self.setParent(main_widget)
        self.setStyleSheet("QLineEdit{background-color:rgb(255,255,255);border:none});}")
        self.textChanged[str].connect(tgr)


class printer(QPlainTextEdit):
    def __init__(self, pos, main_widget, text=' ', height=670, width=1000, wsize=20):
        super().__init__()
        self.setReadOnly(True)
        self.setFont(font(wsize))
        self.setPlainText(text)
        self.hide()
        self.setStyleSheet("QPlainTextEdit{background-color:rgb(244,244,244);border:none});}")
        self.setGeometry(QRect(pos[0], pos[1], width, height))
        self.setParent(main_widget)


class buttoner(QPushButton):
    def __init__(self, pos, main_widget, tgr, text="提交"):
        super().__init__()
        self.setFont(font(20))
        self.setGeometry(QRect(pos[0], pos[1], len(text) * wordsize[0], wordsize[1]))
        self.setStyleSheet("QPushButton{color:rgb(0,0,0);border:none;}"
                           "QPushButton::pressed{color:rgb(255,255,255);border:none;}")
        self.setText(text)
        self.setChecked(True)
        self.hide()
        self.setAutoExclusive(True)
        self.clicked.connect(tgr)
        self.setParent(main_widget)


class tabler(QTableWidget):
    def __init__(self, main_widght):
        super().__init__(main_widght)
        self.main_widght = main_widght
        self.setFont(font(16))
        self.setGeometry(QRect(10, 100, 1010, 500))
        self.setParent(main_widght)
        self.hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.verticalHeader().setVisible(False)

    def make(self, col: list, items):
        self.setColumnCount(len(col))
        self.setRowCount(0)
        for i in range(len(items)):
            item = items[i]
            row = self.rowCount()
            self.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.setItem(row, j, item)
        self.setHorizontalHeaderLabels(col)
