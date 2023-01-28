# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:04:00 2023

@author: user
"""

from ui.lists_ui import Ui_Form


class ListsWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.answer_first = ""
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        def square():
            pass
        try:
            oceny = [3,4,6]
            exec("self.answer_first = " + answer)
            if self.answer_first == sum(oceny)/len(oceny):
                self.labelExercise1.setText("Brawo! Udało się.")
                print("Średnia ocen to:", sum(oceny)/len(oceny))
            else:
                self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spróbuj ponownie")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spójrz do konsoli")
            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        try:
            if int(answer) == 7:
                self.labelExercise2.setText("Brawo! Udało się. Spójrz do konsoli")
            else:
                self.labelExercise2.setText("Twoja odpowiedź jest nieprawidłowa. Spróbuj ponownie!")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Twoja odpowiedź jest nieprawidłowa, spójrz do konsoli")