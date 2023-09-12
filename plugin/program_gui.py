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

import argparse
import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication as Application, QWidget as Widget, QPushButton as Button
from PyQt5.QtWidgets import QLabel as Label, QGridLayout, QDesktopWidget

import print_string_colors as COLOUR


class ProgramGUI(Widget):

    def __init__(self):
        super().__init__()
        # GUI window specific values
        self.title = 'Crispy Octo Pancake'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        # Other object specific values
        self.label_str = "This is a demo string"
        self.plot_status = u'a'
        self.X_plot_val = None
        self.Y_plot_val = None
        self.Z_plot_val = None

        # Call argument parsing to enable/disable debug options
        dbg_parse = argparse.ArgumentParser()
        dbg_parse.add_argument(u'-d',
                               u'--debug',
                               action='store_true',
                               help=u'Enable DEBUG specific functions')
        self.argh = dbg_parse.parse_args()

        # Debug output
        if self.argh.debug is True:
            print(COLOUR.STRONG_BLUE +
                  "====================\n" +
                  "==== DEBUG MODE ====\n" +
                  "====================" +
                  COLOUR.NORMAL)

        # initialize UI
        self.init_ui()

    def init_ui(self):
        #
        # Setup Window Title and geometry
        #
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #
        # Setup User message
        #
        self.label = Label(self.label_str)
        #
        # Setup "Program" button
        #
        self.test_graph_button = Button(u'Update button', self)
        self.test_graph_button.setToolTip(u'Call update function to do stuff')
        self.test_graph_button.clicked.connect(self.test_std_out)
        #
        # Setup grid layout for global window
        #
        main_layout = QGridLayout()  # Layout for Main Tab Widget
        main_layout.setRowMinimumHeight(0, 5)  # setting layout parameters
        main_layout.setRowMinimumHeight(2, 10)
        main_layout.setRowMinimumHeight(4, 5)
        main_layout.addWidget(self.label, 1, 1, Qt.AlignHCenter)
        main_layout.addWidget(self.test_graph_button, 2, 1)
        self.setLayout(main_layout)  # sets Main layout
        #
        # Special setup when '--debug' is passed as an argument
        #
        if self.argh.debug is True:
            # tell user that all debug Widgets are set up
            print(COLOUR.YELLOW +
                  "Debug Wigets & objects setup done" +
                  COLOUR.NORMAL)

    @pyqtSlot()
    def test_std_out(self):
        # Used for rapid GUI testing
        return None


if __name__ == '__main__':
    app = Application(sys.argv)
    gui = ProgramGUI()

    qr = gui.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    gui.move(qr.topLeft())
    app.processEvents()

    gui.show()

    exit_val = app.exec_()

    # behaviour to trigger on exit
    sys.exit(exit_val)
