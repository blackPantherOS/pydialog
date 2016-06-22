#!/usr/bin/python3

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*************************************************************************************(c)2002-2016********
#
# Rewrite plan of blackPanther App Helper 2016

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication

import modules
from modules import window1

class MainWindow(QDialog, window1.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())
