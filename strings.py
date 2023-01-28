# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:53:53 2022

@author: user
"""

from ui.strings_ui import Ui_Form


class StringsWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.first_answer = ''
        self.second_answer = ''
        
    def firstExerciseExecute(self):
        quote = "Mylisz niebo z gwiazdami odbitymi nocą na powierzchni stawu."
        answer = self.lineEditExercise1.text().strip()
        command = "self.first_answer = " + answer
        try:
            if answer.startswith("quote"):
                exec(command)
                if self.first_answer == "niebo":
                    self.labelExercise1.setText("Brawo! Udało się.")
                else:
                    self.labelExercise1.setText("Sprawdź w konsoli otrzymany przez ciebie tekst")
                    print(self.first_answer)
            else:
                self.labelExercise1.setText("Twoja odpowiedź powinna zaczynać się od nazwy zmiennej")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie.")
            
    def secondExerciseExecute(self):
        answer = self.lineEdit.text().strip()
        try:
            command = "self.answer_for_second = " + answer
            exec(command)
            if self.answer_for_second == 12:
                self.labelExercise2.setText("Brawo! Udało się.")
            else:
                self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie.")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie.")