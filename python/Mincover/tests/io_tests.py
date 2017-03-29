import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

_translate = QtCore.QCoreApplication.translate
app = QApplication(sys.argv)


class OpenFileTest(unittest.TestCase):
    '''This class contains the methods for testing input/output operations'''

    def setUp(self):
        '''Instantiate the gui'''
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        
        self.gui = core.UI()


    def test_open_save_file(self):        
        self.assertTrue(self.open_no_file())
        self.assertTrue(self.open_no_file())
        self.assertTrue(self.open_bad_file())
        self.assertTrue(self.open_bad_fds())
        self.assertTrue(self.open_bad_cover())
        self.assertTrue(self.open_false_cover())
        self.assertTrue(self.open_good_file())

    def set_file(self, fileName):
        QTest.qWaitForWindowActive(self.gui)
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QTest.keyPress(self.gui, Qt.Key_O, Qt.ControlModifier)
        QTest.keyRelease(self.gui, Qt.Key_O, Qt.ControlModifier)


    def open_no_file(self):
        # write data to test file
        self.set_file(None)
        if core._attributes != []:
            return False
        elif core._fds != []:
            return False
        elif core._cover != []:
            return False
        return True


    def open_not_file(self):
        # write data to test file
        self.set_file("notafile")
        if core._attributes != []:
            return False
        if core._fds != []:
            return False
        if core._cover != []:
            return False
        return True

    def open_bad_file(self):
        # write data to test file
        self.set_file("test.txt")
        if core._attributes != []:
            return False
        if core._fds != []:
            return False
        if core._cover != []:
            return False
        return True

    def open_bad_fds(self):
        # write data to test file
        self.set_file("badfd.fdcover")
        if core._attributes != []:
            return False
        if core._fds != []:
            return False
        if core._cover != []:
            return False
        return True

    def open_bad_cover(self):
        # write data to test file
        self.set_file("badcover.fdcover")
        if core._attributes != []:
            return False
        if core._fds != []:
            return False
        if core._cover != []:
            return False
        return True

    def open_false_cover(self):
        # write data to test file
        self.set_file("false.fdcover")
        if core._attributes != []:
            return False
        if core._fds != []:
            return False
        if core._cover != []:
            return False
        return True

    def open_good_file(self):
        # write data to test file
        self.set_file("sample.fdcover")
        if core._attributes != ['a', 'b', 'c']:
            return False
        if core._fds != ['a-b', 'b-c', 'a-c']:
            return False
        if core._cover != ['a-b','b-c']:
            return False
        return True


    def tearDown(self):
        core._attributes = []
        core._fds = []
        core._cover = []







def inject(window, fileName):
    window.text = lambda: fileName
    window.close()



if __name__ == "__main__":
    _projname = "mincover"
    parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    srcdir = os.path.join(parent, _projname)
    sys.path.append(srcdir)

    import core
    unittest.main()
