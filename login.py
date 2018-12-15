import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtGui


class Login(widgets.QMainWindow):
    def __init__(self):
        widgets.QMainWindow.__init__(self)

        self.winDims = [1024, 576]
        self.setMinimumSize(QtCore.QSize(self.winDims[0], self.winDims[1]))
        self.setWindowTitle("Please log in")

        self.qtRect = self.frameGeometry()
        self.ctrPoint = widgets.QDesktopWidget().availableGeometry().center()
        self.qtRect.moveCenter(self.ctrPoint)
        self.move(self.qtRect.topLeft())

        self.centralWidget = widgets.QWidget(self)
        self.grid = widgets.QGridLayout(self)
        self.centralWidget.setLayout(self.grid)
        self.setCentralWidget(self.centralWidget)

        self.headingWidget = widgets.QWidget(self)
        self.entryWidget = widgets.QWidget(self)
        self.buttonWidget = widgets.QWidget(self)

        self.popHeading()
        self.popEntry()
        self.popButton()

        self.grid.addWidget(self.headingWidget, 0, 0)
        self.grid.addWidget(self.entryWidget, 1, 0)
        self.grid.addWidget(self.buttonWidget, 2, 0)

        self.makeMenu()

        self.show()


    def popHeading(self):
        self.headingTxt = widgets.QLabel(self.headingWidget)
        self.headingTxt.setText("Welcome. Please log in using your credentials.")
        self.headingTxt.setAlignment(QtCore.Qt.AlignCenter)


    def popEntry(self):
        self.unameLabel = widgets.QLabel(self.entryWidget)
        self.unameLabel.setText('User Name:')
        self.unameBox = widgets.QLineEdit(self.entryWidget)

        self.passwdLabel = widgets.QLabel(self.entryWidget)
        self.passwdLabel.setText('Password:')
        self.passwdBox = widgets.QLineEdit(self.entryWidget)

        self.entryGrid = widgets.QGridLayout(self.entryWidget)
        self.entryWidget.setLayout(self.entryGrid)
        self.entryGrid.addWidget(self.unameLabel, 0, 0)
        self.entryGrid.addWidget(self.unameBox, 0, 1)
        self.entryGrid.addWidget(self.passwdLabel, 1, 0)
        self.entryGrid.addWidget(self.passwdBox, 1, 1)


    def popButton(self):
        self.submitButton = widgets.QPushButton("Submit", self.buttonWidget)
        self.submitButton.clicked.connect(self.submit)
        self.submitButton.setToolTip("Submit your credentials")

        self.exitButton = widgets.QPushButton("Exit", self.buttonWidget)
        self.exitButton.clicked.connect(self.close)
        self.exitButton.setToolTip("Exit application")

        self.buttonGrid = widgets.QGridLayout(self.buttonWidget)
        self.buttonWidget.setLayout(self.buttonGrid)
        self.buttonGrid.addWidget(self.submitButton, 0, 0)
        self.buttonGrid.addWidget(self.exitButton, 0, 1)


    def submit(self):
        pass


    def makeMenu(self):
        about = widgets.QAction(QtGui.QIcon('assets/about.png'), '&About', self)
        about.setShortcut('F1')
        about.setStatusTip('About Application')
        about.triggered.connect(self.aboutApp)

        menu = self.menuBar()
        menuAbout = menu.addMenu('&About')
        menuAbout.addAction(about)


    def aboutApp(self):
        widgets.QMessageBox.about(
            self,
            "About this Application",
            "Details about this application can be found on https://GitHub.com/MNahad",
        )


if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    mainLogin = Login()
    sys.exit(app.exec_())
