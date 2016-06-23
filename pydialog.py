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

from optparse import OptionParser


import modules

from modules import window1


class MainWindow(QDialog, window1.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


def call_parser():
    usage = "usage: %prog [options] MESSAGE"
    parser = OptionParser(usage=usage)
    parser.add_option("--title", help="Dialog title", dest="title", metavar="TITLE")
    parser.add_option("--icon", help="Use icon as the application icon.", dest="icon", metavar="ICON")
    parser.add_option("--yesnocancel", help="Question message box with yes/no/cancel buttons", dest="ync", action="store_true", default=False)
    parser.add_option("--yesno", help="Question message box with yes/no buttons", dest="yn", action="store_true", default=False)
    parser.add_option("--yes-label", help="The label of the yes-button", dest="yeslabel", metavar="LABEL")
    parser.add_option("--no-label", help="The label of the no-button", dest="nolabel", metavar="LABEL")
    parser.add_option("--cancel-label", help="The label of the cancel-button", dest="cancellabel", metavar="LABEL")
    return parser.parse_args()
    


if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    (options, args) = call_parser()
    
    form = MainWindow()
    form.show()

    sys.exit(app.exec_())
