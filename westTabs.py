# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:32:01 2020

@author: chris
"""

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