import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

_translate = QtCore.QCoreApplication.translate
app = QApplication(sys.argv)



class DatabaseTests(unittest.TestCase):
    """This class contains methods to test interfacing with databases
    """

    gui = None

    @classmethod
    def setUpClass(cls):
        '''Instantiate the gui'''
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        
        DatabaseTests.gui = core.UI()
        DatabaseTests.gui.ui.stackedWidget.setCurrentIndex(0)


    def test_bad_file(self):
        self.set_file("bad.csv")
        self.assertEqual(core._attributes, [])
        self.assertEqual(core._fds, [])
        self.assertEqual(core._cover, [])
        self.assertEqual(DatabaseTests.gui.ui.schemaLine.text(), "")

    def test_no_file(self):
        QTest.qWaitForWindowActive(DatabaseTests.gui)
        QtCore.QTimer.singleShot(2000, lambda: QTest.keyPress(QApplication.activeModalWidget(), Qt.Key_Escape))
        QTest.keyPress(DatabaseTests.gui, Qt.Key_I, Qt.ControlModifier)
        QTest.keyRelease(DatabaseTests.gui, Qt.Key_I, Qt.ControlModifier)
        
        self.assertEqual(core._attributes, [])
        self.assertEqual(core._fds, [])
        self.assertEqual(core._cover, [])
        self.assertEqual(DatabaseTests.gui.ui.schemaLine.text(), "")

    def test_good_file_single_table(self):
        self.set_file("daily_scrum.db")
        self.assertEqual(core._attributes, ['date', 'minutes'])
        self.assertEqual(core._fds, [])
        self.assertEqual(core._cover, [])
        self.assertEqual(DatabaseTests.gui.ui.schemaLine.text(), "date,minutes")

    def test_good_file_multi_table(self):
        fileName = "database.db"
        QTest.qWaitForWindowActive(DatabaseTests.gui)            
        QtCore.QTimer.singleShot(1000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), "Beers"))
        QTest.keyPress(DatabaseTests.gui, Qt.Key_I, Qt.ControlModifier)
        QTest.keyRelease(DatabaseTests.gui, Qt.Key_I, Qt.ControlModifier)

        self.assertEqual(core._attributes, ['name', 'manf'])
        self.assertEqual(core._fds, [])
        self.assertEqual(core._cover, [])
        self.assertEqual(DatabaseTests.gui.ui.schemaLine.text(), "name,manf")

    def test_good_file_no_table(self):
        self.set_file("empty.db")
        self.assertEqual(core._attributes, [])
        self.assertEqual(core._fds, [])
        self.assertEqual(core._cover, [])
        self.assertEqual(DatabaseTests.gui.ui.schemaLine.text(), "")

    def set_file(self, fileName):
        QTest.qWaitForWindowActive(DatabaseTests.gui)
        QtCore.QTimer.singleShot(2000, lambda: inject(QApplication.activeModalWidget(), fileName))
        QTest.keyPress(DatabaseTests.gui, Qt.Key_I, Qt.ControlModifier)
        QTest.keyRelease(DatabaseTests.gui, Qt.Key_I, Qt.ControlModifier)

    def tearDown(self):
        core._attributes = []
        core._fds = []
        core._cover = []
        DatabaseTests.gui.ui.schemaLine.setText("")

    @classmethod
    def tearDownClass(cls):
        DatabaseTests.gui.destroy()

def inject(window, fileName):
    window.text = lambda: fileName
    window.close()



if __name__ == "__main__":
    _projname = "mincover"
    parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    srcdir = os.path.join(parent, _projname)
    sys.path.append(srcdir)

    import core

    testSuite = unittest.makeSuite(DatabaseTests, 'test')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testSuite)
