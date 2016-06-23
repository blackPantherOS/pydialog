#!/usr/bin/python3

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*************************************************************************************(c)2002-2016********

import sys
import gettext

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication

from optparse import OptionParser


import modules

from modules import window1


gettext.install("pydialog", "/usr/share/locale")


class MainWindow(QDialog, window1.Ui_Dialog):
    def __init__(self, parent=None, options=None, args=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        


def call_parser():
    usage = _("usage: %prog [options] MESSAGE")
    parser = OptionParser(usage=usage)
    parser.add_option("--title", help=_("Dialog title"), dest="title", metavar=_("TITLE"))
    parser.add_option("--icon", help=_("Use icon as the application icon."), dest="icon", metavar=_("ICON"))
    parser.add_option("--yesnocancel", help=_("Question message box with yes/no/cancel buttons"), dest="ync", action="store_true", default=False)
    parser.add_option("--yesno", help=_("Question message box with yes/no buttons"), dest="yn", action="store_true", default=False)
    parser.add_option("--yes-label", help=_("The label of the yes-button"), dest="yeslabel", metavar=_("LABEL"))
    parser.add_option("--no-label", help=_("The label of the no-button"), dest="nolabel", metavar=_("LABEL"))
    parser.add_option("--cancel-label", help=_("The label of the cancel-button"), dest="cancellabel", metavar=_("LABEL"))
    return parser.parse_args()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    (options, args) = call_parser()
    
    form = MainWindow(options=options, args=args)
    form.show()

    sys.exit(app.exec_())