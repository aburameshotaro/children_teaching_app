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
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.answer_for_second = ""
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        self.labelExercise1.resize(500,20)
        if re.match(r"^print\('[0-9a-zA-ZąęóśżźćńłĘÓŁŚĄŻŹĆŃ()!@#$%^&\*;:\{\}\[\].,<>/?]*'\)$", answer.replace(" ","")) or re.match(r"^print\(\"[0-9a-zA-ZąęóśżźćńłĘÓŁŚĄŻŹĆŃ()!@#$%^&\*;:\{\}\[\].,<>/?]*\"\)$", answer.replace(" ","")):
            exec(answer)
            self.labelExercise1.setText("Brawo! Udało się. Zobacz rezultat swojego kodu w konsoli(to czarne ustrojstwo za programem)")
        else:
            self.labelExercise1.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie")
            
            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        command = "self.answer_for_second=" + answer
        self.labelExercise2.resize(500,20)
        try:
            exec(command)
            if type(self.answer_for_second) == int or type(self.answer_for_second)==float:
                self.labelExercise2.setText("Wynik twojego działania to: " +str(self.answer_for_second))
                self.labelExercise2_2.setText("")
            else:
                self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie.")
                self.labelExercise2_2.setText("W konsoli mogą być dodatkowe informacje")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Twoja odpowiedź wydaje się być nieprawidłowa, spróbuj ponownie.")
            self.labelExercise2_2.setText("W konsoli mogą być dodatkowe informacje")
        
        