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


    def test_test(self):
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeyEvent
        QTest.qWaitForWindowActive(self.gui)


        dialog = QFileDialog(self.gui, _translate("MainWindow", "Open File"), "",
        _translate("MainWindow", "DB Design File (*.fdcover);;All files (*.*)"),
                             options = 0)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.accepted.connect(lambda: test2(dialog))
        dialog.exec()

##        QtCore.QTimer.singleShot(2000, lambda: QApplication.activeModalWidget().keyPressEvent(QKeyEvent(QEvent.KeyPress, Qt.Key_Escape, Qt.NoModifier)))
##        QtCore.QTimer.singleShot(2000, lambda: test())
##        QTest.keyPress(self.gui, Qt.Key_O, Qt.ControlModifier)
##        QTest.keyRelease(self.gui, Qt.Key_O, Qt.ControlModifier)

def test2(window):
    print("test2")
    print(window.selectedFiles()[0])

def test():
    global window
    from PyQt5.QtCore import QEvent
    from PyQt5.QtGui import QKeyEvent
    window = QApplication.activeModalWidget()

    QApplication.activeModalWidget().keyPressEvent(QKeyEvent(QEvent.KeyPress, Qt.Key_Enter, Qt.NoModifier))
    QApplication.activeModalWidget().keyPressEvent(QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier))

##    window.selectFile("sample.fdcover")
##    window.currentChanged.emit(os.path.abspath("sample.fdcover"))
##    window.fileSelected.emit(os.path.abspath("sample.fdcover"))
##    window.filesSelected.emit([os.path.abspath("sample.fdcover")])
##    window.filterSelected.emit("DB Design File (*.fdcover)")
##
##    window.selectedFiles = lambda: ["sample.fdcover"]
##
##    print(help(window.selectFile))
##   
##    window.accepted.emit()
##    window.finished.emit(1)
##    window.setResult(QDialog.Accepted)    
##    print(window.selectedFiles())
##    window.done(1)



    #print("test")
    #accepted = <unbound PYQT_SIGNAL accepted()>
    #selectUrl(...)
    #fileSelected = <unbound PYQT_SIGNAL fileSelected(QString)>
    #print(window)


    

##    for each in dir(window):
##        window.getattr(window, each) = lambda: ["sample.fdcover"]


if __name__ == "__main__":
    _projname = "mincover"
    parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    srcdir = os.path.join(parent, _projname)
    sys.path.append(srcdir)

    import core
    unittest.main()
