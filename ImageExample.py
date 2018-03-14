import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Image'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel(self)
        pixmap = QPixmap('luna.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


# app = QApplication(sys.argv)
#
# grid = QGridLayout()
# browser = QWebEngineView()
# url_input = UrlInput(browser)
#
# grid.addWidget(url_input, 1, 0)
# grid.addWidget(browser, 2, 0)
#
# main_frame = QWidget()
# main_frame.setLayout(grid)
# main_frame.show()
#
# sys.exit(app.exec_())
