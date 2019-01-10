import sys
import os
from PyQt5 import QtWidgets
import  design
import numpy as np
from rpy2.robjects.packages import importr
#os.environ['R_USER'] = 'C:/Program Files (x86)/Python37-32/Lib/site-packages/rpy2'
import rpy2.robjects as robjects


robjects.r("source('Ln.R')")
result1 = robjects.r(f"fun.ln()")
print(type(result1))
result2 = np.asarray(result1)
print(type(result2))
result3 = np.array(map(str, result2))
print(type(result3))
result4 = result3.tolist()
#print(result1)
#print(result2)
class pyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listZip.addItems(result4)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = pyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
