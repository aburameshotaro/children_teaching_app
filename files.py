# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:00:28 2023

@author: user
"""

from ui.files_ui import Ui_Form


class FilesWindow(Ui_Form):
    def retranslateUi(self):
        super().retranslateUi()
        
        self.pushButtonExercise1.clicked.connect(self.firstExerciseExecute)
        
    def firstExerciseExecute(self):
        answer = self.lineEditExercise1.text().strip()
        command = """with open('Zadanie_Z_Plikow.txt', 'w') as f:
    """ + answer
        
        try:
            exec(command)
            self.labelExercise1.setText("Sprawdź czy w folderze z naszym programem utworzył się plik")
        except Exception as e:
            print(str(type(e).__name__) +": "+ str(e))
            self.labelExercise1.setText("Sprawdź czy w konsoli, co poszło nie tak.")
            