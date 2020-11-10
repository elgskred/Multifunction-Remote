# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:28:03 2020

@author: chris
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyle, QMainWindow, QPushButton, QToolTip, QMessageBox, QWidget, QAction, QTabWidget,QVBoxLayout, QBoxLayout, QFormLayout, QLabel, QScrollArea, QScrollBar, QInputDialog, QLineEdit, QFileDialog, QGridLayout
from PyQt5.QtCore import QCoreApplication, QRect, pyqtSlot, QTimer, Qt
from PyQt5.QtGui import QIcon, QFont

import os.path
import json
import functions
import westTabs
import settingsWidget

tabs = []
buttons = []

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = 'Multifunction Remote'
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 480
        
        self.DT = functions.DataContainer()
        self.DT.loadFiles()

        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setMinimumSize(QtCore.QSize(800, 480))
        self.setMaximumSize(QtCore.QSize(800, 480))
        
        self.quit = QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
        
        self.show()
        print(self.frameGeometry().width())
        
    def Close_Clicked(self):
        QCoreApplication.instance().quit()
    
    def CloseApp(self):
        reply = QMessageBox.question(self, "Close message", "Exit the application?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    
    def closeEvent(self, event):
        print("Close")
        
        
class MyTableWidget(QWidget):   
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.DT = parent.DT
        self.widgetRefs = []
        self.settings_widgetRefs = []

        
        #Fonts
        boldFont = QFont()
        boldFont.setBold(True)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        

        # Add default tab
        self.mainSettingsTab = QWidget()
        self.tabs.addTab(self.mainSettingsTab, "Settings")
        #Set layout of default tab
        self.mainSettingsTab.layout = QGridLayout(self)
        
        
        # Add user defined tabs, as stored in DataStructure
        tempArray = self.DT.tabArray
        
        for i in tempArray:
            widget = QWidget()
            widget.setObjectName(i.tabName)
            grid = QGridLayout()
            widget.setLayout(grid)
            self.tabs.insertTab(0, widget, i.tabName)
            self.widgetRefs.append(widget)
            
            
            
        #Testing
        # print(self.tabs.count())
        # print(self.tabs.indexOf(self.widgetRefs[0]))
        # print(self.widgetRefs[0].objectName())
        # print(self.widgetRefs[0].frameGeometry().width())
        # print(self.widgetRefs[0].frameGeometry().height())
        
        

        
        
        #Add user defined buttons to user defined tabs
        buttonArray = self.DT.buttonArray
        for ref in self.widgetRefs:
            print(ref.objectName())
            columnNums = self.DT.getColumns(ref.objectName())
            print(columnNums)
            columnNums = int(columnNums)
            print(type(columnNums))
            Ccnt = 0
            Rcnt = 0
            for btn in buttonArray:
                if (ref.objectName() == btn.onTab):
                    #print(ref.layout())
                    grid = ref.layout()
                    newButton = QPushButton(btn.buttonName)
                    newButton.setObjectName(btn.buttonName)
                    newButton.clicked.connect(self.testFunction)
                    if (Ccnt > columnNums):
                        Ccnt = 0
                        Rcnt + 1                        
                    grid.addWidget(newButton, Ccnt, Rcnt)
                    grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                    ref.setLayout(grid)
                    Ccnt + 1

        # print(self.widgetRefs[0].children())
        # test = self.widgetRefs[0].children()
        # tt = test[0]
        # print(len(tt))
        # print(self.widgetRefs[0].findChildren(QtWidgets.QPushButton))
    
        # Set size on tab buttons
        self.tabs.setStyleSheet(""
        "QTabBar::tab:selected {height: 30px; width: 82px;}"
        "QTabBar::tab:!selected { height: 30px; width: 82px;}"                      
        "");

       
        
        #Apply settings to default tab
        self.settingTab = westTabs.TabWidget()
        self.settingTab_setting = settingsWidget.SettingWidget(self)
        self.settingTab_tv = QWidget()
        
        # Set stylesheet on tab buttons
        self.settingTab.setStyleSheet(""
        "QTabBar::tab:selected {height: 82px; width: 30px;}"
        "QTabBar::tab:!selected { height: 82px; width: 30px;}"                      
        "");

        #Add default setting tab to settings window
        self.settingTab.addTab(self.settingTab_setting, QIcon(QApplication.style().standardIcon(QStyle.SP_DriveNetIcon)), "Settings")
        
        
        # Add user defined tabs, as stored in DataStructure to settings window
        for i in tempArray:
            settings_widget = QWidget()
            settings_widget.setObjectName(i.tabName)
            grid = QGridLayout()
            settings_widget.setLayout(grid)
            self.settingTab.insertTab(1, settings_widget, QIcon(QApplication.style().standardIcon(QStyle.SP_DriveNetIcon)), i.tabName)
            self.settings_widgetRefs.append(settings_widget)
        
        for ref in self.settings_widgetRefs:
            for btn in buttonArray:
                if (ref.objectName() == btn.onTab):
                    grid = ref.layout()
                    newButton = QPushButton(btn.buttonName)
                    newButton.setObjectName(btn.buttonName)
                    newButton.clicked.connect(self.testFunction)
                    grid.addWidget(newButton)
                    grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                    ref.setLayout(grid)
        
        
        #Add settingsTab to mainSettingsTab
        self.mainSettingsTab.layout.addWidget(self.settingTab, 0, 0)

        #Apply layout to mainSettingsTab
        self.mainSettingsTab.setLayout(self.mainSettingsTab.layout)

        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    @pyqtSlot()
    def on_click(self):
        print("Button click")
        
    def test_update(self):
        print("Updated!!")
        
    def testFunction(self):
        print(self.sender().objectName())
        
    def appendTabs(self, name):
        self.tabs.insertTab(0, QWidget(), name)
        self.settingTab.insertTab(1, QWidget(), QIcon(QApplication.style().standardIcon(QStyle.SP_DriveNetIcon)), name)
        
    def appendButton(self, tab, name):
        for ref in self.widgetRefs:
            if (ref.objectName() == tab):
                grid = ref.layout()
                newButton = QPushButton(name)
                newButton.setObjectName(name)
                newButton.clicked.connect(self.testFunction)
                grid.addWidget(newButton)
                grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
                ref.setLayout(grid)
        
        
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()

