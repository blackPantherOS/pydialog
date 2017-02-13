#!/usr/bin/env python3

import unittest, subprocess

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
        
    def check_values(self, args):
        values = []
        for cmd in ["./pydialog.py", "kdialog"]:
            value = subprocess.run([cmd]+args)
            values.append(value)
        self.assertEqual(values[0].returncode, values[1].returncode)
        self.assertEqual(values[0].stdout, values[1].stdout)


    def test_01_msgbox_return(self):
        self.check_values(['--msgbox','Please press the ok button!'])
        
    def test_02_yesno_return(self):
        self.check_values(['--yesno', 'Please press the YES button!'])
        self.check_values(['--yesno', 'Please press the NO button!'])
        
    def test_03_yesnocancel_return(self):
        self.check_values(['--yesnocancel', 'Please press the YES button!'])
        self.check_values(['--yesnocancel', 'Please press the NO button!'])
        self.check_values(['--yesnocancel', 'Please press the CANCEL button!'])

    def test_04_sorry_return(self):
        self.check_values(['--sorry','Sorry, press the ok button!'])
        
    def test_05_error_return(self):
        self.check_values(['--error','Error: press the ok button!'])
        
    def test_06_warningyesno_return(self):
        self.check_values(['--warningyesno', 'Please press the YES button!'])
        self.check_values(['--warningyesno', 'Please press the NO button!'])
        
    def test_07_warningyesnocancel_return(self):
        self.check_values(['--warningyesnocancel', 'Please press the YES button!'])
        self.check_values(['--warningyesnocancel', 'Please press the NO button!'])
        self.check_values(['--warningyesnocancel', 'Please press the CANCEL button!'])

    def test_08_warningcontinuecancel_return(self):
        self.check_values(['--warningcontinuecancel', 'Please press the CONTINUE button!'])
        self.check_values(['--warningcontinuecancel', 'Please press the CANCEL button!'])

    def test_09_detailedsorry_return(self):
        self.check_values(['--detailedsorry','Sorry, press the ok button!', 'These lines are the details. Please press OK'])

    def test_10_detailedsorry_return(self):
        self.check_values(['--detailederror','Error press the ok button!', 'These lines are the details. Please press OK'])


if __name__ == '__main__':
    unittest.main()


"""
    parser.add_argument("--error", metavar=_("<text>"), help=_("'Error' message box"))
    parser.add_argument("--sorry", help=_("Sorry message box"), metavar=_("<text>"))
    parser.add_argument("--yesnocancel", help=_("Question message box with yes/no/cancel buttons"))
    parser.add_argument("--yesno", help=_("Question message box with yes/no buttons"))
    parser.add_argument("--msgbox", metavar=_("<text>"), help=_("Message Box dialog"))
    parser.add_argument("--warningyesno", metavar=_("<text>"), help=_("Warning message box with yes/no buttons"))
    parser.add_argument("--warningyesnocancel", metavar=_("<text>"), help=_("Warning message box with yes/no/cancel buttons"))
    parser.add_argument("--warningcontinuecancel", metavar=_("<text>"), help=_("Warning message box with continue/cancel buttons"))

    parser.add_argument("--detailedsorry", help=_("Sorry message box with expendable Details field"), nargs=2, metavar=_("<text> <details>")) 
    parser.add_argument("--detailederror", metavar=_("<text> <details>"), help=_("'Error' message box with expandable Details field"), nargs=2)

    parser.add_argument("--title", help=_("Dialog title"), metavar=_("<text>"))

    parser.add_argument("--yes-label", help=_("The label of the yes-button"), dest="yeslabel", metavar=_("<text>"))
    parser.add_argument("--no-label", help=_("The label of the no-button"), dest="nolabel", metavar=_("<text>"))
    parser.add_argument("--cancel-label", help=_("The label of the cancel-button"), dest="cancellabel", metavar=_("<text>"))
    parser.add_argument("--continue-label", help=_("Use text as Continue button label"), dest="continuelabel", metavar=_("<text>"))

    parser.add_argument("--icon", help=_("Use icon as the application icon."), dest="icon", metavar=_("<path>"))
    parser.add_argument("--progressbar", help=_("Progress bar dialog, returns a D-Bus reference for communication"), nargs="+", metavar=_("<text> [totalsteps]"))
    parser.add_argument("--forkedprogressbar", help=_(""), nargs="+", metavar=_("<text> [totalsteps]"))
    parser.add_argument("--dbusname", help=_(""), nargs="+", metavar=_("<text>"))
    parser.add_argument("--inputbox", metavar=_("<text> <init>"), help=_("Input Box dialog"), nargs='+')
    parser.add_argument("--password", metavar=_("<text>"), help=_("Password dialog"), nargs=1)
    parser.add_argument("--checklist", metavar=_("<text> [tag item status] ..."), help=_("Check List dialog"), nargs='+')
    parser.add_argument("--radiolist", metavar=_("<text> [tag item status] ..."), help=_("Radio List dialog"), nargs='+')
    parser.add_argument("--menu", metavar=_("<text> [tag item] [tag item] ..."), help=_("Menu dialog"), nargs='+')

    # TODO: icons needed

    # TODO: Untested options below
    parser.add_argument("--slider", metavar=_("<text> [minvalue] [maxvalue] [step]"), help=_("Slider dialog box, returns selected value"), nargs="+")    

    # TODO: Unfinished options below
    parser.add_argument("--combobox", metavar=_("<text> item [item] [item] ..."), help=_("ComboBox dialog"), nargs='+')

    parser.add_argument("--textinputbox", metavar=_("<text> <init> [width] [height]"), help=_("Text Input Box dialog"), nargs='+')
    parser.add_argument("--passivepopup", metavar=_("<text> <timeout>"), help=_("Passive Popup"), nargs='+')

     # TODO: Waiting for GUI

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

    parser.add_argument("--stayontop", help=_("The window stays on top"), action='store_true')

    parser.add_argument("--antisegfault", action='store_true')

"""
