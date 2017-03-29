import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

_translate = QtCore.QCoreApplication.translate
app = QApplication(sys.argv)


class IO_Test(unittest.TestCase):
    '''This class contains the methods for testing input/output operations'''

    def setUp(self):
        '''Instantiate the gui'''
        self.gui = core.UI()


    def test_open_save_file(self):
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        
        QTest.qWaitForWindowActive(self.gui)
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget()))
        QTest.keyPress(self.gui, Qt.Key_O, Qt.ControlModifier)
        QTest.keyRelease(self.gui, Qt.Key_O, Qt.ControlModifier)



def inject(window):
    window.text = lambda: "sample.fdcover"
    window.close()





if __name__ == "__main__":
    _projname = "mincover"
    parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    srcdir = os.path.join(parent, _projname)
    sys.path.append(srcdir)

    import core
    unittest.main()
