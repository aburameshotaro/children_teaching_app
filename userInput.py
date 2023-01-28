# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:55:59 2023

@author: user
"""

from ui.input_ui import Ui_Form


class InputWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        if (answer == "34"):
            self.labelExercise1.setText("Brawo! Udało się.")
        else:
            self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spróbuj ponownie")
            
            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        command = "print(int(" + answer +") + 10)"
        try:
            exec(command)
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Brawo! Udało się. Spójrz do konsoli")
        else:
            self.labelExercise2.setText("Nie udało się. Wynik w konsoli.")
            