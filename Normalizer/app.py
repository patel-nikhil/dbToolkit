#!/user/bin/python3

import sys

from PyQt5.QtWidgets import QApplication

from view.gui import UI



if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = UI()
    sys.exit(app.exec_())
