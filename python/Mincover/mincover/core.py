#!/user/bin/python3
# -*- coding: utf-8 -*-

""""
This module customizes the user interface and defines
the control flow of the Mincover program
"""

import os
import re
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtWidgets import QMainWindow, QDialog, QFileDialog
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import QtCore


from view.interface import Ui_MainWindow
from view.ui_input import Ui_Dialog

import mincover


__all__ = ["UI"]

_translate = QtCore.QCoreApplication.translate


class UI(QMainWindow):
    """
    The UI class is the delegate of QMainWindow. It is the interface
    between the main application and the user interface
    """
    def __init__(self):
        super(UI, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.initUI()                
        self.show()

    def initUI(self):
        """Initialize and define properties of the main window"""
        
        self.setGeometry(300, 100, 450, 620)
        self.setWindowTitle('Minimal Cover Widget')
        #self.setWindowIcon(QIcon('icon.png'))

        self.addMenus()
        self.addCallbacks()

        initModel(self.ui.fdText)
        initModel(self.ui.mincoverText)
        

    def addMenus(self):
        """Add customized menubar to the main window"""
        
        self.menu = self.menuBar()        

        self.addFileMenu()
        self.addToolsMenu()


    def addFileMenu(self):

        fileMenu = self.menu.addMenu('&File')
        
        # Load previous instance option
        openAction = QAction(QIcon(), '&Open previous...', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Import previously saved Mincover data')
        openAction.triggered.connect(lambda: import_data(self))

        # Import from csv option
        csvImport = QAction(QIcon(), '&Import from CSV', self)
        csvImport.setShortcut('Ctrl+Shift+I')
        csvImport.setStatusTip('Import Schema as first line of a comma-separated file')
        csvImport.triggered.connect(lambda: importCSV(self, self.ui.schemaLine))

        # Add modal dialog for choosing database type and path to driver & database
        dbImport = QAction(QIcon(), '&Import from existing database', self)
        dbImport.setShortcut('Ctrl+I')
        dbImport.setStatusTip('Import Schema from a database')
        dbImport.triggered.connect(lambda: importCSV(self, self.ui.schemaLine))

        exitAction = QAction(QIcon(), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        fileMenu.addAction(openAction)
        fileMenu.addAction(dbImport)
        fileMenu.addAction(csvImport)
        fileMenu.addAction(exitAction)

    def addToolsMenu(self):
        
        toolMenu = self.menu.addMenu('&Tools')
        

    ###################     Callbacks   ###################

    def addCallbacks(self):
        """Connect signals to appropriate callbacks"""
        
        self.ui.editFDBtn.clicked.connect(self.get_fds)        
        self.ui.splitBtn.clicked.connect(self.split_fds)
        self.ui.clearBtn.clicked.connect(self.clear_fds)

        self.ui.editSchemaBtn.clicked.connect(self.get_schema)
        self.ui.genBtn.clicked.connect(lambda: gen_cover(self.ui.mincoverText))
        self.ui.saveBtn.clicked.connect(lambda: export_cover(self, self.ui.mincoverText))


    def get_schema(self):
        """Launch manual entry dialog for schema"""        
        global _attributes
        
        self.window = QDialog()
        self.form = Ui_Dialog()     
        self.form.setupUi(self.window)        
        self.form.attrLabel.setText(_translate("Dialog", "Enter attribute name"))
        self.form.confirmBtn.clicked.connect(lambda: addAttr(self.form))
        self.form.clearBtn.clicked.connect(lambda: clearSchema(self.form))
        self.form.buttonBox.accepted.connect(lambda: update(self.form, self.ui.schemaLine))
        
        
        initModel(self.form.schemaView)
        for attr in _attributes:            
            newAttr = QStandardItem(attr)
            self.form.schemaView.data.appendRow(newAttr)
        self.ui.schemaLine.setText(','.join(_attributes))
        self.window.exec_()

    def get_fds(self):
        """Launch manual entry dialog for functional dependencies"""
        
        self.window = QDialog()
        self.form = Ui_Dialog()     
        self.form.setupUi(self.window)        
        self.form.attrLabel.setText(_translate("Dialog", "Enter Dependency in form attr1, attr2 - attr3, attr4"))
        self.form.confirmBtn.clicked.connect(lambda: addFD(self.form))
        self.form.clearBtn.clicked.connect(lambda: clearSchema(self.form))
        self.form.buttonBox.accepted.connect(lambda: updateFD(self.form, self.ui.fdText))
        
        initModel(self.form.schemaView)
        
        for dep in _fds:
            text = dep.replace('-', "\t\u27F6\t")
            newFD = QStandardItem(text)            
            self.form.schemaView.data.appendRow(newFD)
        self.window.exec_()

    def split_fds(self):
        """Split the rhs of the FDs in the view and update interface"""
        global _fds
        
        split_fds = mincover.split_rhs([[dep.split(',') for dep in fd.split('-')] for fd in _fds])
        self.ui.fdText.data.clear()
        
        # format string
        _fds = ["-".join([", ".join(a) for a in each]) for each in split_fds]
        
        for fd in _fds:
            text = fd.replace('-', "\t\u27F6\t")
            newFD = QStandardItem(text)            
            self.ui.fdText.data.appendRow(newFD)
        

    def clear_fds(self):
        """Empty the set of functional dependencies"""
        global _fds
        
        _fds = []
        self.ui.fdText.data.clear()    




def initModel(listView):
    """Define the data model for the specified widget"""
    
    data = QStandardItemModel(listView)
    listView.data = data
    listView.setModel(data)



    ###################     Update   ###################


def update(source, schema):
    """Update the schema displayed in the interface"""
    global _attributes

    _attributes = []
    for i in range(source.schemaView.data.rowCount()):
        _attributes.append(source.schemaView.data.item(i).text())
    schema.setText(','.join(_attributes))


def updateFD(source, fdBox):
    """Update the functional dependencies displayed in the interface"""
    global _fds
    _fds = []

    for i in range(source.schemaView.data.rowCount()):
        _fds.append(source.schemaView.data.item(i).text().replace("\t\u27F6\t", "-"))

    fdBox.data.clear()
    for dep in _fds:
        text = dep.replace('-', "\t\u27F6\t")
        newFD = QStandardItem(text)            
        fdBox.data.appendRow(newFD)

    ###################     Entry   ###################

_attributes = []
_fds = []
_cover = []


def addAttr(source):
    """Validate entry of attribute to input dialog"""
    attributes = []
    for i in range(source.schemaView.data.rowCount()):
        attributes.append(source.schemaView.data.item(i).text())
    
    
    inputText = source.attrEntry.text()
    attr = str(inputText)
    attr = re.match("[\w+_][\w+\d+_]*", attr)

    if attr is not None:
        if attr.groups() == ():
            text = attr.group(0)
            if len(text) == len(inputText) and text.lower() not in attributes:
                attributes.append(text.lower())
                newAttr = QStandardItem(text)
                source.schemaView.data.appendRow(newAttr)
                source.attrEntry.clear()

def clearSchema(source):
    """Clear data from input form"""
    source.schemaView.data.clear()

def addFD(source):
    """Validate entry of functional dependency to input dialog"""
    global _attributes
    deps = []
    
    for i in range(source.schemaView.data.rowCount()):
        deps.append(source.schemaView.data.item(i).text())
    
    inputText = source.attrEntry.text()
    fd = str(inputText).replace(' ', '') # narrow the scope using regex
    fd = re.match("\w+[,\w]*-\w+[,\w]*", fd)

    if fd is not None:
        if fd.groups() == ():
            text = fd.group(0)
            
            for attr in re.split('[,-]', text):
                if attr not in _attributes:            
                    return
            if text not in deps:
                deps.append(text)
                text = text.replace('-', "\t\u27F6\t")
                newFD = QStandardItem(text)            
                source.schemaView.data.appendRow(newFD)
                source.attrEntry.clear()


def importCSV(window, schema):
    """Import a schema from a comma-delimited file"""
    import csv
    global _attributes

    fileName = QFileDialog.getOpenFileName(window, _translate("MainWindow", "Open File"), "",
        _translate("MainWindow", "Comma-separated (*.csv);;Text files (*.txt);;All files (*.*)"))

    if os.path.isfile(fileName[0]):
        with open(fileName, 'r', newline='') as infile:            
            if csv.Sniffer().has_header(infile.readline()):
                infile.seek(0)
                reader = csv.reader(infile)
                text = next(reader) # -> [attr1, attr2, ..., attrN]
                _attributes = [s.lower() for s in text]
                for attr in _attributes:
                    schema.text = _attributes
            else:
                print("Invalid formatting")



def export_cover(window, source):
    """Export the minimal cover to file"""

    fileName = QFileDialog.getSaveFileName(window, _translate("MainWindow", "Save File"), "",
        _translate("MainWindow", "DB Design File (*.fdcover);;Comma-separated (*.csv);;Text files (*.txt);;All files (*.*)"))

    dependencies = []
    for i in range(source.data.rowCount()):
        dependencies.append(source.data.item(i).text().replace("\t\u27F6\t", '-'))

    # Minimal cover  
    data = '\n'.join(dependencies)    

    # Functional dependencies
    deps = []
    for i in range(window.ui.fdText.data.rowCount()):
        deps.append(window.ui.fdText.data.item(i).text().replace("\t\u27F6\t", "-"))

    # Write to file
    if fileName is not None:
        with open(fileName[0], "w") as outfile:
            outfile.write("Minimal Cover for Schema: ")
            outfile.write(window.ui.schemaLine.text() + "\n")
            outfile.write("With functional dependencies:")
            outfile.write(', '.join(deps) + "\n")
            outfile.write(data)
                                       

def import_data(window):
    """Import previously exported dataset"""
    global _attributes
    global _fds
    global _cover
    
    dialog = QFileDialog(window, _translate("MainWindow", "Open File"), "",
        _translate("MainWindow", "DB Design File (*.fdcover);;All files (*.*)"),
                             options = 0)
    dialog.setFileMode(QFileDialog.ExistingFile)
    dialog.text = lambda x=dialog.result: dialog.selectedFiles()[0] if x() else None
    #dialog.text = dialog.selectedFiles() if dialog.result() else None ##doesn't work
    dialog.accepted.connect(lambda: dialog.text)
    dialog.exec()

    fileName = dialog.text()
    if fileName is None:
        return

    if os.path.isfile(fileName):
        with open(fileName, "r") as infile:
            try:                
                line1 = infile.readline()
                schema = line1[:-1].split(":")[1][1:]
                
                line2 = infile.readline()
                fds = line2[:-1].split(':')[1].split(', ')

                cover = infile.read().split('\n')

                attributes = [s.lower() for s in schema.split(',')]

                for dep in fds:
                    if not testFD(dep, attributes):
                        raise DatabaseError("FD(s) contain attributes not in schema")

                for fd in cover:
                    if not testFD(fd, attributes):
                        raise DatabaseError("FD(s) contain attributes not in schema")

                if cover != []:
                    import mincover
                    ffds = [[dep for dep in fd.split('-')] for fd in fds]
                    ffds = mincover.mincover(ffds)
                    ffds = ["-".join([", ".join(a) for a in each]) for each in ffds]
                    assert equality(cover, ffds)

                _attributes = attributes
                _fds = fds
                _cover = cover

                window.ui.fdText.data.clear()
                window.ui.mincoverText.data.clear()

                window.ui.schemaLine.setText(schema)

                for dep in fds:
                    text = dep.replace('-', "\t\u27F6\t")
                    newFD = QStandardItem(text)            
                    window.ui.fdText.data.appendRow(newFD)
                    
                for dep in cover:
                    text = dep.replace('-', "\t\u27F6\t")
                    newFD = QStandardItem(text)            
                    window.ui.mincoverText.data.appendRow(newFD)
                    
            except (IndexError, DatabaseError, EqualityError) as e:
                print(e)



def testFD(fd, attributes):
    """Test that fd only contains attributes listed in the schema"""

    fd = str(fd).replace(' ', '')
    if fd is not None:            
        for attr in re.split('[,-]', fd):
            if attr not in attributes:            
                return False
    return True

    ###################     Generator     ###################


def gen_cover(coverBox):
    """Use functional dependencies to generate a minimal cover"""
    import mincover

    global _fds
    global _cover

    # Format for function call to mincover
    ffds = [[dep for dep in fd.split('-')] for fd in _fds]
    
    cover = mincover.mincover(ffds)
    
    # Format mincover output to match required output
    _cover = ["-".join([", ".join(a) for a in each]) for each in cover]

    # Update interface with minimal cover
    coverBox.data.clear()
    for dep in _cover:
        text = dep.replace('-', "\t\u27F6\t")
        newFD = QStandardItem(text)            
        coverBox.data.appendRow(newFD)

#Dependencies of form ['a-b,c', 'a,b-c']
def equality(set1, set2):
    from collections import Counter

    if Counter(set1) == Counter(set2):
        return True
    else:
        raise EqualityError("Sets of FDs are not equivalent")

class DatabaseError(Exception):
    pass

class EqualityError(Exception):
    pass
