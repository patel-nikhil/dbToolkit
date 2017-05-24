# -*- coding: utf-8 -*-

# Tools and interface for normal form tools

from PyQt5.QtWidgets import QDialog

### First Normal Form  ###

def first_nf_prompt():
    '''Display advice/examples of converting to 1NF'''
    from view.first_nf_prompt import Ui_Dialog as Dialog
    window = QDialog()
    prompt = Dialog()
    prompt.setupUi(window)
    window.exec_()


### Second Normal Form  ###

def second_nf_prompt():
    '''Display advice/examples of converting to 2NF'''
    pass

def second_nf_tools():
    pass


### Third Normal Form  ###

def third_nf_prompt():
    '''Display advice/examples of converting to 3NF'''
    pass

def third_nf_tools():
    pass


### Boyce-Codd Normal Form  ###

def bcnf_prompt():
    '''Display advice/examples of BCNF'''
    pass

def bcnf_tools():
    pass


### Fourth Normal Form  ###

def fourth_nf_prompt():
    '''Display advice/examples of 4NF'''
    pass

def fourth_nf_tools():
    pass


def fifth_nf_prompt():
    '''Display advice/examples of converting to 5NF'''
    pass

def fifth_nf_tools():
    pass
