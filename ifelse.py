# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:36:14 2023

@author: user
"""

from ui.ifelse_ui import Ui_Form


class IfElseWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.answer_for_second = ""
        
    def firstExerciseExecute(self):
        if self.radioButton_4.isChecked():
            self.labelExercise1.setText("Brawo! Udało się.")
        else:
            self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spróbuj ponownie")
            
            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        command = "self.answer_for_second=" + answer
        try:
            exec(command)
            if self.answer_for_second == 8:
                self.labelExercise2.setText("Brawo! Udało się.")
            else:
                self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie.")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, sprawdź konsolę.")