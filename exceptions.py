# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:53:25 2023

@author: user
"""

from ui.exceptions_ui import Ui_Form

def division(second_number):
    try:
        liczba1 = 100
        liczba2 = second_number
        print(liczba1/liczba2)
        return liczba1/liczba2
    except TypeError:
        print('Dzielenie wykonywane jest na liczbach')
        return "TypeError"
    except ZeroDivisionError:
        print('Pamiętaj cholero nie dziel przez zero')
        return "ZeroDivisionError"

class ExceptionsWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        exec("division("+ answer+")")
        self.labelExercise1.setText("Sprawdź wynik swoich działań w konsoli")