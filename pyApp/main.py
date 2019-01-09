import sys
import os
from PyQt5 import QtWidgets
import  design

class pyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = pyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()