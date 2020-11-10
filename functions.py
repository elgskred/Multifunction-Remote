# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:05:46 2020

@author: chris
"""

import os.path
import json
import pickle


# def loadTabs():
#     #Checks config file for Factorio base folder and users mod folder
#     file_name = 'tabs.json'
#     try:
#         file = open(file_name, 'r')
#         tabs = json.load(file)
#         file.close()
#     except IOError:
#         file = open(file_name, 'w')
#         tabs = []
#         file.write(json.dumps(tabs))
#         file.close()
    
#     return(tabs)


# def loadButtons():
#     #Checks config file for Factorio base folder and users mod folder
#     file_name = 'buttons.json'
#     try:
#         file = open(file_name, 'r')
#         buttons = json.load(file)
#         file.close()
#     except IOError:
#         file = open(file_name, 'w')
#         buttons = []
#         file.write(json.dumps(buttons))
#         file.close()
    
#     return(buttons)


# def storeTabs(tabs):
#     file_name = 'tabs.json'
#     file = open(file_name, 'w')
#     file.write(json.dumps(tabs))
#     file.close()
        
    
# def storeButtons(buttons):
#     file_name = 'buttons.json'
#     file = open(file_name, 'w')
#     file.write(json.dumps(buttons))
#     file.close()
    
    

    
class DataContainer():
    def __init__(self):
        self.tabArray = []
        self.buttonArray = []
        self.functionsArray = []
        self.createFiles()

        
    def createFiles(self):
        if (os.path.isfile('tabs.pkl') == False):
            self.storeTabs(self.tabArray)
        if (os.path.isfile('buttons.pkl') == False):
            self.storeButtons(self.tabArray)
        if (os.path.isfile('functions.pkl') == False):
            self.storeFunctions(self.tabArray)
            
    def loadFiles(self):
        self.tabArray = self.loadTabs()
        self.buttonArray = self.loadButtons()
        self.functionsArray = self.loadFunctions()
        
    def storeFiles(self):
        self.storeTabs(self.tabArray)
        self.storeButtons(self.buttonArray)
        self.storeFunctions(self.functionsArray)
        
    def appendTab(self, tabName, rows, columns):
        self.tab = NewTab(tabName, rows, columns)
        self.tabArray = self.loadTabs()
        print(self.tabArray)
        self.tabArray.append(self.tab)
        print(self.tabArray)
        print(self.tab.tabName)
        self.storeTabs(self.tabArray)
        
    def appendButton(self, buttonName, function, toTab):
        self.button = NewButton(buttonName, function, toTab)
        self.buttonArray = self.loadButtons()
        print(self.buttonArray)
        self.buttonArray.append(self.button)
        print(self.buttonArray)
        print(self.button.buttonName)
        self.storeButtons(self.buttonArray)
        
        
    def appendFunction(self, functionName, sequence, frequency):
        self.function = NewFunction(functionName, sequence, frequency)
        self.functionArray = self.loadFunctions()
        print(self.functionArray)
        self.functionArray.append(self.function)
        print(self.functionArray)
        print(self.function.functionName)
        self.storeFunctions(self.functionArray)
        self.functionsArray = self.loadFunctions()
        
    def storeTabs(self, obj):
        file_name = 'tabs.pkl'
        with open(file_name, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
            
    def loadTabs(self):
        file_name = 'tabs.pkl'
        with open(file_name, 'rb') as input:
            arr = pickle.load(input)
            return(arr)

        
    def storeButtons(self, obj):
        file_name = 'buttons.pkl'
        with open(file_name, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
            
    def loadButtons(self):
        file_name = 'buttons.pkl'
        with open(file_name, 'rb') as input:
            arr = pickle.load(input)
            return(arr)
    
    def storeFunctions(self, obj):
        file_name = 'functions.pkl'
        with open(file_name, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
            
    def loadFunctions(self):
        file_name = 'functions.pkl'
        with open(file_name, 'rb') as input:
            arr = pickle.load(input)
            return(arr)
      
    def getColumns(self, name):
        for tab in self.tabArray:
            if (tab.tabName == name):
                return(tab.columns)
      

    def testing(self):
        print("testing")
    
        
    
        


class NewFunction():
    def __init__(self, functionName, sequence, freqency):
        self.functionName = functionName
        self.sequence = sequence
        self.freqency = freqency
        
        

class NewTab():
    def __init__(self, tabName, rows, columns):
        self.tabName = tabName
        self.tabPosition = 0
        self.buttonList = []
        self.rows = rows
        self.columns = columns
    
    def addTab():
        print("add Tab to list")
        
        
        
class NewButton():
    def __init__(self, buttonName, function, onTab):
        self.buttonName = buttonName
        self.function = function
        self.onTab = onTab
    
    def addButton():
        print("add button to list")     
        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        