# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:32:21 2020

@author: chris
"""
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import QIcon, QFont

import os.path
import json
import functions
import mainWindow



import sys


tabs = []
buttons = []



App = QCoreApplication.instance()
if App is None:
    App = QApplication(sys.argv)
window = mainWindow.Window()
sys.exit(App.exec())