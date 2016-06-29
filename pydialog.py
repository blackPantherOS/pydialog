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

from argparse import ArgumentParser


import modules

from modules import window1


gettext.install("pydialog", "/usr/share/locale")


class ReturnClass():
    def __init__(self, value):
        self.value = value
    def __call__(self):
        sys.exit(self.value)


class MainWindow(QDialog, window1.Ui_PyDialog):
    def __init__(self, parent=None, arguments=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.nullarg = False

        if arguments.title:
            self.setWindowTitle(arguments.title)
        if arguments.icon:
            self.setWindowIcon(arguments.icon)


        self.button_ids = ["details_button", "ok_button", "yes_button", "no_button", "cancel_button"]
        self.button_names = {
            "details_button":_("Details"), 
            "ok_button":_("Ok"), 
            "yes_button":_("Yes"), 
            "no_button":_("No"), 
            "cancel_button":_("Cancel")
        }
        self.active_buttons = dict((e, True) for e in self.button_names)

        if arguments.yn:
            self.disable_buttons(["details_button", "cancel_button", "ok_button"])
        elif arguments.ync:
            self.disable_buttons(["details_button", "ok_button"])
        elif arguments.sorry:
            self.disable_buttons(["details_button", "cancel_button", "yes_button", "no_button"])
            self.nullarg = True
            self.groupBox.setTitle(arguments.sorry)
        elif arguments.dsorry:
            self.disable_buttons(["cancel_button", "yes_button", "no_button"])
            self.nullarg = True
            self.groupBox.setTitle(arguments.dsorry[0])

        if not self.nullarg:
            if len(args) == 0:
                sys.exit(_("There is no argument!"))
            self.groupBox.setTitle(args[0])

        self.create_buttons()

        if arguments.yeslabel and self.active_buttons["yes_button"]:
            self.buttons["yes_button"].setText(arguments.yeslabel)
        if arguments.nolabel and self.active_buttons["no_button"]:
            self.buttons["no_button"].setText(arguments.nolabel)
        if arguments.cancellabel and self.active_buttons["cancel_button"]:
            self.buttons["cancel_button"].setText(arguments.cancellabel)



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
    parser = ArgumentParser(usage=usage)

    parser.add_argument("--title", help=_("Dialog title"), dest="title", metavar=_("<text>"))
    parser.add_argument("--icon", help=_("Use icon as the application icon."), dest="icon", metavar=_("<path>"))

    parser.add_argument("--yesnocancel", help=_("Question message box with yes/no/cancel buttons"), dest="ync", action="store_true", default=False)
    parser.add_argument("--yesno", help=_("Question message box with yes/no buttons"), dest="yn", action="store_true", default=False)

    parser.add_argument("--sorry", help=_("Sorry message box"), dest="sorry", metavar=_("<text>"))
    parser.add_argument("--detailedsorry", help=_("Sorry message box with expendable Details field"), dest="dsorry", nargs=2, metavar=_("<text> <details>"))
    parser.add_argument("--progressbar", help=_("Progress bar dialog, returns a D-Bus reference for communication"), dest="progressbar", nargs=2, metavar=_("<text> [totalsteps]"))

    parser.add_argument("--yes-label", help=_("The label of the yes-button"), dest="yeslabel", metavar=_("<text>"))
    parser.add_argument("--no-label", help=_("The label of the no-button"), dest="nolabel", metavar=_("<text>"))
    parser.add_argument("--cancel-label", help=_("The label of the cancel-button"), dest="cancellabel", metavar=_("<text>"))

    parser.add_argument("--warningyesno", metavar=_("<text>"), help=_("Warning message box with yes/no buttons"))
    parser.add_argument("--warningcontinuecancel", metavar=_("<text>"), help=_("Warning message box with continue/cancel buttons"))
    parser.add_argument("--warningyesnocancel", metavar=_("<text>"), help=_("Warning message box with yes/no/cancel buttons"))
    parser.add_argument("--continue-label", metavar=_("<text>"), help=_("Use text as Continue button label"))
    parser.add_argument("--error", metavar=_("<text>"), help=_("'Error' message box"))
    parser.add_argument("--detailederror", metavar=_("<text> <details>"), help=_("'Error' message box with expandable Details field"), nargs=2)
    parser.add_argument("--msgbox", metavar=_("<text>"), help=_("Message Box dialog"))
    parser.add_argument("--inputbox", metavar=_("<text> <init>"), help=_("Input Box dialog"), nargs=2)
    parser.add_argument("--password", metavar=_("<text>"), help=_("Password dialog"))
#    parser.add_argument("--textbox", metavar=_("<file> [width] [height]"), help=_("Text Box dialog"), nargs='1+')
#    parser.add_argument("--textinputbox", metavar=_("<text> <init> [width] [height]"), help=_("Text Input Box dialog"), nargs='2+')
#    parser.add_argument("--combobox", metavar=_("<text> item [item] [item] ..."), help=_("ComboBox dialog"))
#    parser.add_argument("--menu", metavar=_("<text> [tag item] [tag item] ..."), help=_("Menu dialog"))
#    parser.add_argument("--checklist", metavar=_("<text> [tag item status] ..."), help=_("Check List dialog"))
#    parser.add_argument("--radiolist", metavar=_("<text> [tag item status] ..."), help=_("Radio List dialog"))
    parser.add_argument("--passivepopup", metavar=_("<text> <timeout>"), help=_("Passive Popup"))
#    parser.add_argument("--getopenfilename", metavar=_("[startDir] [filter]"), help=_("File dialog to open an existing file"))
#    parser.add_argument("--getsavefilename", metavar=_("[startDir] [filter]"), help=_("File dialog to save a file"))
#    parser.add_argument("--getexistingdirectory", metavar=_("[startDir]"), help=_("File dialog to select an existing directory"))
#    parser.add_argument("--getopenurl", metavar=_("[startDir] [filter]"), help=_("File dialog to open an existing URL"))
#    parser.add_argument("--getsaveurl", metavar=_("[startDir] [filter]"), help=_("File dialog to save a URL"))
#    parser.add_argument("--geticon", metavar=_("[group] [context]"), help=_("Icon chooser dialog"))
    parser.add_argument("--getcolor", help=_("Color dialog to select a color"))
    parser.add_argument("--default", metavar=_("<text>"), help=_("Default entry to use for combobox, menu and color"))
    parser.add_argument("--multiple", help=_("Allows the --getopenurl and --getopenfilename options to return multiple files"))
    parser.add_argument("--separate-output", help=_("Return list items on separate lines (for checklist option and file open with --multiple)"))
    parser.add_argument("--print-winid", help=_("Outputs the winId of each dialog"))
    parser.add_argument("--dontagain", metavar=_("<file:entry>"), help=_("Config file and option name for saving the 'do-not-show/ask-again' state"))
#    parser.add_argument("--slider", metavar=_("<text> [minvalue] [maxvalue] [step]"), help=_("Slider dialog box, returns selected value"))
    parser.add_argument("--calendar", metavar=_("<text>"), help=_("Calendar dialog box, returns selected date"))
    parser.add_argument("--attach", metavar=_("<winid>"), help=_("Makes the dialog transient for an X app specified by winid"))

    return parser.parse_args()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    arguments = call_parser()
    
    form = MainWindow(arguments=arguments)
    form.show()

    app.exec_()
