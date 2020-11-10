# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:30:03 2020

@author: chris
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QStyle, QMainWindow, QPushButton, QToolTip, QMessageBox, QWidget, QAction, QTabWidget,QVBoxLayout, QBoxLayout, QFormLayout, QLabel, QScrollArea, QScrollBar, QInputDialog, QLineEdit, QFileDialog, QGridLayout
from PyQt5.QtCore import QCoreApplication, QRect, pyqtSlot, QTimer, Qt
from PyQt5.QtGui import QIcon, QFont, QIntValidator

import os.path
import json
import functions

tabs = []
buttons = []

class SettingWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        grid = QGridLayout()
        self.parent = parent
        self.DT = self.parent.DT
        
        
        #Add default buttons
        self.addTab = QPushButton('Add Tab', self)
        self.addButton = QPushButton('Add Button', self)
        self.learnFunction = QPushButton('Learn Function', self)
        
        #Set size of the buttons
        self.addTab.setFixedSize(82, 50)
        self.addButton.setFixedSize(82, 50)
        self.learnFunction.setFixedSize(82, 50)
        
        #Add functions to the buttons
        self.addTab.clicked.connect(self.AddTab)
        self.addButton.clicked.connect(self.AddButton)
        self.learnFunction.clicked.connect(self.LearnFunction)
        
        grid.addWidget(self.addTab, 0, 0)
        grid.addWidget(self.addButton, 0, 1)
        grid.addWidget(self.learnFunction, 0, 2)
        
        
                
        # for i in range(0,5):
        #     for j in range(0,5):
        #         grid.addWidget(QPushButton(str(i)+str(j)),i,j)

        grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setLayout(grid)

        
    def addTabToMain(self, name):
        self.parent.appendTabs(name)
    
    def addButtonToMain(self, tab, name):
        self.parent.appendButton(tab, name)
    
    def AddTab(self):
        print("addTab pressed")
        self.parent.DT.testing()
        self.popup = NewTabPopup(self)
            
    def AddButton(self):
        print("addButton pressed")
        self.popup = NewButtonPopup(self)
            
    def LearnFunction(self):
        print("learnFunction pressed")
        self.popup = NewFunctionPopup(self)
        #self.parent.test_update()

class NewButtonPopup(QMainWindow):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
                
        self.setWindowTitle("New Button")
        self.setGeometry(400,220,400,220)
        
        self.initNewButtonUI()
        
    def initNewButtonUI(self):
        self.window = QWidget()
        self.setCentralWidget(self.window)
        grid = QGridLayout()
        
        #Define components of window
        self.newButton_Label = QLabel("Button Name:", self)
        grid.addWidget(self.newButton_Label, 0, 0)
        
        self.newButtonName_Input = QLineEdit(self)
        self.newButtonName_Input.setFixedSize(200,20)
        grid.addWidget(self.newButtonName_Input, 1, 0)
        
        self.assignFunction_Label = QLabel("Assign Function:", self)
        grid.addWidget(self.assignFunction_Label, 3, 0)
        
        self.assignFunction_List = QComboBox()
        func = self.parent.DT.functionsArray
        
        for i in func:
            self.assignFunction_List.addItem(i.functionName)
        grid.addWidget(self.assignFunction_List, 4, 0)
        
        self.assignToTab_Label = QLabel("Assign to Tab:", self)
        grid.addWidget(self.assignToTab_Label, 5, 0)
        
        self.assignToTab_List = QComboBox()
        tabs = self.parent.DT.tabArray
        
        for i in tabs:
            self.assignToTab_List.addItem(i.tabName)
        grid.addWidget(self.assignToTab_List, 6, 0)
            
        self.ok_Button = QPushButton("Save", self)
        self.ok_Button.clicked.connect(self.ok_Clicked)
        grid.addWidget(self.ok_Button, 7, 0)
        
        self.cancel_Button = QPushButton("Cancel", self)
        self.cancel_Button.clicked.connect(self.cancel_Clicked)
        grid.addWidget(self.cancel_Button, 7 ,1)

        
        grid.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.window.setLayout(grid)
        self.show()
        
        
    def ok_Clicked(self):
        self.parent.DT.appendButton(self.newButtonName_Input.text(), self.assignFunction_List.currentText(), self.assignToTab_List.currentText())
        self.parent.addButtonToMain(self.assignToTab_List.currentText(), self.newButtonName_Input.text())
        self.hide()
        
    def cancel_Clicked(self):
        self.hide()

class NewTabPopup(QMainWindow):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("New Tab")
        self.setGeometry(400,220,400,220)
        
        self.initNewTabUI()
        
    def initNewTabUI(self):
        self.window = QWidget()
        self.setCentralWidget(self.window)
        grid = QGridLayout()
        
        #Define components of window
        self.newTab_Label = QLabel("New Tab:", self)
        grid.addWidget(self.newTab_Label, 0, 0)
        
        self.newTabName_Input = QLineEdit(self)
        self.newTabName_Input.setFixedSize(200,20)
        grid.addWidget(self.newTabName_Input, 1, 0)
        
        self.newDim_Label = QLabel("Dimmensions:", self)
        grid.addWidget(self.newDim_Label, 2, 0)
        
        self.newDimRow_Label = QLabel("Rows:", self)
        grid.addWidget(self.newDimRow_Label, 3, 0)
        
        self.newDimRow_Input = QLineEdit(self)
        self.newDimRow_Input.setFixedSize(50,20)
        self.newDimRow_Input.setValidator(QIntValidator())
        grid.addWidget(self.newDimRow_Input, 3, 1)

        self.newDimColumn_Label = QLabel("Columns:", self)
        grid.addWidget(self.newDimColumn_Label, 4, 0)
        
        self.newDimColumn_Input = QLineEdit(self)
        self.newDimColumn_Input.setFixedSize(50,20)
        self.newDimColumn_Input.setValidator(QIntValidator())
        grid.addWidget(self.newDimColumn_Input, 4, 1)


        self.ok_Button = QPushButton("Save", self)
        self.ok_Button.clicked.connect(self.ok_Clicked)
        grid.addWidget(self.ok_Button, 5, 0)
        
        self.cancel_Button = QPushButton("Cancel", self)
        self.cancel_Button.clicked.connect(self.cancel_Clicked)
        grid.addWidget(self.cancel_Button, 5 ,1)

        grid.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.window.setLayout(grid)
        self.show()

    def ok_Clicked(self):
        print("text")
        self.parent.DT.appendTab(self.newTabName_Input.text(), self.newDimRow_Input.text(), self.newDimColumn_Input.text())
        self.parent.addTabToMain(self.newTabName_Input.text())
        self.hide()
        
    def cancel_Clicked(self):
        self.hide()


class NewFunctionPopup(QMainWindow):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("New Function")
        self.setGeometry(400,220,400,220)
        
        self.initNewFunctionUI()




    def initNewFunctionUI(self):
        self.window = QWidget()
        self.setCentralWidget(self.window)
        grid = QGridLayout()


        #Define components of window
        self.newFunction_Label = QLabel("Function Name:", self)
        grid.addWidget(self.newFunction_Label, 0, 0)
        
        self.newFunctionName_Input = QLineEdit(self)
        self.newFunctionName_Input.setFixedSize(200,20)
        grid.addWidget(self.newFunctionName_Input, 1, 0)

        self.newSequence_Label = QLabel("IR Sequence:", self)
        grid.addWidget(self.newSequence_Label, 2, 0)
        
        self.newSequence_Input = QLineEdit(self)
        self.newSequence_Input.setFixedSize(200,20)
        self.newSequence_Input.setValidator(QIntValidator())
        grid.addWidget(self.newSequence_Input, 3, 0)

        self.newFrequency_Label = QLabel("IR Frequency:", self)
        grid.addWidget(self.newFrequency_Label, 4, 0)
        
        self.newFrequency_Input = QLineEdit(self)
        self.newFrequency_Input.setFixedSize(200,20)
        self.newFrequency_Input.setValidator(QIntValidator())
        grid.addWidget(self.newFrequency_Input, 5, 0)

        self.ok_Button = QPushButton("Save", self)
        self.ok_Button.clicked.connect(self.ok_Clicked)
        grid.addWidget(self.ok_Button, 6, 0)
        
        self.cancel_Button = QPushButton("Cancel", self)
        self.cancel_Button.clicked.connect(self.cancel_Clicked)
        grid.addWidget(self.cancel_Button, 6 ,1)


        grid.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.window.setLayout(grid)
        self.show()


    def ok_Clicked(self):
        print("append function")
        self.parent.DT.appendFunction(self.newFunctionName_Input.text(), self.newSequence_Input.text(), self.newFrequency_Input.text())
        self.hide()
        
    def cancel_Clicked(self):
        self.hide()





