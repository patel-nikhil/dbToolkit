import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

_translate = QtCore.QCoreApplication.translate
app = QApplication(sys.argv)


class LoadFileTests(unittest.TestCase):
    '''This class contains the methods for testing input/output operations'''

    gui = None

    @classmethod
    def setUpClass(cls):
        '''Instantiate the gui'''
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        
        LoadFileTests.gui = core.UI()


    def test_open_save_file(self):        
        self.assertTrue(self.open_no_file())
        self.assertTrue(self.open_no_file())
        self.assertTrue(self.open_bad_file())
        self.assertTrue(self.open_bad_fds())
        self.assertTrue(self.open_bad_cover())
        self.assertTrue(self.open_false_cover())
        self.assertTrue(self.open_good_file())

    def set_file(self, fileName):
        QTest.qWaitForWindowActive(LoadFileTests.gui)
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QTest.keyPress(LoadFileTests.gui, Qt.Key_O, Qt.ControlModifier)
        QTest.keyRelease(LoadFileTests.gui, Qt.Key_O, Qt.ControlModifier)


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

    @classmethod
    def tearDownClass(cls):
        LoadFileTests.gui.destroy()


class ReadFileTests(unittest.TestCase):
    '''This class contains the methods for testing file import operations'''

    gui = None

    @classmethod
    def setUpClass(cls):
        '''Instantiate the gui'''
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        
        ReadFileTests.gui = core.UI()

    def set_csv(self, fileName):
        QTest.qWaitForWindowActive(ReadFileTests.gui)
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QTest.keyPress(LoadFileTests.gui, Qt.Key_I, Qt.ControlModifier | Qt.ShiftModifier)        
        QTest.keyRelease(LoadFileTests.gui, Qt.Key_I, Qt.ControlModifier | Qt.ShiftModifier)        
    
    def set_file(self, delim, fileName):
        QTest.qWaitForWindowActive(ReadFileTests.gui)
        QtCore.QTimer.singleShot(1000, lambda: inject(QApplication.activeModalWidget(), delim))
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QTest.keyPress(ReadFileTests.gui, Qt.Key_F, Qt.ControlModifier | Qt.ShiftModifier)
        QTest.keyRelease(ReadFileTests.gui, Qt.Key_F, Qt.ControlModifier | Qt.ShiftModifier)        

    def test_read_good_csv(self):
        self.set_csv("good.csv")
        self.assertEqual(core._attributes,['name', 'manf'])
        self.assertEqual(ReadFileTests.gui.ui.schemaLine.text(),"name,manf")    

    def test_read_bad_csv(self):
        self.set_csv("bad.csv")
        self.assertEqual(core._attributes,['Minimal Cover for Schema: abc'])
        self.assertEqual(ReadFileTests.gui.ui.schemaLine.text(), 'Minimal Cover for Schema: abc')

    def test_read_no_csv(self):
        self.set_csv("no.csv")
        self.assertEqual(core._attributes, [])
        self.assertEqual(ReadFileTests.gui.ui.schemaLine.text(), "")

    def test_read_good_delim(self):
        self.set_file("|", "good_delim.txt")
        self.assertEqual(core._attributes, ['name', 'manf'])
        self.assertEqual(ReadFileTests.gui.ui.schemaLine.text(), "name,manf")

    def test_read_no_delim(self):        
        delim = ""
        fileName = "good_delim.txt"
        QTest.qWaitForWindowActive(ReadFileTests.gui)
        QtCore.QTimer.singleShot(1000, lambda: inject(QApplication.activeModalWidget(), delim))
        QTest.keyPress(ReadFileTests.gui, Qt.Key_F, Qt.ControlModifier | Qt.ShiftModifier)
        QTest.keyRelease(ReadFileTests.gui, Qt.Key_F, Qt.ControlModifier | Qt.ShiftModifier)
        
        self.assertEqual(core._attributes, [])
        self.assertEqual(ReadFileTests.gui.ui.schemaLine.text(), "")
        

    def tearDown(self):
        core._attributes = []
        ReadFileTests.gui.ui.schemaLine.setText("")

    @classmethod
    def tearDownClass(cls):
        ReadFileTests.gui.destroy()


def inject(window, fileName):
    window.text = lambda: fileName
    window.close()


if __name__ == "__main__":
    _projname = "mincover"
    parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    srcdir = os.path.join(parent, _projname)
    sys.path.append(srcdir)

    import core
    
    loader = unittest.TestLoader()
    testSuite = unittest.makeSuite(LoadFileTests, 'test')
    testSuite.addTests(loader.loadTestsFromTestCase(ReadFileTests))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testSuite)
