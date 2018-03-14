import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QAction, QApplication, QLineEdit, QMainWindow,
                             QSizePolicy, QTextEdit)
from PyQt5.QtNetwork import QNetworkProxyFactory, QNetworkRequest
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class MyBrowser(QMainWindow):
    def __init__(self, url):
        super(QMainWindow, self).__init__()

        self.progress = 0

        QNetworkProxyFactory.setUseSystemConfiguration(True)

        self.generateView(url)
        self.editLocation()
        self.generateToolBar()
        self.generateViewMenu()
        self.generateEffectMenu()
        self.generateToolsMenu()

        self.setCentralWidget(self.view)

    def generateToolsMenu(self):
        """Method generates the Tools menu on the tool bar and adds actions to it."""
        toolsMenu = self.menuBar().addMenu("&Tools")
        toolsMenu.addAction("Filler Action")

    def generateViewMenu(self):
        """Method generates the View menu on the tool bar and adds actions to it."""
        viewMenu = self.menuBar().addMenu("&View")
        viewSourceAction = QAction("Page Source", self)
        # viewSourceAction.triggered.connect(self.viewSource)
        viewMenu.addAction(viewSourceAction)

    def generateEffectMenu(self):
        """Method generates the Effect menu on the tool bar and adds actions to it."""
        effectMenu = self.menuBar().addMenu("&Effect")
        effectMenu.addAction("Filler Action")

    def editLocation(self):
        """Method edits the URL location based on what is typed into the url bar."""
        self.locationEdit = QLineEdit(self)
        self.locationEdit.setSizePolicy(QSizePolicy.Expanding,
                                        self.locationEdit.sizePolicy().verticalPolicy())
        self.locationEdit.returnPressed.connect(self.changeLocation)

    def generateToolBar(self):
        """Method generates the navigation tool bar. It then adds the Back, Forward,
        Reload, Stop, and URL bar functionality to it."""
        toolBar = self.addToolBar("Navigation")
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Back))
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Forward))
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Reload))
        toolBar.addAction(self.view.pageAction(QWebEnginePage.Stop))
        toolBar.addWidget(self.locationEdit)

    def generateView(self, url):
        """Method generates the QWebEngineView and handles all page loading."""
        self.view = QWebEngineView(self)
        self.view.load(url)
        self.view.loadFinished.connect(self.adjustLocation)
        self.view.titleChanged.connect(self.adjustTitle)
        self.view.loadProgress.connect(self.setProgress)
        self.view.loadFinished.connect(self.finishLoading)

    # networkAcccessManager does not work with QWebEnginePage. Need to research
    # how to do with QtWebEngine.
    def viewSource(self):
        """WIP Method: It should allow user to view the page source."""
        accessManager = self.view.page().networkAccessManager()
        request = QNetworkRequest(self.view.url())
        reply = accessManager.get(request)
        reply.finished.connect(self.slotSourceDownloaded)

    def slotSourceDownloaded(self):
        """Downloads source code."""
        reply = self.sender()
        self.textEdit = QTextEdit()
        self.textEdit.setAttribute(Qt.WA_DeleteOnClose)
        self.textEdit.show()
        self.textEdit.setPlainText(QTextStream(reply).readAll())
        self.textEdit.resize(600, 400)
        reply.deleteLater()

    def adjustLocation(self):
        """Adjusts url location when called."""
        self.locationEdit.setText(self.view.url().toString())

    def changeLocation(self):
        """Similar to adjustLocation, however only changes based on user
        input into the URL bar."""
        url = QUrl.fromUserInput(self.locationEdit.text())
        self.view.load(url)
        self.view.setFocus()

    def adjustTitle(self):
        """Adjusts the window's title based on the website visited. Also shows page loading
        as a percentage."""
        if 0 < self.progress < 100:
            self.setWindowTitle("%s (%s%%)" % (self.view.title(), self.progress))
        else:
            self.setWindowTitle(self.view.title())

    def setProgress(self, p):
        """Sets the page progress and calls adjustTitle."""
        self.progress = p
        self.adjustTitle()

    def finishLoading(self):
        """When the progress is 100%, changes the window's title to its text value
        without the progress displayed."""
        self.progress = 100
        self.adjustTitle()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    if len(sys.argv) > 1:
        url = QUrl(sys.argv[1])
    else:
        url = QUrl('http://www.google.com/ncr')

    browser = MyBrowser(url)
    browser.showMaximized()

    sys.exit(app.exec_())
