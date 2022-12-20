# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:53:17 2022

@author: user
"""

from ui.orders_ui import Ui_MainWindow
import re

class OrdersWindow(Ui_MainWindow):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        self.labelExercise1.resize(500,20)
        if re.match(r"^print\('[ -~]*'\)$", answer.replace(" ","")) or re.match(r"^print\(\"[ -~]*\"\)$", answer.replace(" ","")):
            exec(answer)
            self.tab_exercise1.setStyleSheet('''
                                    QTabBar::tab {background: green;}
                                    ''')
            self.labelExercise1.setText("Brawo! Udało się. Zobacz rezultat swojego kodu w konsoli(to czarne ustrojstwo za programem)")
        else:
            self.labelExercise1.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie")