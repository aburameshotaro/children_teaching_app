# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:53:34 2022

@author: user
"""

from ui.variables_ui import Ui_MainWindow
import re

def answersButtonClicked(button):
        button.setText(button.question if button.status else button.answer)
        button.status = (button.status + 1)%2


class VariablesWindow(Ui_MainWindow):
    def retranslateUi(self):
        super().retranslateUi()
        self.lineEditExercise1.setDragEnabled(True)
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.pushButtonGrunwald.clicked.connect(lambda: answersButtonClicked(self.pushButtonGrunwald))
        self.pushButtonPanTadeusz.clicked.connect(lambda: answersButtonClicked(self.pushButtonPanTadeusz))
        self.pushButtonStolicaPolski.clicked.connect(lambda: answersButtonClicked(self.pushButtonStolicaPolski))
        self.pushButtonProgramowanie.clicked.connect(lambda: answersButtonClicked(self.pushButtonProgramowanie))
        
    def firstExerciseExecute(self):
        print('Twoje odpowiedzi: ')
        print('bitwa_pod_grunwaldem_rok = ' + self.pushButtonGrunwald.answer)
        print('pan_tadeusz_autor_nazwisko = ' + self.pushButtonPanTadeusz.answer)
        print('stolica_polski = ' + self.pushButtonStolicaPolski.answer)
        print('czy_programowanie_fajne = ' + self.pushButtonProgramowanie.answer)
        correct = True
        if self.pushButtonGrunwald.answer != "1410":
            print("W którym roku była bitwa pod Grunwaldem?")
            correct = False
        if self.pushButtonPanTadeusz.answer.lower() != "mickiewicz":
            print("Jak miał na nazwisko autor Pana Tadeusza?")
            correct = False
        if self.pushButtonStolicaPolski.answer.lower() != "warszawa":
            print("Polska stolica?")
            correct = False
        if self.pushButtonProgramowanie.answer == "":
            print("Programowanie jest fajne?")
            correct = False
            
        if correct:
            self.labelExercise1.setText("Udało Ci się poprawnie uzupełnić zmienne")
        else:
            self.labelExercise1.setText("Sprawdź konsolę w poszukiwaniu odpowiedzi")

            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        niespodzianka = "Jesteś cudownym programistą! Tak dalej!"
        
        if re.match(r"^print\(.*\)$", answer.replace(" ","")):
            exec(answer)
            self.labelExercise2.setText("Sprawdź w konsoli, czy pojawiła się tam niespodzianka")
        else:
            self.labelExercise2.setText("Spróbuj poprawnie użyć metody print")