# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:17:29 2023

@author: user
"""

from ui.functions_ui import Ui_Form
import re

def draw_tree(levels):
    star_counter = 1
    for i in range(levels):
        print(("*" * star_counter).center(levels*2) )
        star_counter += 2

class FunctionsWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.answer_first = ""
        
    def firstExerciseExecute(self):
        answer = self.plainTextEditExercise1.toPlainText().strip()
        def square():
            pass
        try:
            exec(answer + "\nself.answer_first = square(6)")
            if self.answer_first == 36:
                self.labelExercise1.setText("Brawo! Udało się.")
            else:
                self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spróbuj ponownie")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spójrz do konsoli")
            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        try:
            if re.match(r"^draw_tree\([0-9]+\)$", answer.replace(" ","")):
                exec(answer)
                self.labelExercise2.setText("Brawo! Udało się. Spójrz do konsoli")
            else:
                self.labelExercise2.setText("Twoja odpowiedź jest nieprawidłowa. Spróbuj ponownie!")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Twoja odpowiedź jest nieprawidłowa, spójrz do konsoli")
          