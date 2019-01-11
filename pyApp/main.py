import sys
from PyQt5 import QtWidgets
import  design
import numpy as np
import rpy2.robjects as robjects

class pyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        list_r = robjects.r(f"fun.zip()")
        list_r = np.asarray(list_r)
        list_r = np.array(map(str, list_r))
        list_r = list_r.tolist()
        list_r = list(list_r)
        list_r.sort()
        self.list_r = list_r
        self.listZip.addItems(self.list_r)
        self.pushButtonPredict.clicked.connect(self.Predict)
        self.listZip.setCurrentRow(0)

    def Predict(self):
        sqftLiving = self.spinBoxSqftLiving.value()
        yrBuilt = self.spinBoxYrBuilt.value()
        grade = self.spinBoxGrade.value()
        zipcode = self.listZip.currentRow()
        zipcode = self.list_r[zipcode]
        if self.radioButtonYes.isChecked():
            waterfront = 1
        elif self.radioButtonNo.isChecked():
            waterfront = 0

        predictFromR = robjects.r(f"fun.predict({sqftLiving}, {yrBuilt}, {grade}, {waterfront}, {zipcode})")
        predictFromR = int(predictFromR[0])
        self.lcdNumberResult.setProperty("intValue", predictFromR)

def main():
    robjects.r("source('R.R')")
    app = QtWidgets.QApplication(sys.argv)
    window = pyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
