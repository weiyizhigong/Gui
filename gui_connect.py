from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow,QLineEdit,QVBoxLayout,QLabel,QMenu,QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize,Qt
import sys
from random import choice


# titles = ['my app','my app','still my app','still my app','This is surprising','This is surprising','something went wrong']


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setWindowTitle('my app')
        # self.button = QPushButton('press me')
        # self.button.setCheckable(True)
        # self.button.clicked.connect(self.the_button_is_pressed)
        # # self.button.clicked.connect(self.the_button_is_togged)
        # # self.button.released.connect(self.the_button_is_released)
        # self.setCentralWidget(self.button)
        # self.button_is_checked = False
        # self.button.setChecked(self.button_is_checked)
        # self.windowTitleChanged.connect(self.windowtitlechanged)
        self.label = QLabel('I LOVE ZBY')
        # self.label.setMouseTracking(True)
        # self.setMouseTracking(True)
        # self.text = QLineEdit()
        # self.text.textChanged.connect(self.label.setText)
        # layout = QVBoxLayout()
        # layout.addWidget(self.label)
        # layout.addWidget(self.button)
        # container = QWidget()
        # container.setLayout(layout)
        # self.show()
        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.on_context_menu)
        self.setCentralWidget(self.label)
        self.setFixedSize(600, 400)
    # def the_button_is_pressed(self):
    #     self.button.setText('you have pressed me')
    #     # self.button.setEnabled(False)
    #     title = choice(titles)
    #     print('newWindowTitle:%s' % title)
    #     self.setWindowTitle(title)

    # def windowtitlechanged(self,window_title):
    #     print('windowtitle is changed to:%s' % window_title)
    #     if window_title == 'something went wrong':
    #         self.button.setEnabled(False)

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)
        self.label.setText('mouseMoveEvent')

    def mouseDoubleClickEvent(self, e):
        e.ignore()
        if e.button() == Qt.LeftButton:
            self.label.setText('mouseDoubleClickEvent Left')

        if e.button() == Qt.MiddleButton:
            self.label.setText('mouseDoubleClickEvent Middle')

        if e.button() == Qt.RightButton:
            self.label.setText('mouseDoubleClickEvent Right')

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText('mouseReleaseEvent Left')

        if e.button() == Qt.MiddleButton:
            self.label.setText('mouseReleaseEvent Middle')

        if e.button() == Qt.RightButton:
            self.label.setText('mouseReleaseEvent Right')

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # self.contextMenuEvent(e)
            self.label.setText('mousePressEvent Left')

        if e.button() == Qt.MiddleButton:
            self.label.setText('mousePressEvent Middle')

        if e.button() == Qt.RightButton:
            e.ignore()
            self.label.setText('mousePressEvent Right')

    def contextMenuEvent(self, e):
        menu = QMenu(self)
        menu.addAction(QAction('action1', self))
        menu.addAction(QAction('action2', self))
        menu.addAction(QAction('action3', self))
        menu.exec(e.globalPos())

    # def the_button_is_togged(self):
    #     self.button_is_checked = self.button.isChecked()
    #     print('the button is checked:', self.button_is_checked)
    #
    # def the_button_is_released(self):
    #     self.button_is_checked = self.button.isChecked()
    #     print(self.button_is_checked)


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec_()
