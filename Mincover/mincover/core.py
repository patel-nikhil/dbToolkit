#!/user/bin/python3
# -*- coding: utf-8 -*-

"""
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

from view.ui_stacked import Ui_MainWindow
from view.ui_input import Ui_Dialog
from view.char_input import Ui_Dialog as charDialog

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
        
        self.init_ui()                
        self.show()

    def init_ui(self):
        """Initialize and define properties of the main window"""
        
        self.setGeometry(300, 100, 450, 620)
        self.setWindowTitle('Minimal Cover Widget')
        #self.setWindowIcon(QIcon('icon.png'))
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.page = lambda: self.ui.stackedWidget.currentIndex()
        self.add_menus()
        self.set_page_one()
        self.set_page_two()

        init_model(self.ui.fdText)
        init_model(self.ui.mincoverText)

        init_model(self.ui.fdText_2)
        init_model(self.ui.mincoverText_2)
        
        

    def add_menus(self):
        """Add customized menubar to the main window"""
        
        self.menu = self.menuBar()
        self.add_file_menu()
        self.add_tools_menu()


    def add_file_menu(self):
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
        csvImport.triggered.connect(lambda: import_csv(self, (self.ui.schemaLine_2 if self.page() else self.ui.schemaLine)))

        # Import from file option
        fileImport = QAction(QIcon(), '&Import from file', self)
        fileImport.setShortcut('Ctrl+Shift+F')
        fileImport.setStatusTip('Import Schema as first line of a character-delimited file')
        fileImport.triggered.connect(lambda: import_file(self, (self.ui.schemaLine_2 if self.page() else self.ui.schemaLine)))

        # Add modal dialog for choosing database type and path to driver & database
        dbImport = QAction(QIcon(), '&Import from existing database', self)
        dbImport.setShortcut('Ctrl+I')
        dbImport.setStatusTip('Import Schema from a database')
        dbImport.triggered.connect(lambda: import_sqlite(self, (self.ui.schemaLine_2 if self.page() else self.ui.schemaLine)))
        #dbImport.triggered.connect(lambda pg=self.page: lambda: import_csv(self, self.ui.schemaLine_2) if pg() else lambda: import_csv(self, self.ui.schemaLine_2))

        exitAction = QAction(QIcon(), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        fileMenu.addAction(openAction)
        fileMenu.addAction(dbImport)
        fileMenu.addAction(csvImport)
        fileMenu.addAction(fileImport)
        fileMenu.addAction(exitAction)

    def add_tools_menu(self):
        
        toolMenu = self.menu.addMenu('&Tools')

        # Load previous instance option
        page1 = QAction(QIcon(), '&Cover Generation Mode', self)
        page1.setShortcut('Ctrl+G')
        page1.setStatusTip('Switch to interface for generating minimal cover')
        page1.triggered.connect(self.switch_page1)

        # Load previous instance option
        page2 = QAction(QIcon(), '&Cover Testing Mode', self)
        page2.setShortcut('Ctrl+T')
        page2.setStatusTip('Switch to interface for testing minimal cover')
        page2.triggered.connect(self.switch_page2)

        toolMenu.addAction(page1)
        toolMenu.addAction(page2)
        

    ###################     Callbacks   ###################

    def clear_all(self):
        self.ui.fdText.data.clear()
        self.ui.fdText_2.data.clear()
        self.ui.mincoverText.data.clear()
        self.ui.mincoverText_2.data.clear()

    def switch_page1(self):
        global _fds
        
        self.clear_all()
        self.ui.schemaLine.setText(self.ui.schemaLine_2.text())
        for dep in _fds:
            text = dep.replace('-', "\t\u27F6\t")
            newFD = QStandardItem(text)            
            self.ui.fdText.data.appendRow(newFD)
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_page2(self):
        global _fds
        global _cover
                                
        self.clear_all()
        self.ui.schemaLine_2.setText(self.ui.schemaLine.text())
        for dep in _fds:
            text = dep.replace('-', "\t\u27F6\t")
            newFD = QStandardItem(text)            
            self.ui.fdText_2.data.appendRow(newFD)

        for dep in _cover:
            text = dep.replace('-', "\t\u27F6\t")
            newFD = QStandardItem(text)            
            self.ui.mincoverText_2.data.appendRow(newFD)
        self.ui.stackedWidget.setCurrentIndex(1)

                                

    def set_page_one(self):
        """Connect signals to appropriate callbacks"""
        self.ui.editFDBtn.clicked.connect(self.get_fds)        
        self.ui.splitFDBtn.clicked.connect(self.split_fds)
        self.ui.clearFDBtn.clicked.connect(lambda: self.clear_fds(self.ui.fdText))
        
        self.ui.editSchemaBtn.clicked.connect(self.get_schema)
        self.ui.genCoverBtn.clicked.connect(lambda: gen_cover(self.ui.mincoverText))
        self.ui.saveCoverBtn.clicked.connect(lambda: export_cover(self, self.ui.mincoverText))

        
    def set_page_two(self):
        """Connect signals to appropriate callbacks"""
        self.ui.editFDBtn_2.clicked.connect(self.get_fds)        
        self.ui.clearFDBtn_2.clicked.connect(lambda: self.clear_fds(self.ui.fdText_2))
        self.ui.editSchemaBtn_2.clicked.connect(self.get_schema)
        
        self.ui.editCoverBtn.clicked.connect(self.get_cover)
        self.ui.clearCoverBtn.clicked.connect(lambda: self.clear_cover(self.ui.mincoverText_2))
        self.ui.testCoverBtn.clicked.connect(lambda: test_cover(self.ui.fdText_2, self.ui.mincoverText_2))


    def get_schema(self):
        """Launch manual entry dialog for schema"""
        global _attributes
        
        self.window = QDialog()
        self.form = Ui_Dialog()     
        self.form.setupUi(self.window)        
        self.form.attrLabel.setText(_translate("Dialog", "Enter attribute name"))
        self.form.confirmBtn.clicked.connect(lambda: add_attribute(self.form))
        self.form.clearBtn.clicked.connect(lambda: clear_schema(self.form))
        self.form.buttonBox.accepted.connect(lambda: update(self.form, (self.ui.schemaLine_2 if self.page() else self.ui.schemaLine)))
        
        init_model(self.form.schemaView)
        for attr in _attributes:            
            newAttr = QStandardItem(attr)
            self.form.schemaView.data.appendRow(newAttr)

        if self.page():
            self.ui.schemaLine_2.setText(','.join(_attributes))
        else:
            self.ui.schemaLine.setText(','.join(_attributes))
        self.window.exec_()

    def get_fds(self):
        """Launch manual entry dialog for functional dependencies"""
        self.window = QDialog()
        self.form = Ui_Dialog()     
        self.form.setupUi(self.window)        
        self.form.attrLabel.setText(_translate("Dialog", "Enter Dependency in form attr1, attr2 - attr3, attr4"))
        self.form.confirmBtn.clicked.connect(lambda: add_fd(self.form))
        self.form.clearBtn.clicked.connect(lambda: clear_schema(self.form))
        self.form.buttonBox.accepted.connect(lambda: update_fds(self.form, (self.ui.fdText_2 if self.page() else self.ui.fdText)))
        
        init_model(self.form.schemaView)
        
        for dep in _fds:
            text = dep.replace('-', "\t\u27F6\t")
            newFD = QStandardItem(text)            
            self.form.schemaView.data.appendRow(newFD)
        self.window.exec_()

    def get_cover(self):
        """Launch manual entry dialog for minimal cover FDs"""
        
        self.window = QDialog()
        self.form = Ui_Dialog()     
        self.form.setupUi(self.window)        
        self.form.attrLabel.setText(_translate("Dialog", "Enter Dependency in form attr1, attr2 - attr3, attr4"))
        self.form.confirmBtn.clicked.connect(lambda: check_fd(self, self.form))
        self.form.clearBtn.clicked.connect(lambda: clearCover(self.form))
        self.form.buttonBox.accepted.connect(lambda: update_cover(self.form, self.ui.mincoverText_2))
        
        init_model(self.form.schemaView)
        
        for dep in _cover:
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
        
    def clear_fds(self, fdBox):
        """Empty the set of functional dependencies"""
        global _fds
        
        _fds = []
        fdBox.data.clear()

    def clear_cover(self, coverBox):
        """Empty the fds that comprise the proposed minimal cover"""
        global _cover
        
        _cover = []
        coverBox.data.clear()


def init_model(listView):
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
    

def update_fds(source, fdBox):
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

def update_cover(source, coverBox):
    """Update the proposed minimal cover displayed in the interface"""
    global _cover
    _cover = []
    
    for i in range(source.schemaView.data.rowCount()):
        _cover.append(source.schemaView.data.item(i).text().replace("\t\u27F6\t", "-"))
    
    coverBox.data.clear()
    for dep in _cover:
        text = dep.replace('-', "\t\u27F6\t")
        newFD = QStandardItem(text)            
        coverBox.data.appendRow(newFD)

        
    ###################     Entry   ###################

_attributes = []
_fds = []
_cover = []


def add_attribute(source):
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

def clear_schema(source):
    """Clear data from input form"""
    source.schemaView.data.clear()

def add_fd(source):
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

def check_fd(window, source):
    """Add FDs to minimal cover"""
    
    # Functional dependencies
    deps = []
    for i in range(window.ui.fdText_2.data.rowCount()):
        deps.append(window.ui.fdText_2.data.item(i).text().replace("\t\u27F6\t", "-"))

    inputText = source.attrEntry.text()
    fd = str(inputText).replace(' ', '') # narrow the scope using regex
    fd = re.match("\w+[,\w]*-\w+[,\w]*", fd)

    if fd is not None:
        if fd.groups() == ():
            text = fd.group(0)

            if text not in deps:
                return
            else:
                text = text.replace('-', "\t\u27F6\t")
                newFD = QStandardItem(text)            
                source.schemaView.data.appendRow(newFD)
                source.attrEntry.clear()


def import_sqlite(window, schema):
    import sqlite3
    from view.ui_tables import Ui_Dialog as TableDialog

    global _attributes
    global _fds
    global _cover
    
    fileName = get_file(window, 2)
    if fileName is None:
        return
    
    if os.path.isfile(fileName):

        with open(fileName, "rb") as dbfile:
            header = dbfile.read(100)
            
            if header[0:16] != b'SQLite format 3\x00':
                return
            
        connection = sqlite3.connect(fileName)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tableList = cursor.fetchall()
        
        if len(tableList) == 0:
            return
        elif len(tableList) > 1:
            import traceback
            try:
                dialog = QDialog()
                td = TableDialog()
                td.setupUi(dialog)
                td.tables.addItems([table[0] for table in tableList])
                dialog.text = lambda x=dialog.result: td.tables.currentText() if x() else None
                td.buttonBox.accepted.connect(dialog.text)
                dialog.exec_()

                table = dialog.text()
            except:
                print(traceback.format_exc())
        else:                
            table = tableList[0][0]

        if table is not None:
            cursor.execute("pragma table_info ({})".format(table))
            metaInfo = cursor.fetchall()
            _attributes = [s[1] for s in metaInfo]
            schema.setText(','.join(_attributes))
            window.clear_all()
            _fds = []
            _cover = []
            
        connection.close()
    

def import_database(window, schema):

    import sqlite3
    from view.ui_tables import Ui_Dialog as TableDialog
    supportedDB = ["SQLite, SQL Server"]
    
    dialog = QDialog()
    td = TableDialog()
    td.setupUi(dialog)
    td.tables.addItems(supportedDB)
    dialog.text = lambda x=dialog.result: td.tables.currentText() if x() else None
    td.buttonBox.accepted.connect(dialog.text)
    dialog.exec_()

    dbms = dialog.text()

    if dbms is not None:
        if dbms == "SQLite":
            import_sqlite(window, schema)
            return

    from PyQt5.QtWidgets import QMessageBox
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Information")
    msgBox.setIcon(QMessageBox.NoIcon)
    msgBox.setText('''You will need a compatible JRE installed (32 or 64-bit depending
    on which version of this program you are using).
    You will need to provide a JDBC driver for your DBMS.
    Only SQLite support is natively included''')
    msgBox.exec_()

    driver = get_file(window, 5)
    if fileName is None:
        return

    if os.path.isfile(fileName):
        auth = getAuthentication(window)
        if dbms == "SQL Server":
            import_sqlserver(window, schema, driver, auth)
            return


def import_sqlserver(window, schema, jar, auth, port=1433):
    import jaydebeapi
    global connection
    global cursor

    from PyQt5.QtWidgets import QMessageBox
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Information")
    msgBox.setIcon(QMessageBox.NoIcon)
    msgBox.setText('''A SQL Server instance must be running with TCP/IP connectivity enabled''')
    msgBox.exec_()
    
    driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    dbURL = "jdbc:sqlserver://localhost;database=TEST2;integratedSecurity=true"
    jar = "data//dbfiles//sqljdbc41.jar"
    connection = jaydebeapi.connect(driver, dbURL, jars=jar)
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT TABLE_NAME FROM TEST2.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA ='dbo'")
    tables = [t[0] for t in cursor.fetchall()]
    print("tables");print(tables)
    for table in tables:
        cursor.execute("SELECT COLUMN_NAME FROM TEST2.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ='{}' AND TABLE_SCHEMA ='dbo'".format(table))
        attrs = [c[0] for c in cursor.fetchall()]
        print(table)
        print(attrs)
            
    connection.close()

def import_csv(window, schema):
    """Import a schema from a comma-delimited file"""
    import csv
    global _attributes
    global _fds
    global _cover
    
    fileName = get_file(window, 1)
    if fileName is None:
        return
    
    if os.path.isfile(fileName):
        with open(fileName, 'r', newline='') as infile:
            if csv.Sniffer().has_header(infile.readline()):
                infile.seek(0)
                reader = csv.reader(infile)
                text = next(reader) # -> [attr1, attr2, ..., attrN]                
                _attributes = [s for s in text]
                schema.setText(','.join(_attributes))
                window.clear_all()
                _fds = []
                _cover = []
            else:
                print("Invalid formatting")


def import_file(window, schema):
    """Import a schema from a character-delimited file"""
    global _attributes
    global _fds
    global _cover
        
    dialog = QDialog()
    inDialog = charDialog()
    inDialog.setupUi(dialog)    
    dialog.text = lambda x=dialog.result: inDialog.delim.text() if x() else None    
    dialog.accepted.connect(dialog.text)
    dialog.exec_()

    sep = dialog.text()
    if sep is None or sep == "":
        return
    
    fileName = get_file(window, 3)
    if fileName is None:
        return

    if os.path.isfile(fileName):
        with open(fileName, 'r') as infile:            
            text = infile.readline()[:-1] # -> [attr1, attr2, ..., attrN]
            attrs = text.split(sep)
            _attributes = attrs
            schema.setText(','.join(_attributes))
            window.clear_all()
            _fds = []
            _cover = []

def export_cover(window, source):
    """Export the minimal cover to file"""

    fileName = get_file(window, 4)
    if fileName is None:
        return
    
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
    with open(fileName, "w") as outfile:
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
    
    fileName = get_file(window, 0)
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
                    if not test_fd(dep, attributes):
                        raise DatabaseError("FD(s) contain attributes not in schema")

                for fd in cover:
                    if not test_fd(fd, attributes):
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
                
                if window.page():
                    window.ui.fdText_2.data.clear()
                    window.ui.mincoverText_2.data.clear()
                    window.ui.schemaLine_2.setText(schema)

                    for dep in fds:
                        text = dep.replace('-', "\t\u27F6\t")
                        newFD = QStandardItem(text)            
                        window.ui.fdText_2.data.appendRow(newFD)
                    
                    for dep in cover:
                        text = dep.replace('-', "\t\u27F6\t")
                        newFD = QStandardItem(text)            
                        window.ui.mincoverText_2.data.appendRow(newFD)
                else:
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


def get_file(window, mode):
    """Prompt user for and return filename"""

    # Load data
    if mode == 0:
        dialog = QFileDialog(window, _translate("MainWindow", "Open File"), "",
            _translate("MainWindow", "DB Design File (*.fdcover);;All files (*.*)"),
                             options = 0)
        dialog.setFileMode(QFileDialog.ExistingFile)

    # Load schema (csv)
    elif mode == 1:
        dialog = QFileDialog(window, _translate("MainWindow", "Open File"), "",
            _translate("MainWindow", "Comma-separated file (*.csv);;All files (*.*)"),
                             options = 0)
        dialog.setFileMode(QFileDialog.ExistingFile)

    # Load schema (db)
    elif mode == 2:
        dialog = QFileDialog(window, _translate("MainWindow", "Open File"), "",
            _translate("MainWindow", "Sqlite Database (*.db);;All files (*.*)"),
                             options = 0)
        dialog.setFileMode(QFileDialog.ExistingFile)

    # Load character-delimited
    elif mode == 3:
        dialog = QFileDialog(window, _translate("MainWindow", "Open File"), "",
            _translate("MainWindow", "All files (*.*)"),
                             options = 0)
        dialog.setFileMode(QFileDialog.ExistingFile)

    # Save data
    elif mode == 4:
        dialog = QFileDialog(window, _translate("MainWindow", "Save File"), "",
            _translate("MainWindow", "DB Design File (*.fdcover);;Plain text file (*.txt);;All files (*.*)"),
                             options = 0)
        dialog.setFileMode(QFileDialog.AnyFile)
        
    dialog.text = lambda x=dialog.result: dialog.selectedFiles()[0] if x() else None    
    dialog.accepted.connect(lambda: dialog.text)
    dialog.exec_()
    if mode == 4:
        ext = dialog.selectedNameFilter()[:-1].split('*')[1]
    else:
        ext = ""
    fileName = dialog.text()
    if fileName is not None:
        fileName += ext
    return fileName


def test_fd(fd, attributes):
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

def test_cover(fdBox, coverBox):
    """Test the list of FDs in the cover box against a minimal cover"""
    import mincover

    # Specified FDs
    fds = []
    for i in range(fdBox.data.rowCount()):
        fds.append(fdBox.data.item(i).text().replace("\t\u27F6\t", '-'))

    # Proposed cover
    cover = []
    for i in range(coverBox.data.rowCount()):
        cover.append(coverBox.data.item(i).text().replace("\t\u27F6\t", "-"))
        
    ffds = [[dep for dep in fd.split('-')] for fd in fds]
    ffds = mincover.mincover(ffds)

    coverFDs = [[dep for dep in fd.split('-')] for fd in cover]

    try:

        # Compare closures from set of FDs and minimal cover
        assert equality(mincover.find_closures(ffds), mincover.find_closures(coverFDs))

        ffds = ["-".join([", ".join(a) for a in fd]) for fd in ffds]

        # Compare the specified and generated covers for equality
        assert equality(cover, ffds)


        from PyQt5.QtWidgets import QMessageBox
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Information")
        msgBox.setIcon(QMessageBox.NoIcon)
        msgBox.setText("The set of entered FDs form a minimal cover")
        msgBox.exec_()
    
    except EqualityError:

        from PyQt5.QtWidgets import QMessageBox
        msgBox = QMessageBox()
        msgBox.addButton(QMessageBox.Yes)
        msgBox.addButton(QMessageBox.No)
        msgBox.addButton(QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        msgBox.setWindowTitle("Information")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('''The set of entered FDs do not form a minimal cover
        Would you like to compute a minimal cover?''')
        nextAction = msgBox.exec_()

        if nextAction == QMessageBox.Yes:
            gen_cover(coverBox)


def equality(set1, set2):
    """Compares two sets of functional dependencies for equality"""
    from collections import Counter

    #Dependencies of form ['a-b,c', 'a,b-c']
    if Counter(set1) == Counter(set2):
        return True
    else:
        raise EqualityError("Sets of FDs are not equivalent")

class DatabaseError(Exception):
    pass

class EqualityError(Exception):
    pass
