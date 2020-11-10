from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyle, QMainWindow, QPushButton, QToolTip, QMessageBox, QWidget, QAction, QTabWidget,QVBoxLayout, QBoxLayout, QFormLayout, QLabel, QScrollArea, QScrollBar, QInputDialog, QLineEdit, QFileDialog, QGridLayout
from PyQt5.QtCore import QCoreApplication, QRect, pyqtSlot, QTimer, Qt
from PyQt5.QtGui import QIcon, QFont

import os.path
import json
import functions



import sys


tabs = []
buttons = []

class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()

class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)     



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = 'Multifunction Remote'
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 480

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
        
    def Close_Clicked(self):
        QCoreApplication.instance().quit()
    
    def CloseApp(self):
        reply = QMessageBox.question(self, "Close message", "Exit the application?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    
    def closeEvent(self, event):
        functions.storeTabs(tabs)
        print("Close")
        
class SettingWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        grid = QGridLayout()
        self.parent = parent
        
        
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
        
        #self.setLayout(self.layout)
        
    def AddTab(self):
        print("addTab pressed")
        tabs.append(NewTab("Testing"))
            
    def AddButton(self):
        print("addButton pressed")
        print(tabs)
            
    def LearnFunction(self):
        print("learnFunction pressed")
        self.parent.test_update()
        

class NewTab():
    def __init__(self, name):
        self.tabName = name
        self.tabPosition = 0
        self.buttonList = []
    
    def addButton():
        print("add button to list")
        

class RemoteFunctions():
    def __init__(self):
        self.sequence = "000000"
        self.functionName = ""
        
    def setName(name):
        functionName = name
        
    def setSequence(seq):
        sequence = ""



class MyTableWidget(QWidget):   
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        
        #Fonts
        boldFont = QFont()
        boldFont.setBold(True)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.mainSettingsTab = QWidget()
        
        # Set size on tab buttons
        self.tabs.setStyleSheet(""
        "QTabBar::tab:selected {height: 30px; width: 82px;}"
        "QTabBar::tab:!selected { height: 30px; width: 82px;}"                      
        "");


        # Add default tabs
        self.tabs.addTab(self.mainSettingsTab, "Settings")
        
        tempArray = ["Testing22", "Kake", "Fjott"]
        
        for i in tempArray:
            self.tabs.insertTab(0, QWidget(), i)

        
        #Create third tab
        self.mainSettingsTab.layout = QGridLayout(self)

        
        self.settingTab = TabWidget()
        self.settingTab_setting = SettingWidget(self)
        self.settingTab_tv = QWidget()
        
        # Set stylesheet on tab buttons
        self.settingTab.setStyleSheet(""
        "QTabBar::tab:selected {height: 82px; width: 30px;}"
        "QTabBar::tab:!selected { height: 82px; width: 30px;}"                      
        "");

        
        #Add tab with text and icon
        self.settingTab.addTab(self.settingTab_setting, QIcon(QApplication.style().standardIcon(QStyle.SP_DriveNetIcon)), "Settings")
        
        
        #Add tab with text
        #self.settingTab.addTab(self.settingTab_setting,"Settings")
        
        
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

        
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()





#App = QApplication(sys.argv)
App = QCoreApplication.instance()
if App is None:
    App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())