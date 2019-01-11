import sys
from PyQt5 import QtWidgets
import  design
import numpy as np
import rpy2.robjects as robjects

#Класс UI приложения
class pyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Получение списка индексов округа и приведение его к нужному типу
        list_r = robjects.r(f"fun.zip()")
        list_r = np.asarray(list_r)
        list_r = np.array(map(str, list_r))
        list_r = list_r.tolist()
        list_r = list(list_r)
        list_r.sort()
        self.list_r = list_r
        self.listZip.addItems(self.list_r) #Передача индексов в интерфейс для возможности дальнейшего выбора
        self.listZip.setCurrentRow(0)
        self.pushButtonPredict.clicked.connect(self.Predict) #Присоединение к кнопке функции

    #Функция возвращает предсказанное значение
    def Predict(self):
        #Получение параметров из формы интерфейса
        sqftLiving = self.spinBoxSqftLiving.value()
        yrBuilt = self.spinBoxYrBuilt.value()
        grade = self.spinBoxGrade.value()
        zipcode = self.listZip.currentRow()
        zipcode = self.list_r[zipcode]
        if self.radioButtonYes.isChecked():
            waterfront = 1
        elif self.radioButtonNo.isChecked():
            waterfront = 0

        #Получение предсказанного значения
        predictFromR = robjects.r(f"fun.predict({sqftLiving}, {yrBuilt}, {grade}, {waterfront}, {zipcode})")
        predictFromR = int(predictFromR[0])
        #Проверка предсказанного числа на корректность и его вывод экран
        if predictFromR < 0:
            #В случае ошибки возникает окно с сообщением об ошибке
            self.lcdNumberResult.setProperty("intValue", 0)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Ошибка предсказания')
            msgBox.setWindowTitle('Ошибка')
            msgBox.exec()
        else:
            self.lcdNumberResult.setProperty("intValue", predictFromR)

#Инициализация R и UI
def main():
    robjects.r("source('R.R')")
    app = QtWidgets.QApplication(sys.argv)
    window = pyApp()
    window.show()
    app.exec_()

#Точка старта
if __name__ == '__main__':
    main()
