# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:04:20 2023

@author: user
"""
from ui.classes_ui import Ui_Form

class Student():
    def __init__(self, name):
        self.name = name
        self.marks = []

    def addMark(self, mark):
        self.marks.append(mark)

    def changeLastMark(self,mark):
        self.marks[-1] = mark

    def calculateAverage(self):
        if len(self.marks> 0):
            return sum(self.marks)/len(self.marks)
        else:
            return 1


class ClassesWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        self.pushButtonExercise2.clicked.connect(self.secondExerciseExecute)
        self.student = ''
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        if (answer == "class"):
            self.labelExercise1.setText("Brawo! Udało się.")
        else:
            self.labelExercise1.setText("Twoja odpowiedź jest nieprawidłowa, spróbuj ponownie")
            
            
    def secondExerciseExecute(self):
        answer = self.lineEditExercise2.text().strip()
        
        command = "self.student = " + answer 
        try:
            exec(command)
            if self.student.name == "Anna":
                self.labelExercise2.setText("Brawo! Udało się.")
            else:
                self.labelExercise2.setText("Nie udało się. Spróbuj ponownie")
                
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise2.setText("Nie udało się. Wynik w konsoli.")