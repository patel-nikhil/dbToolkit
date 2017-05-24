# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow

from view.interface import Ui_MainWindow
from view.util import *

class UI(QMainWindow):

    def __init__(self):
        '''Initialize and customize the UI'''
        super(UI, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.page = 0

        self.init()                      
        self.show()
    
    def next_page(self):
        '''Make the next page of the UI active'''
        self.page += 1
        self.ui.nav.setCurrentIndex(self.page)

    
    def init(self):
        self.set_splash()
        self.set_page1()
        self.set_page2()
        self.set_page3()
        self.set_pageb()
        self.set_page4()
        self.set_page5()


    def set_splash(self):
        self.ui.start_btn.clicked.connect(self.next_page)
    
    def set_page1(self):
        self.ui.yes_btn_1.clicked.connect(self.next_page)
        self.ui.no_btn_1.clicked.connect(first_nf_prompt)

    def set_page2(self):
        self.ui.yes_btn_2.clicked.connect(self.next_page)
        self.ui.no_btn_2.clicked.connect(second_nf_prompt)
        self.ui.test_btn_2.clicked.connect(second_nf_tools)

    def set_page3(self):
        self.ui.yes_btn_3.clicked.connect(self.next_page)
        self.ui.no_btn_3.clicked.connect(third_nf_prompt)
        self.ui.test_btn_3.clicked.connect(third_nf_tools)

    def set_pageb(self):
        self.ui.yes_btn_b.clicked.connect(self.next_page)
        self.ui.no_btn_b.clicked.connect(bcnf_prompt)
        self.ui.test_btn_b.clicked.connect(bcnf_tools)
        
    def set_page4(self):
        self.ui.yes_btn_4.clicked.connect(self.next_page)
        self.ui.no_btn_4.clicked.connect(fourth_nf_prompt)
        self.ui.test_btn_4.clicked.connect(fourth_nf_tools)
        
    def set_page5(self):
        self.ui.restart_btn.clicked.connect(self.restart)
        self.ui.exit_btn.clicked.connect(self.exitapp)
        #self.ui.yes_btn_5.clicked.connect(fifth_nf_prompt)
        #self.ui.no_btn_5.clicked.connect(fifth_nf_tools)

    def restart(self):
        self.page = 0
        self.ui.nav.setCurrentIndex(self.page)

    def exitapp(self):
        exit()
