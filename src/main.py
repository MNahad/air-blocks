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
        self.setWindowTitle("Please log in")

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

        self.populateView()
        self.populateAdd()

        self.grid.addWidget(self.viewWidget, 0, 0)
        self.grid.addWidget(self.addWidget, 1, 0)

        self.loginUI = login.Login(self)
        self.loginUI.show()


    def populateView(self):
        self.viewButton = widgets.QPushButton(self.viewWidget)


    def populateAdd(self):
        self.addButton = widgets.QPushButton(self.addWidget)


    def loginOK(self):
        self.show()
        self.loginUI.close()


if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    menuUI = Menu()
    sys.exit(app.exec_())
