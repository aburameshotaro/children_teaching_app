# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:53:00 2022

@author: user
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_page_ui import Ui_MainWindow
from introduction import IntroductionWindow
from orders import OrdersWindow
from variables import VariablesWindow
from strings import StringsWindow
from classes import ClassesWindow
from exceptions import ExceptionsWindow
from files import FilesWindow
from functions import FunctionsWindow
from ifelse import IfElseWindow
from userInput import InputWindow
from lists import ListsWindow

class MainPageWindow(Ui_MainWindow):
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.introduction_window = IntroductionWindow()
        self.orders_window = OrdersWindow()
        self.variables_window = VariablesWindow()
        self.strings_window = StringsWindow()
        self.files_window = FilesWindow()
        self.class_window = ClassesWindow()
        self.ifelse_window = IfElseWindow()
        self.input_window = InputWindow()
        self.functions_window = FunctionsWindow()
        self.lists_window = ListsWindow()
        self.exceptions_window = ExceptionsWindow()
        self.pushButtonIntroduction.clicked.connect(self.introduction_clicked)
        self.pushButtonBasics.clicked.connect(self.orders_clicked)
        self.pushButtonVariables.clicked.connect(self.variables_clicked)
        self.pushButtonStringFunctions.clicked.connect(self.strings_clicked)
        self.pushButtonIfElse.clicked.connect(self.if_else_clicked)
        self.pushButtonUserCommunication.clicked.connect(self.input_clicked)
        self.pushButtonFunction.clicked.connect(self.functions_clicked)
        self.pushButtonLists.clicked.connect(self.lists_clicked)
        self.pushButtonFile.clicked.connect(self.files_clicked)
        self.pushButtonClass.clicked.connect(self.classes_clicked)
        self.pushButtonError.clicked.connect(self.error_clicked)
        
         
    def introduction_clicked(self):
        self.introduction_window.setupUi()
        self.introduction_window.show()

    def orders_clicked(self):
        self.orders_window.setupUi()
        self.orders_window.show()
        
    def variables_clicked(self):
        self.variables_window.setupUi()
        self.variables_window.show()
    
    def strings_clicked(self):
        self.strings_window.setupUi()
        self.strings_window.show()
    
    def if_else_clicked(self):
        self.ifelse_window.setupUi()
        self.ifelse_window.show()
        
    def input_clicked(self):
        self.input_window.setupUi()
        self.input_window.show()
        
    def functions_clicked(self):
        self.functions_window.setupUi()
        self.functions_window.show()
        
    def lists_clicked(self):
        self.lists_window.setupUi()
        self.lists_window.show()
    
    def files_clicked(self):
        self.files_window.setupUi()
        self.files_window.show()
        
    def classes_clicked(self):
        self.class_window.setupUi()
        self.class_window.show()
        
    def error_clicked(self):
        self.exceptions_window.setupUi()
        self.exceptions_window.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainPageWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())