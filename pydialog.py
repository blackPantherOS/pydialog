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
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication

from optparse import OptionParser


import modules

from modules import window1


gettext.install("pydialog", "/usr/share/locale")


class ReturnClass():
    def __init__(self, value):
        self.value = value
    def __call__(self):
        sys.exit(self.value)


class MainWindow(QDialog, window1.Ui_PyDialog):
    def __init__(self, parent=None, options=None, args=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.nullarg = False

        if options.title:
            self.setWindowTitle(options.title)
        if options.icon:
            self.setWindowIcon(options.icon)


        self.button_ids = ["details_button", "ok_button", "yes_button", "no_button", "cancel_button"]
        self.button_names = {
            "details_button":_("Details"), 
            "ok_button":_("Ok"), 
            "yes_button":_("Yes"), 
            "no_button":_("No"), 
            "cancel_button":_("Cancel")
        }
        self.active_buttons = dict((e, True) for e in self.button_names)

        if options.yn:
            self.disable_buttons(["details_button", "cancel_button", "ok_button"])
        elif options.ync:
            self.disable_buttons(["details_button", "ok_button"])
        elif options.sorry:
            self.disable_buttons(["details_button", "cancel_button", "yes_button", "no_button"])
            self.nullarg = True
        elif options.dsorry:
            self.disable_buttons(["details_button", "cancel_button", "yes_button", "no_button"])
            self.nullarg = True

        if not self.nullarg:
            if len(args) == 0:
                sys.exit(_("There is no argument!"))
            self.groupBox.setTitle(args[0])

        self.create_buttons()

        if options.yeslabel and self.active_buttons["yes_button"]:
            self.buttons["yes_button"].setText(options.yeslabel)
        if options.nolabel and self.active_buttons["no_button"]:
            self.buttons["no_button"].setText(options.nolabel)
        if options.cancellabel and self.active_buttons["cancel_button"]:
            self.buttons["cancel_button"].setText(options.cancellabel)



    def create_buttons(self):
        self.buttons = {}
        
        noab = len(list(filter(lambda x: self.active_buttons[x], self.active_buttons)))
        i = 0
        for button_id in self.button_ids:
            if self.active_buttons[button_id]:
                self.buttons[button_id] = QPushButton(self.button_names[button_id])
                self.gridLayout.addWidget(self.buttons[button_id])
                if i < noab-1:
                    objname = button_id[:-7]
                    self.__dict__[objname] = ReturnClass(i)
                    self.buttons[button_id].clicked.connect(self.__dict__[objname])
                else:
                    self.reject = ReturnClass(i)
                    self.buttons[button_id].clicked.connect(self.reject)
                i += 1


    def disable_buttons(self, button_list):
        for button in button_list:
            self.active_buttons[button] = False
       


def call_parser():
    usage = _("usage: %prog [options] [arg]")
    parser = OptionParser(usage=usage)

    parser.add_option("--title", help=_("Dialog title"), dest="title", metavar=_("<text>"))
    parser.add_option("--icon", help=_("Use icon as the application icon."), dest="icon", metavar=_("<path>"))

    parser.add_option("--yesnocancel", help=_("Question message box with yes/no/cancel buttons"), dest="ync", action="store_true", default=False)
    parser.add_option("--yesno", help=_("Question message box with yes/no buttons"), dest="yn", action="store_true", default=False)

    parser.add_option("--sorry", help=_("Sorry message box"), dest="sorry", metavar=_("<text>"))
    parser.add_option("--detailedsorry", help=_("Sorry message box with expendable Details field"), dest="dsorry", nargs=2, metavar=_("<text> <details>"))
#    TODO: progressbar
  
    parser.add_option("--yes-label", help=_("The label of the yes-button"), dest="yeslabel", metavar=_("<text>"))
    parser.add_option("--no-label", help=_("The label of the no-button"), dest="nolabel", metavar=_("<text>"))
    parser.add_option("--cancel-label", help=_("The label of the cancel-button"), dest="cancellabel", metavar=_("<text>"))

    return parser.parse_args()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    (options, args) = call_parser()
    
    form = MainWindow(options=options, args=args)
    form.show()

    app.exec_()
