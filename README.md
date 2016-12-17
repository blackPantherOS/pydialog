Description: 
------------

My problem was that the kdialog code is still not ported to Qt5 and it depends on various Qt4/KDE4 components. 
The kdialog has big dependency sizes so we made an alternate dialogs like kdialog switches, options. 
We would still like full compatibility with kdialog but a few options are still not finished and although this release provides many important functions.

Patches, Extensions, any ideas are welcome!

Working dialogs/options: 
--title <text> Dialog title
--yesnocancel YESNOCANCEL Question message box with yes/no/cancel buttons
--yesno YESNO Question message box with yes/no buttons
--yes-label <text> The label of the yes-button
--no-label <text> The label of the no-button
--cancel-label <text> The label of the cancel-button
--continue-label <text> Use text as Continue button label
--icon <path> Use icon as the application icon.
--progressbar <text> [totalsteps] [<text> [totalsteps] ...] Progress bar dialog, returns a D-Bus reference for
communication
--forkedprogressbar <text> [totalsteps] [<text> [totalsteps] ...]
--dbusname <text> [<text> ...]
--inputbox <text> <init> [<text> <init> ...] Input Box dialog
--password <text> Password dialog
--checklist <text> [tag item status] ... [<text> [tag item status] ... ...] Check List dialog
--sorry <text> Sorry message box
--warningyesno <text> Warning message box with yes/no buttons
--warningyesnocancel <text> Warning message box with yes/no/cancel buttons
--error <text> 'Error' message box
--msgbox <text> Message Box dialog
--detailedsorry <text> <details> <text> <details> Sorry message box with expendable Details field
--warningcontinuecancel <text> Warning message box with continue/cancel buttons
--detailederror <text> <details> <text> <details>
'Error' message box with expandable Details field
--slider <text> [minvalue] [maxvalue] [step] [<text> [minvalue] [maxvalue] [step] ...]

Plans:
-----------
- Dialogs still in focus (optional/default)
- License dialog intagration
- Full compatible for replace /or with --kdialog option/ with kdialog

Screenshot
-----------
![pydialog](https://raw.githubusercontent.com/blackPantherOS/playground/master/pydialog/screenshot.png)

