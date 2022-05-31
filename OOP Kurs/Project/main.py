import sys
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from TryServer import DOTA_N_results, CSGO_T_results, CSGO_N_results


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("design.ui", self)
        self.btn_1.clicked.connect(self.gotoWindow1)
        self.btn_2.clicked.connect(self.gotoWindow2)
        self.btn_3.clicked.connect(self.gotoWindow3)
        self.btn_4.clicked.connect(app.quit)

    def gotoWindow1(self, index):

        widget.setCurrentIndex(widget.currentIndex()+1)
        print(widget.currentIndex())
        print(len(widget))

    def gotoWindow2(self, index):

        widget.setCurrentIndex(widget.currentIndex()+2)
        print(widget.currentIndex())
        print(len(widget))

    def gotoWindow3(self, index):

        widget.setCurrentIndex(widget.currentIndex()+3)
        print(widget.currentIndex())
        print(len(widget))


class Window1(QMainWindow):
    def __init__(self):
        super(Window1, self).__init__()
        loadUi("Wind1.ui", self)
        self.btn_1.clicked.connect(self.gotoMainWindow)
        id = 0
        for i in range(len(CSGO_N_results)):
            id += 1
            day = uic.loadUi("PartOfNews.ui")
            day.setObjectName(str(id))
            print("Adding")
            day.label.setText(str(CSGO_N_results[i][2]))
            day.textEdit.setText(str(CSGO_N_results[i][3]))
            day.label_2.setText("Date: " + str(CSGO_N_results[i][1]))
            self.box.addWidget(day)



    def gotoMainWindow(self, index):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Window2(QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()
        loadUi("Wind2.ui", self)
        self.btn_1.clicked.connect(self.gotoMainWindow)
        id = 20
        for i in range(len(DOTA_N_results)):
            id += 1
            day = uic.loadUi("PartOfNews.ui")
            day.setObjectName(str(id))
            print("Adding")
            day.label.setText(str(DOTA_N_results[i][2]))
            day.textEdit.setText(str(DOTA_N_results[i][3]))
            day.label_2.setText("Date: " + str(DOTA_N_results[i][1]))
            self.box.addWidget(day)

    def gotoMainWindow(self, index):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() - 2)


class Window3(QMainWindow):
    def __init__(self):
        super(Window3, self).__init__()
        loadUi("Wind3.ui", self)
        self.btn_1.clicked.connect(self.gotoMainWindow)
        id = 10
        for i in range(len(CSGO_T_results)):
            id += 1
            day = uic.loadUi("PartOfNews2.ui")
            day.setObjectName(str(id))
            print("Adding")
            day.label.setText(str(CSGO_T_results[i][1]))
            day.textEdit.setText(str(CSGO_T_results[i][2]))
            day.label_2.setPixmap(QtGui.QPixmap("Pictures/Training/" + str(CSGO_T_results[i][3]) + ".png"))
            self.box.addWidget(day)

    def gotoMainWindow(self, index):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() - 3)


app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)

window1 = Window1()
widget.addWidget(window1)

window2 = Window2()
widget.addWidget(window2)

window3 = Window3()
widget.addWidget(window3)

widget.showFullScreen()

sys.exit(app.exec())
