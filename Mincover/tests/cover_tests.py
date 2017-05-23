import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

_translate = QtCore.QCoreApplication.translate
app = QApplication(sys.argv)



class CoverEqualityTests(unittest.TestCase):
    """This class contains methods to test the 'test if a set of FDs
    form a minimal cover' feature
    """

    gui = None

    @classmethod
    def setUpClass(cls):
        '''Instantiate the gui'''
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        
        CoverEqualityTests.gui = core.UI()
        CoverEqualityTests.gui.ui.stackedWidget.setCurrentIndex(1)

    
    def setUp(self):        
        self.assertTrue(self.open_good_file())


    def test_good_cover(self):
        QtCore.QTimer.singleShot(1000, lambda: self.assertTrue(len(QApplication.activeModalWidget().buttons())==1))
        QtCore.QTimer.singleShot(2000, lambda: QTest.mouseClick(QApplication.activeModalWidget().buttons()[0], Qt.LeftButton))
        QTest.mouseClick(CoverEqualityTests.gui.ui.testCoverBtn, Qt.LeftButton)
        return True

    def test_bad_nofix_cover(self):
        QTest.mouseClick(CoverEqualityTests.gui.ui.clearCoverBtn, Qt.LeftButton)
        QtCore.QTimer.singleShot(1000, lambda: self.assertTrue(len(QApplication.activeModalWidget().buttons())==3))
        QtCore.QTimer.singleShot(2000, lambda: QTest.mouseClick(QApplication.activeModalWidget().buttons()[0], Qt.LeftButton))
        QTest.mouseClick(CoverEqualityTests.gui.ui.testCoverBtn, Qt.LeftButton)
        return True

    def test_bad_fix_cover(self):
        QTest.mouseClick(CoverEqualityTests.gui.ui.clearCoverBtn, Qt.LeftButton)
        QtCore.QTimer.singleShot(1000, lambda: self.assertTrue(len(QApplication.activeModalWidget().buttons())==3))
        QtCore.QTimer.singleShot(2000, lambda: QTest.mouseClick(QApplication.activeModalWidget().buttons()[0], Qt.LeftButton))
        QTest.mouseClick(CoverEqualityTests.gui.ui.testCoverBtn, Qt.LeftButton)
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

    def set_file(self, fileName):
        QTest.qWaitForWindowActive(CoverEqualityTests.gui)
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QTest.keyPress(CoverEqualityTests.gui, Qt.Key_O, Qt.ControlModifier)
        QTest.keyRelease(CoverEqualityTests.gui, Qt.Key_O, Qt.ControlModifier)


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

    testSuite = unittest.makeSuite(CoverEqualityTests, 'test')
    runner = unittest.TextTestRunner()
    runner.run(testSuite)
