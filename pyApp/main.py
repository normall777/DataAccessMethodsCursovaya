import sys
import os
from PyQt5 import QtWidgets
import  design
import numpy as np
from rpy2.robjects.packages import importr
#os.environ['R_USER'] = 'C:/Program Files (x86)/Python37-32/Lib/site-packages/rpy2'
import rpy2.robjects as robjects


robjects.r("source('R.R')")
result = robjects.r(f"fun.ln()")
result = np.asarray(result)
result = np.array(map(str, result))
result = result.tolist()


class pyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listZip.addItems(result)
        self.pushButtonPredict.clicked.connect(self.Predict)
        self.listZip.setCurrentRow(0)

    def Predict(self):
        sqftLiving = self.spinBoxSqftLiving.value()
        yrBuilt = self.spinBoxYrBuilt.value()
        grade = self.spinBoxGrade.value()
        zipcode = self.listZip.currentItem()

        if self.radioButtonYes.isChecked():
            waterfront = 1
        elif self.radioButtonNo.isChecked():
            waterfront = 0

        print(zipcode, type(zipcode))
        #predictFromR = robjects.r(f"fun.predict({sqftLiving}, {yrBuilt}, {grade}, {waterfront}, {zipcode})")
        predictFromR = robjects.r(f"fun.predict(2570, 1951, 7, 0, 98125)")
        predictFromR = int(predictFromR[0])
        self.lcdNumberResult.setProperty("intValue", predictFromR)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = pyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
