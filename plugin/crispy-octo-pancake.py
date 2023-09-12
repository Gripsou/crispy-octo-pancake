"""
===================
Crispy Octo Pancake
===================

Brief:
------
_KiCad_ plugin which allow user to choose which field to copy in BoM with the
help of a GUI.

Important
---------
    This project is published under **GNU LGPLv3 License*
"""

import pcbnew
import os

import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication as Application, QWidget as Widget, QPushButton as Button
from PyQt5.QtWidgets import QLabel as Label, QGridLayout, QDesktopWidget

import program_gui


class CrispyOctoPancake(pcbnew.ActionPlugin):
    def __init__(self):
        self.icon_file_name = None
        self.show_toolbar_button = None
        self.description = None
        self.category = None
        self.name = None

    def defaults(self):
        self.name = "Crispy Octo Pancake"
        self.category = "Something like _A descriptive category name_"
        self.description = "KiCad plugin which allow user to choose which field to copy in BoM with the help of a GUI"
        self.show_toolbar_button = False  # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'ressources/Pancatake.png')  # Optional, defaults to ""

    def Run(self):
        # The entry function of the plugin that is executed on user action
        app = Application(sys.argv)
        gui = program_gui.ProgramGUI()

        qr = gui.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        gui.move(qr.topLeft())
        app.processEvents()

        gui.show()

        exit_val = app.exec_()

        # behaviour to trigger on exit
        sys.exit(exit_val)


CrispyOctoPancake().register()  # Instantiate and register to Pcbnew
