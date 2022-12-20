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

class MainPageWindow(Ui_MainWindow):
    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        self.introduction_window = IntroductionWindow()
        self.orders_window = OrdersWindow()
        self.variables_window = VariablesWindow()
        self.strings_window = StringsWindow()
        self.pushButtonIntroduction.clicked.connect(self.introduction_clicked)
        self.pushButtonBasics.clicked.connect(self.orders_clicked)
        self.pushButtonVariables.clicked.connect(self.variables_clicked)
        self.pushButtonStringFunctions.clicked.connect(self.strings_clicked)
        
         
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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainPageWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())