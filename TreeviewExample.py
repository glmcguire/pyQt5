import sys
from PyQt5.QtGui import (QIcon, QStandardItemModel)

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel,
                          Qt, QTime)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView,
                             QVBoxLayout, QWidget)


class App(QWidget):

    FROM, SUBJECT, DATE = range(3)

    def __init__(self):
        super.__init__()
        self.title = 'Treeview Example'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 240
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.dataGroupBox = QGroupBox("Inbox")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)
