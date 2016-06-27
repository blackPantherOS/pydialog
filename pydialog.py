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
import time

from PyQt5.QtCore import Qt, QMetaObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication, QDialogButtonBox

from optparse import OptionParser


import modules

from modules import window1


gettext.install("pydialog", "/usr/share/locale")


class MainWindow(QDialog, window1.Ui_Dialog):
    def __init__(self, parent=None, options=None, args=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_positions = ["yes_button", "no_button", "cancel_button"]

        self.active_buttons = dict((e, True) for e in self.button_positions)
        if options.yn:
            self.active_buttons["cancel_button"] = False

        self.buttons = {}
        self.detect_buttons()
        
        if options.title:
            self.setWindowTitle(options.title)
        if options.icon:
            self.setWindowIcon(options.icon)

#        self.buttons["yes_button"] = self.buttonBox.addButton(QDialogButtonBox.Yes)
#        self.buttons["no_button"] = self.buttonBox.addButton(QDialogButtonBox.No)
#        if options.ync:
#            self.buttons["cancel_button"] = self.buttonBox.addButton(QDialogButtonBox.Cancel)
#            self.buttons["cancel_button"].clicked.connect(self.reject)

        self.buttons["yes_button"].clicked.connect(self.yes)
        self.buttons["no_button"].clicked.connect(self.no)

        QMetaObject.connectSlotsByName(self)

        if options.yeslabel:
            self.buttons["yes_button"].setText(options.yeslabel)
        if options.nolabel:
            self.buttons["no_button"].setText(options.nolabel)
        if options.cancellabel:
            self.buttons["cancel_button"].setText(options.cancellabel)
            
        self.message.setText(args[0])

        
    def yes(self):
        print ("yes")
        sys.exit(0)

    def no(self):
        print ("no")
        sys.exit(1)
        
    def reject(self):
        print ("cancel")
        sys.exit(2)
        
    def detect_buttons(self):
        buttons = self.buttonBox.buttons()
        if self.active_buttons["cancel_button"]:
            buttons.append(buttons.pop(0))
        pos = 0
        for button_name in self.button_positions:
            if self.active_buttons[button_name]:
                self.buttons[button_name] = buttons[pos]
                pos += 1
            else:
                print("delete:", button_name)
        


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
