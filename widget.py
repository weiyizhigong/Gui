from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QMainWindow,
                             QLabel, QLineEdit, QVBoxLayout, QComboBox, QDateEdit,
                             QDateTimeEdit, QDial, QCheckBox, QDoubleSpinBox, QFontComboBox,
                             QLCDNumber, QProgressBar, QRadioButton, QSlider, QSpinBox, QTimeEdit, QListWidget)

from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setWindowTitle('my app')
        # widget = [QPushButton,QLabel,QLineEdit,QComboBox,QDateEdit,QDateTimeEdit,
        #           QDial,QCheckBox,QDoubleSpinBox,QFontComboBox,QLCDNumber,QProgressBar,
        #           QRadioButton,QSlider,QSpinBox,QTimeEdit]
        # layout = QVBoxLayout()
        # for w in widget:
        #     layout.addWidget(w())
        # self.widget = QWidget()
        # Qlabel ##########################################################################################
        # label = QLabel()
        # label.setPixmap(QPixmap(r'C:\Users\xxx\Desktop\zhaopian\微信图片_20240427161107.jpg'))
        # label.setScaledContents(True)
        # font = label.font()
        # font.setPointSize(30)
        # label.setFont(font)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignCenter)

        # QCheckBox########################################################################################
        # checkbox = QCheckBox()
        # # checkbox.setCheckState(Qt.PartiallyChecked)
        # # checkbox.setChecked(False)
        # checkbox.setTristate(True)
        # checkbox.stateChanged.connect(self.state_change)
        # self.widget.setLayout(layout)

        # QComBoBox########################################################################################
        # combobox = QComboBox()
        # combobox.addItems(['I love zby','I love zby exceedingly','I love zby extremely'])
        # combobox.currentIndexChanged.connect(self.show_new_index)
        # combobox.currentTextChanged.connect(self.show_new_text)
        # combobox.setEditable(True)
        # combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        # combobox.setMaxCount(5)

        # QListWidget########################################################################################
        # listwidget = QListWidget()
        # listwidget.addItems(['I love zby','I love zby exceedingly','I love zby extremely'])
        # listwidget.currentItemChanged.connect(self.show_new_index)
        # listwidget.currentTextChanged.connect(self.show_new_text)

        # QEditLine########################################################################################
        # widget = QLineEdit()
        # widget.setMaxLength(20)
        # widget.setPlaceholderText('Enter your text')
        #
        # widget.returnPressed.connect(self.return_pressed)
        # widget.selectionChanged.connect(self.selection_changed)
        # widget.textEdited.connect(self.text_edited)
        # widget.textChanged.connect(self.text_changed)
        # widget.setInputMask('000.000.000.000')

        # QSpinBox########################################################################################
        widget = QSpinBox()
        widget.setMaximum(10)
        widget.setMinimum(-3)
        widget.setSingleStep(3)
        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.textChanged.connect(self.show_new_text)
        widget.valueChanged.connect(self.show_new_text)

        # #################################################################################################
        self.setCentralWidget(widget)
        self.setFixedSize(600, 400)

    def return_pressed(self):
        print('return_pressed')
        self.centralWidget().setText('BOOM')

    def selection_changed(self):
        print('selection_changed')
        print(self.centralWidget().selectedText())

    def text_edited(self,i):
        print('text_edited')
        print(i)

    def text_changed(self,s):
        print('text_changed')
        print(s)
    def show_new_index(self,i):
        print(i.text())

    def show_new_text(self,s):
        print(s)

    def state_change(self,s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec_()

