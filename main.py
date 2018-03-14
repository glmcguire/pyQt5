import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QMessageBox, QAction, QLineEdit, QMainWindow, QLabel, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from widget import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 simple window"
        self.left = 10
        self.top = 35
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.create_table()

        # Add box layout
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.tableWidget)
        # self.setLayout(self.layout)

        self.table_widget = AppWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    # Textbox example - Call in initUI function to try
    # Works with App(QWidget)
    def create_text_box(self):
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        # Create a button in the window
        self.button = QPushButton("Show text", self)
        self.button.move(20, 80)
        # Connect button to function on_click
        self.button.clicked.connect(self.on_click_textbox)

    # PyQT slot for textbox example
    @pyqtSlot()
    def on_click_textbox(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    # Example of absolute positioning of widgets
    # Works with App(QWidget) or App(QMainWindow)
    def abs_positioning_example(self):
        label = QLabel("Python", self)
        label.move(50, 50)

        label2 = QLabel("Java", self)
        label2.move(100, 100)

        label3 = QLabel("C++", self)
        label3.move(150, 150)

        label4 = QLabel("Clojure", self)
        label4.move(200, 200)

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    # Tables example
    # Works with App(QWidget)
    def create_table(self):
        # Create Table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0, 0)

        # Table selection change
        self.tableWidget.doubleClicked.connect(self.on_click_table)

    @pyqtSlot()
    def on_click_table(self):
        print("\n")
        for current_qtable_widget_item in self.tableWidget.selectedItems():
            print(current_qtable_widget_item.row(), current_qtable_widget_item.column(),
                  current_qtable_widget_item.text())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
