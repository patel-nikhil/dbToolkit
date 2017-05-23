#!/user/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from core import UI


if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = UI()
    sys.exit(app.exec_())
