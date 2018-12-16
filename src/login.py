import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtGui


class Login(widgets.QMainWindow):
    def __init__(self):
        widgets.QMainWindow.__init__(self)

        self.winDims = [480, 640]
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

        self.populateHeading()
        self.populateEntry()
        self.populateButton()

        self.grid.addWidget(self.headingWidget, 0, 0)
        self.grid.addWidget(self.entryWidget, 1, 0)
        self.grid.addWidget(self.buttonWidget, 2, 0)

        self.makeMenu()

        self.show()


    def populateHeading(self):
        self.headingTxt = widgets.QLabel(self.headingWidget)
        self.headingTxt.setText("Welcome. Please log in using your credentials.")
        self.headingTxt.setAlignment(QtCore.Qt.AlignCenter)


    def populateEntry(self):
        self.credBox = widgets.QGroupBox("Enter credentials", self.entryWidget)
        self.credLayout = widgets.QFormLayout()
        self.credLayout.addRow(widgets.QLabel("User Name:"), widgets.QLineEdit())
        self.credLayout.addRow(widgets.QLabel("Password:"), widgets.QLineEdit())
        self.credBox.setLayout(self.credLayout)


    def populateButton(self):
        self.submitButton = widgets.QDialogButtonBox(
            widgets.QDialogButtonBox.Ok | widgets.QDialogButtonBox.Cancel,
            self.buttonWidget,
        )
        self.submitButton.accepted.connect(self.submit)
        self.submitButton.rejected.connect(self.close)


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
