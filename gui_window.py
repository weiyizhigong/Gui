from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow,QWidget
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import QSize
import sys


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setWindowTitle('app')
        button = QPushButton('press me')
        self.setCentralWidget(button)
        self.setMinimumSize(QSize(400,300))
        self.setMaximumSize(QSize(800,600))
        button.setCheckable(True)
        button.clicked.connect(self.clicked)

    def clicked(self,checked):
        print(checked)


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec_()
