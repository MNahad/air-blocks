#!/usr/bin/env python3

import sys
import login
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtCore


class Menu(widgets.QMainWindow):
    def __init__(self):
        widgets.QMainWindow.__init__(self)

        self.winDims = [480, 640]
        self.setMinimumSize(QtCore.QSize(self.winDims[0], self.winDims[1]))
        self.setWindowTitle("Main menu")

        self.qtRect = self.frameGeometry()
        self.ctrPoint = widgets.QDesktopWidget().availableGeometry().center()
        self.qtRect.moveCenter(self.ctrPoint)
        self.move(self.qtRect.topLeft())

        self.err = widgets.QErrorMessage()

        self.centralWidget = widgets.QWidget(self)
        self.grid = widgets.QGridLayout(self)
        self.centralWidget.setLayout(self.grid)
        self.setCentralWidget(self.centralWidget)

        self.viewWidget = widgets.QWidget(self)
        self.addWidget = widgets.QWidget(self)
        self.logoutWidget = widgets.QWidget(self)

        self.populateView()
        self.populateAdd()
        self.populateLogout()

        self.grid.addWidget(self.viewWidget, 0, 0)
        self.grid.addWidget(self.addWidget, 0, 1)
        self.grid.addWidget(self.logoutWidget, 1, 1)

        self.loginUI = login.Login(self)
        self.loginUI.show()


    def populateView(self):
        self.viewButton = widgets.QPushButton(
            "VIEW",
            self.viewWidget,
        )


    def populateAdd(self):
        self.addButton = widgets.QPushButton(
            "ADD ENTRY",
            self.addWidget,
        )


    def populateLogout(self):
        self.logoutButton = widgets.QPushButton(
            "LOGOUT",
            self.logoutWidget,
        )
        self.logoutButton.clicked.connect(self.logout)


    def loginOK(self):
        self.uName = self.loginUI.uName.text()
        self.show()
        self.loginUI.close()


    def logout(self):
        self.loginUI = login.Login(self)
        self.loginUI.show()
        self.hide()


class ViewGUI(widgets.QMainWindow):
    def __init__(self):
        widgets.QMainWindow.__init__(self)

        self.winDims = [480, 640]
        self.setMinimumSize(QtCore.QSize(self.winDims[0], self.winDims[1]))
        self.setWindowTitle("View records")

        self.qtRect = self.frameGeometry()
        self.ctrPoint = widgets.QDesktopWidget().availableGeometry().center()
        self.qtRect.moveCenter(self.ctrPoint)
        self.move(self.qtRect.topLeft())

        self.err = widgets.QErrorMessage()

        self.centralWidget = widgets.QWidget(self)
        self.grid = widgets.QGridLayout(self)
        self.centralWidget.setLayout(self.grid)
        self.setCentralWidget(self.centralWidget)


if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    menuUI = Menu()
    sys.exit(app.exec_())
