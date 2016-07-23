#!/usr/bin/python3

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*************************************************************************************(c)2002-2016********

import sys, time
import gettext

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog, QApplication

from argparse import ArgumentParser

import modules
from modules import window1

gettext.install("pydialog", "/usr/share/locale")


def call_parser():
    parser = ArgumentParser()

    parser.add_argument("--title", help=_("Dialog title"), metavar=_("<text>"))
    parser.add_argument("--yesnocancel", help=_("Question message box with yes/no/cancel buttons"))
    parser.add_argument("--yesno", help=_("Question message box with yes/no buttons"))

    parser.add_argument("--yes-label", help=_("The label of the yes-button"), dest="yeslabel", metavar=_("<text>"))
    parser.add_argument("--no-label", help=_("The label of the no-button"), dest="nolabel", metavar=_("<text>"))
    parser.add_argument("--cancel-label", help=_("The label of the cancel-button"), dest="cancellabel", metavar=_("<text>"))
    parser.add_argument("--continue-label", help=_("Use text as Continue button label"), dest="continuelabel", metavar=_("<text>"))
    parser.add_argument("--icon", help=_("Use icon as the application icon."), dest="icon", metavar=_("<path>"))
    parser.add_argument("--progressbar", help=_("Progress bar dialog, returns a D-Bus reference for communication"), nargs="+", metavar=_("<text> [totalsteps]"))
    parser.add_argument("--forkedprogressbar", help=_(""), nargs="+", metavar=_("<text> [totalsteps]"))
    parser.add_argument("--dbusname", help=_(""), nargs="+", metavar=_("<text>"))

    # TODO: icons needed
    parser.add_argument("--sorry", help=_("Sorry message box"), metavar=_("<text>"))
    parser.add_argument("--warningyesno", metavar=_("<text>"), help=_("Warning message box with yes/no buttons"))
    parser.add_argument("--warningyesnocancel", metavar=_("<text>"), help=_("Warning message box with yes/no/cancel buttons"))
    parser.add_argument("--error", metavar=_("<text>"), help=_("'Error' message box"))
    parser.add_argument("--msgbox", metavar=_("<text>"), help=_("Message Box dialog"))

    # TODO: the return value is not compatible with the kdialog
    parser.add_argument("--detailedsorry", help=_("Sorry message box with expendable Details field"), nargs=2, metavar=_("<text> <details>")) 
    parser.add_argument("--warningcontinuecancel", metavar=_("<text>"), help=_("Warning message box with continue/cancel buttons"))
    parser.add_argument("--detailederror", metavar=_("<text> <details>"), help=_("'Error' message box with expandable Details field"), nargs=2)

    # TODO: Untested options below
    parser.add_argument("--slider", metavar=_("<text> [minvalue] [maxvalue] [step]"), help=_("Slider dialog box, returns selected value"), nargs="+")    
    parser.add_argument("--inputbox", metavar=_("<text> <init>"), help=_("Input Box dialog"), nargs='+')
    parser.add_argument("--password", metavar=_("<text>"), help=_("Password dialog"), nargs=1)

    # TODO: Unfinished options below
    parser.add_argument("--combobox", metavar=_("<text> item [item] [item] ..."), help=_("ComboBox dialog"), nargs='+')

    parser.add_argument("--textinputbox", metavar=_("<text> <init> [width] [height]"), help=_("Text Input Box dialog"), nargs='+')
    parser.add_argument("--passivepopup", metavar=_("<text> <timeout>"), help=_("Passive Popup"), nargs='+')

     # TODO: Waiting for GUI

    parser.add_argument("--menu", metavar=_("<text> [tag item] [tag item] ..."), help=_("Menu dialog"), nargs='+')
    parser.add_argument("--checklist", metavar=_("<text> [tag item status] ..."), help=_("Check List dialog"), nargs='+')
    parser.add_argument("--radiolist", metavar=_("<text> [tag item status] ..."), help=_("Radio List dialog"), nargs='+')
    parser.add_argument("--getopenfilename", metavar=_("[startDir] [filter]"), help=_("File dialog to open an existing file"), nargs='*')
    parser.add_argument("--getsavefilename", metavar=_("[startDir] [filter]"), help=_("File dialog to save a file"), nargs='*')
    parser.add_argument("--getexistingdirectory", metavar=_("[startDir]"), help=_("File dialog to select an existing directory"), nargs='*')
    parser.add_argument("--getopenurl", metavar=_("[startDir] [filter]"), help=_("File dialog to open an existing URL"), nargs='*')
    parser.add_argument("--getsaveurl", metavar=_("[startDir] [filter]"), help=_("File dialog to save a URL"), nargs='*')
    parser.add_argument("--geticon", metavar=_("[group] [context]"), help=_("Icon chooser dialog"), nargs='*')
    parser.add_argument("--getcolor", help=_("Color dialog to select a color"))
    parser.add_argument("--default", metavar=_("<text>"), help=_("Default entry to use for combobox, menu and color"), nargs='?')
    parser.add_argument("--multiple", help=_("Allows the --getopenurl and --getopenfilename options to return multiple files"))
    parser.add_argument("--separate-output", help=_("Return list items on separate lines (for checklist option and file open with --multiple)"), dest="separateoutput")
    parser.add_argument("--print-winid", help=_("Outputs the winId of each dialog"), dest="printwinid")
    parser.add_argument("--dontagain", metavar=_("<file:entry>"), help=_("Config file and option name for saving the 'do-not-show/ask-again' state"), nargs='+')
    parser.add_argument("--calendar", metavar=_("<text>"), help=_("Calendar dialog box, returns selected date"), nargs=1)
    parser.add_argument("--attach", metavar=_("<winid>"), help=_("Makes the dialog transient for an X app specified by winid"), nargs=1)
    parser.add_argument("--textbox", metavar=_("<file> [width] [height]"), help=_("Text Box dialog"), nargs='+')


    arguments = parser.parse_args()

    def argument_error(name="", error_type=_("Missing arguments")):
        for argument in arguments.__dict__:
            exec("arguments."+argument+"=None")
        arguments.error = [_("PyDialog - %s: %s") % (error_type, name)]


    unfinished = ["combobox", "textinputbox", "passivepopup", "menu", "checklist", 
        "radiolist", "getopenfilename", "getsavefilename", "getexistingdirectory", "getopenurl",
        "getsaveurl", "geticon", "getcolor", "default", "multiple", "separateoutput", "printwinid",
        "dontagain", "calendar", "attach", "textbox"]
    
    for argument in unfinished:
        if not eval("arguments."+argument) is None:
            argument_error(argument, _("This option is under development"))
            break
    return arguments

app = None

def safety_exit(value):
    """Against the fuckin segfaults"""
    global app
    app.quit()
    sys.exit(value)

arguments = call_parser()


class MainWindow(QDialog, window1.Ui_PyDialog):
    def __init__(self, parent=None):
        global arguments
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.reject_value = 0
        
        self.button_ids = ["details_button", "ok_button", "yes_button", "no_button", "continue_button", "cancel_button"]
        self.button_names = {
            "details_button":_("Details"), 
            "ok_button":_("Ok"), 
            "yes_button":_("Yes"), 
            "no_button":_("No"), 
            "continue_button":_("Continue"),
            "cancel_button":_("Cancel")
        }
        
        self.button_values = {}
        
        self.create_elements()
    

    def create_elements(self):
        self.active_buttons = dict((e, False) for e in self.button_names)
        self.progressbar_cancelled = False

        self.hide_unused_elements()
        self.init_conf()
        self.create_buttons()
        self.set_button_labels()

        
    def hide_unused_elements(self):
        """ Hide the unused elements """
        global arguments
        if not arguments.forkedprogressbar:
            self.progressBar.hide()
        if not arguments.slider:
            self.horizontalSlider.hide()
        if not arguments.combobox:
            self.comboBox.hide()
        if not arguments.inputbox and not arguments.password:
            self.lineEdit.hide()
        if not arguments.combobox and not arguments.password:
            self.label_2.hide()


    def init_conf(self):
        """ Initial configurations (buttons and labels) """
        global arguments
        if arguments.title:
            self.setWindowTitle(arguments.title)
        if arguments.icon:
            from PyQt5.QtGui import QIcon
            icon = QIcon(arguments.icon)
            self.setWindowIcon(icon)

        if arguments.yesno or arguments.warningyesno:
            self.enable_buttons(["yes_button", "no_button"])
            if arguments.yesno:
                self.label.setText(arguments.yesno)
            else:
                self.label.setText(arguments.warningyesno)

        elif arguments.yesnocancel or arguments.warningyesnocancel:
            self.enable_buttons(["yes_button", "no_button", "cancel_button"])
            if arguments.yesnocancel:
                self.label.setText(arguments.yesnocancel)
            else:
                self.label.setText(arguments.warningyesnocancel)

        elif arguments.sorry or arguments.error or arguments.msgbox:
            self.enable_buttons(["ok_button"])
            if arguments.sorry:
                self.label.setText(arguments.sorry)
            elif arguments.error:
                self.label.setText(arguments.error[0])
            else:
                self.label.setText(arguments.msgbox)

        elif arguments.detailedsorry or arguments.detailederror:
            self.enable_buttons(["details_button", "ok_button"])
            if arguments.detailedsorry:
                self.label.setText(arguments.detailedsorry[0])
                self.details = arguments.detailedsorry[1]
            else:
                self.label.setText(arguments.detailederror[0])
                self.details = arguments.detailederror[1]

        elif arguments.warningcontinuecancel:
            self.enable_buttons(["continue_button", "cancel_button"])
            self.label.setText(arguments.warningcontinuecancel)
        
        elif arguments.forkedprogressbar:
            self.label.setText(arguments.forkedprogressbar[0])
            if len(arguments.forkedprogressbar) > 1:
                self.progressBar.setMaximum(int(arguments.forkedprogressbar[1]))
                
        elif arguments.slider:
            self.enable_buttons(["ok_button", "cancel_button"])
            self.label.setText(arguments.slider[0])
            if len(arguments.slider) > 1:
                self.horizontalSlider.setMinimum(int(arguments.slider[1]))
            if len(arguments.slider) > 2:
                self.horizontalSlider.setMaximum(int(arguments.slider[2]))
            if len(arguments.slider) > 3:
                self.horizontalSlider.setSingleStep(int(arguments.slider[3]))
                self.horizontalSlider.setPageStep(int(arguments.slider[3]))
        
        elif arguments.inputbox:
            self.enable_buttons(["ok_button", "cancel_button"])
            self.label.setText(arguments.inputbox[0])
            if len(arguments.inputbox) > 1:
                self.lineEdit.setText(arguments.inputbox[1])

        elif arguments.password:
            self.enable_buttons(["ok_button", "cancel_button"])
            self.lineEdit.setEchoMode(2)
            self.label.setText(arguments.password[0])
            self.label_2.setText(_("Password:"))


    def set_button_labels(self):
        """Set the button labels"""
        global arguments
        if arguments.yeslabel and self.active_buttons["yes_button"]:
            self.buttons["yes_button"].setText(arguments.yeslabel)
        if arguments.nolabel and self.active_buttons["no_button"]:
            self.buttons["no_button"].setText(arguments.nolabel)
        if arguments.cancellabel and self.active_buttons["cancel_button"]:
            self.buttons["cancel_button"].setText(arguments.cancellabel)
        if arguments.continuelabel and self.active_buttons["continue_button"]:
            self.buttons["continue_button"].setText(arguments.continuelabel)

    def create_buttons(self):
        global arguments
        self.buttons = {}
        
        noab = len(list(filter(lambda x: self.active_buttons[x], self.active_buttons)))
        self.reject_value = noab - 1

        i = 0
        for button_id in self.button_ids:
            if self.active_buttons[button_id]:
                self.buttons[button_id] = QPushButton(self.button_names[button_id])
                self.horizontalLayout.addWidget(self.buttons[button_id])
                if button_id == "details_button":
                    self.buttons["details_button"].clicked.connect(self.details_button_clicked)
                elif button_id == "cancel_button":
                    self.buttons[button_id].clicked.connect(self.reject)
                else:
                    self.button_values[button_id] = i
                    exec("self.buttons[button_id].clicked.connect(self."+button_id+"_clicked)")
                    i += 1
    
    def ok_button_clicked(self):
        if arguments.slider:
            print(self.horizontalSlider.value())
        elif arguments.inputbox or arguments.password:
            print(self.lineEdit.text())
        safety_exit(self.button_values["ok_button"])
    
    def yes_button_clicked(self):
        safety_exit(self.button_values["yes_button"])
    
    def no_button_clicked(self):
        safety_exit(self.button_values["no_button"])
    
    def continue_button_clicked(self):
        safety_exit(self.button_values["continue_button"])
    
    def reject(self):
        safety_exit(self.reject_value)

    def enable_buttons (self, button_list):
        for button in button_list:
            self.active_buttons[button] = True
            
    def details_button_clicked (self):
        self.label.setText(self.label.text() + '\n\n' + self.details)
        self.buttons["details_button"].setDisabled(True)

    def progressbar_cancel_clicked(self):
        self.progressbar_cancelled = True

    def showCancelButton(self):
        if not "cancel_button" in self.buttons:
            self.buttons["cancel_button"] = QPushButton(self.button_names["cancel_button"])
            self.buttons["cancel_button"].clicked.connect(self.progressbar_cancel_clicked)
            self.horizontalLayout.addWidget(self.buttons["cancel_button"])
            self.progressbar_cancelled = False
        self.buttons["cancel_button"].show()
        
#    def resizeEvent(self, event):
#        limit = 100
#        if event.size().width() > limit and event.oldSize().width() < limit:
#            self.label.setWordWrap(True)
#        elif event.size().width() < limit and event.oldSize().width() > limit:
#            self.label.setWordWrap(False)
        

    
if __name__ == '__main__' and not (arguments.progressbar or arguments.forkedprogressbar):
    app = QApplication(sys.argv) # NOTE: Be careful, the QApplication can remove elements from the sys.argv! Call the parse_args before it if you want to use them.

    form = MainWindow()
    form.show()
    app.exec_()


if arguments.forkedprogressbar:
    from PyQt5.QtCore import pyqtSlot, pyqtProperty, Q_CLASSINFO, QObject
    from PyQt5.QtDBus import (QDBusAbstractAdaptor, QDBusConnection)

    class Server(QObject):
        def __init__(self, ui):
            QObject.__init__(self)
            self.__dbusAdaptor = ServerAdaptor(self)
            self.autoclose = False
            self.ui = ui

        def close(self):
            self.ui.close()

        @property
        def maximum(self):
            return self.ui.progressBar.maximum()

        @maximum.setter
        def maximum(self, v):
            self.ui.progressBar.setMaximum(v)

        @property
        def value(self):
            return self.ui.progressBar.value()

        @value.setter
        def value(self, v):
            self.ui.progressBar.setValue(v)
            if self.autoclose and v == self.ui.progressBar.maximum():
                self.ui.close()

        @property
        def autoClose(self):
            return self.autoclose

        @autoClose.setter
        def autoClose(self, v):
            self.autoclose = v

        def wasCancelled(self):
            return self.ui.progressbar_cancelled

        def showCancelButton(self, v):
            if v:
                self.ui.showCancelButton()
            else:
                self.ui.buttons["cancel_button"].hide()

        def ignoreCancel(self, v):
            self.ui.buttons["cancel_button"].setDisabled(v)        
        
        def setLabelText(self, v):
            self.ui.label.setText(v)


    class ServerAdaptor(QDBusAbstractAdaptor):
        Q_CLASSINFO("D-Bus Interface", "org.kde.kdialog.ProgressDialog")
        Q_CLASSINFO("D-Bus Introspection",
        '<interface name="org.kde.kdialog.ProgressDialog">\n'
        '    <property name="maximum" type="i" access="readwrite"/>'
        '    <property name="value" type="i" access="readwrite"/>'
        '    <property name="autoClose" type="b" access="readwrite"/>'
        '    <method name="setLabelText">'
        '      <arg type="s" name="label" direction="in"/>'
        '    </method>'
        '    <method name="ignoreCancel">'
        '      <arg name="value" type="b" direction="in"/>'
        '    </method>'
        '    <method name="showCancelButton">'
        '      <arg name="value" type="b" direction="in"/>'
        '    </method>'
        '    <method name="wasCancelled">'
        '      <arg type="b" direction="out"/>'
        '    </method>'
        '    <method name="close"/>'
        '</interface>\n')

        def __init__(self, parent):
            super().__init__(parent)

        @pyqtSlot()
        def close(self):
            self.parent().close()

        @pyqtProperty(int)
        def maximum(self):
            return self.parent().maximum

        @maximum.setter
        def maximum(self, v):
            self.parent().maximum = v

        @pyqtProperty(int)
        def value(self):
            return self.parent().value

        @value.setter
        def value(self, v):
            self.parent().value = v

        @pyqtProperty(bool)
        def autoClose(self):
            return self.parent().autoClose

        @autoClose.setter
        def autoClose(self, v):
            self.parent().autoClose = v

        @pyqtSlot(result=bool)
        def wasCancelled(self):
            return self.parent().wasCancelled()

        @pyqtSlot(bool)
        def showCancelButton(self, v):
            self.parent().showCancelButton(v)

        @pyqtSlot(bool)
        def ignoreCancel(self, v):
            self.parent().ignoreCancel(v)

        @pyqtSlot(str)
        def setLabelText(self, v):
            self.parent().setLabelText(v)


if __name__ == '__main__' and arguments.forkedprogressbar:
    app = QApplication(sys.argv) # NOTE: Be careful, the QApplication can remove elements from the sys.argv! Call the parse_args before it if you want to use them.

    form = MainWindow()
    form.show()

    if arguments.forkedprogressbar:
        bus = QDBusConnection.sessionBus()
        server = Server(form)
        bus.registerObject('/ProgressDialog', server)
        bus.registerService(arguments.dbusname[0])
    app.exec_()


if __name__ == '__main__' and arguments.progressbar:
    import subprocess, dbus, os
    progname = "pydialog"
    dbusname = "org.kde.kdialog"
    dbusname += "-" + str(os.getpid())
    print (dbusname + " /ProgressDialog")
    args = sys.argv[:]
    o = "--progressbar"
    i = args.index(o)
    args[i] = "--forked" + args[i][2:]
    args.append("--dbusname")
    args.append(dbusname)
    subprocess.Popen(args, stdout=sys.stderr)
    bus = dbus.Bus()
    for j in range(20):
        try:
            o = bus.get_object(dbusname, "/ProgressDialog")
            break
        except:
            pass
        time.sleep(0.1)
    sys.exit(0)
