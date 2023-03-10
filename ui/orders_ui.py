# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(641, 455)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidgetBasicFunctions = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetBasicFunctions.setObjectName("tabWidgetBasicFunctions")
        self.tab_welcome = QtWidgets.QWidget()
        self.tab_welcome.setObjectName("tab_welcome")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_welcome)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TextEditWelcome = QtWidgets.QPlainTextEdit(self.tab_welcome)
        self.TextEditWelcome.setObjectName("TextEditWelcome")
        self.gridLayout_2.addWidget(self.TextEditWelcome, 2, 0, 1, 1)
        self.WelcomeImg = QtWidgets.QLabel(self.tab_welcome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WelcomeImg.sizePolicy().hasHeightForWidth())
        self.WelcomeImg.setSizePolicy(sizePolicy)
        self.WelcomeImg.setText("")
        self.WelcomeImg.setPixmap(QtGui.QPixmap(":/Orders/fantastyczne-zwierzeta-i-jak-je-znalezc-recenzja-filmu-online-5.jpg"))
        self.WelcomeImg.setObjectName("WelcomeImg")
        self.gridLayout_2.addWidget(self.WelcomeImg, 5, 0, 1, 1)
        self.tabWidgetBasicFunctions.addTab(self.tab_welcome, "")
        self.tab_structure = QtWidgets.QWidget()
        self.tab_structure.setObjectName("tab_structure")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_structure)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.StructureImg = QtWidgets.QLabel(self.tab_structure)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StructureImg.sizePolicy().hasHeightForWidth())
        self.StructureImg.setSizePolicy(sizePolicy)
        self.StructureImg.setMinimumSize(QtCore.QSize(0, 200))
        self.StructureImg.setMaximumSize(QtCore.QSize(500, 200))
        self.StructureImg.setText("")
        self.StructureImg.setPixmap(QtGui.QPixmap(":/Orders/Katy_tryg.png"))
        self.StructureImg.setObjectName("StructureImg")
        self.gridLayout_3.addWidget(self.StructureImg, 1, 0, 1, 1)
        self.TextEditStructure = QtWidgets.QPlainTextEdit(self.tab_structure)
        self.TextEditStructure.setObjectName("TextEditStructure")
        self.gridLayout_3.addWidget(self.TextEditStructure, 0, 0, 1, 1)
        self.tabWidgetBasicFunctions.addTab(self.tab_structure, "")
        self.tab_print = QtWidgets.QWidget()
        self.tab_print.setObjectName("tab_print")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_print)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TextEditPrint = QtWidgets.QPlainTextEdit(self.tab_print)
        self.TextEditPrint.setMinimumSize(QtCore.QSize(0, 0))
        self.TextEditPrint.setObjectName("TextEditPrint")
        self.gridLayout_4.addWidget(self.TextEditPrint, 0, 0, 1, 1)
        self.PrintImg = QtWidgets.QLabel(self.tab_print)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrintImg.sizePolicy().hasHeightForWidth())
        self.PrintImg.setSizePolicy(sizePolicy)
        self.PrintImg.setMinimumSize(QtCore.QSize(0, 0))
        self.PrintImg.setMaximumSize(QtCore.QSize(16777215, 250))
        self.PrintImg.setText("")
        self.PrintImg.setPixmap(QtGui.QPixmap(":/Orders/orders_print.gif"))
        self.PrintImg.setObjectName("PrintImg")
        self.gridLayout_4.addWidget(self.PrintImg, 1, 0, 1, 1)
        self.tabWidgetBasicFunctions.addTab(self.tab_print, "")
        self.tab_exercise1 = QtWidgets.QWidget()
        self.tab_exercise1.setObjectName("tab_exercise1")
        self.lineEditExercise1 = QtWidgets.QLineEdit(self.tab_exercise1)
        self.lineEditExercise1.setGeometry(QtCore.QRect(140, 190, 311, 20))
        self.lineEditExercise1.setObjectName("lineEditExercise1")
        self.pushButtonExercise1 = QtWidgets.QPushButton(self.tab_exercise1)
        self.pushButtonExercise1.setGeometry(QtCore.QRect(220, 230, 131, 23))
        self.pushButtonExercise1.setObjectName("pushButtonExercise1")
        self.TextEditExercise1 = QtWidgets.QPlainTextEdit(self.tab_exercise1)
        self.TextEditExercise1.setGeometry(QtCore.QRect(140, 90, 311, 71))
        self.TextEditExercise1.setObjectName("TextEditExercise1")
        self.labelExercise1 = QtWidgets.QLabel(self.tab_exercise1)
        self.labelExercise1.setGeometry(QtCore.QRect(100, 290, 47, 13))
        self.labelExercise1.setText("")
        self.labelExercise1.setObjectName("labelExercise1")
        self.tabWidgetBasicFunctions.addTab(self.tab_exercise1, "")
        self.tab_operators = QtWidgets.QWidget()
        self.tab_operators.setObjectName("tab_operators")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_operators)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.plainTextAdding = QtWidgets.QPlainTextEdit(self.tab_operators)
        self.plainTextAdding.setObjectName("plainTextAdding")
        self.gridLayout_6.addWidget(self.plainTextAdding, 0, 0, 1, 1)
        self.AddingImg = QtWidgets.QLabel(self.tab_operators)
        self.AddingImg.setMaximumSize(QtCore.QSize(16777215, 230))
        self.AddingImg.setText("")
        self.AddingImg.setPixmap(QtGui.QPixmap(":/Orders/adding.jpg"))
        self.AddingImg.setObjectName("AddingImg")
        self.gridLayout_6.addWidget(self.AddingImg, 1, 0, 1, 1)
        self.tabWidgetBasicFunctions.addTab(self.tab_operators, "")
        self.tab_exercise2 = QtWidgets.QWidget()
        self.tab_exercise2.setObjectName("tab_exercise2")
        self.pushButtonExercise2 = QtWidgets.QPushButton(self.tab_exercise2)
        self.pushButtonExercise2.setGeometry(QtCore.QRect(240, 210, 131, 23))
        self.pushButtonExercise2.setObjectName("pushButtonExercise2")
        self.lineEditExercise2 = QtWidgets.QLineEdit(self.tab_exercise2)
        self.lineEditExercise2.setGeometry(QtCore.QRect(160, 170, 311, 20))
        self.lineEditExercise2.setObjectName("lineEditExercise2")
        self.TextEditExercise2 = QtWidgets.QPlainTextEdit(self.tab_exercise2)
        self.TextEditExercise2.setGeometry(QtCore.QRect(140, 100, 351, 41))
        self.TextEditExercise2.setObjectName("TextEditExercise2")
        self.labelExercise2 = QtWidgets.QLabel(self.tab_exercise2, wordWrap=True)
        self.labelExercise2.setGeometry(QtCore.QRect(100, 260, 250, 13))
        self.labelExercise2.setText("")
        self.labelExercise2.setObjectName("labelExercise2")
        self.labelExercise2_2 = QtWidgets.QLabel(self.tab_exercise2)
        self.labelExercise2_2.setGeometry(QtCore.QRect(100, 280, 250, 13))
        self.labelExercise2_2.setText("")
        self.labelExercise2_2.setObjectName("labelExercise2_2")
        self.tabWidgetBasicFunctions.addTab(self.tab_exercise2, "")
        self.horizontalLayout.addWidget(self.tabWidgetBasicFunctions)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.tabWidgetBasicFunctions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Podstawowe funkcje"))
        self.TextEditWelcome.setPlainText(_translate("MainWindow", "W tym rozdziale poznamy proste funkcje. W końcu uda nam się zmusić komputer do wykonania naszych rozkazów. Najczęściej opisów funkcji szukamy w dokumentacji, w internecie.\n"
"Zanim to jednak zrobimy musimy poznać wygląd funkcji abyśmy mogli je w ogóle rozpoznać.\n"
"A zatem zapraszam:\n"
"Magiczne funkcje i jak je znaleźć ->"))
        self.tabWidgetBasicFunctions.setTabText(self.tabWidgetBasicFunctions.indexOf(self.tab_welcome), _translate("MainWindow", "Proste rozkazy!"))
        self.TextEditStructure.setPlainText(_translate("MainWindow", "Funkcja składa się z dwóch części:\n"
"nazwa_funkcji( parametry)\n"
"nazwa_funkcji - to unikalna nazwa naszej komendy. To coś jakby nauczyć psa sztuczki \"aport\". Pies dokładnie wie, co ma zrobić, gdy usłyszy taką komendę.\n"
"parametry - to dodatkowe informacje, które możemy przekazać danej funkcji. Można to porównać do danych, które nauczycielka matematyki nam podaje zanim zaczniemy obliczenia. Żeby policzyć pole trójkąta musimy wiedzieć, jaka jest jego podstawa i wysokość.\n"
"Dlatego też wywołanie funkcji do liczenia pola trójkąta mogłaby wyglądać tak:\n"
"pole_trojkata(podstawa, wysokosc)"))
        self.tabWidgetBasicFunctions.setTabText(self.tabWidgetBasicFunctions.indexOf(self.tab_structure), _translate("MainWindow", "Struktura funkcji"))
        self.TextEditPrint.setPlainText(_translate("MainWindow", "Pierwszą i najprostszą funkcją jaką poznamy będzie funkcja print. Służy ona do wyświetlania informacji w konsoli. Konsolę już poznaliśmy. To ten czarny kwadrat w tle ;) \n"
"Pierwszy program, który trzeba napisać jako programista, to przywitanie świata. Komenda, która wykona właśnie to, będzie wygląć następująco:\n"
"print(\"Witaj świecie\")\n"
"Ważne są tutaj podwójne cudzysłowy, które oznaczają, że mamy do czynienia z tekstem. I w sumie ta jedna linijka to wszystko co jest nam potrzebne aby wyświetlić tekst na ekranie konsoli. \n"
"print - to nazwa funkcji\n"
"\"Witaj świecie\" - to parametr funkcji (zauważmy, że tekst jest w cudzysłowiu! - to tak jakbyśmy cytowali czyjeś słowa, w tym przypadku komputera)"))
        self.tabWidgetBasicFunctions.setTabText(self.tabWidgetBasicFunctions.indexOf(self.tab_print), _translate("MainWindow", "print"))
        self.lineEditExercise1.setPlaceholderText(_translate("MainWindow", "Wpisz rozkaz"))
        self.pushButtonExercise1.setText(_translate("MainWindow", "Wyślij rozwiązanie"))
        self.TextEditExercise1.setPlainText(_translate("MainWindow", "Pierwsze zadanie!\n"
"To nie może być nic trudnego. \n"
"A zatem spróbujmy wypisać coś do konsoli!\n"
"Poniżej mamy miejsce na wpisanie odpowiedzi."))
        self.tabWidgetBasicFunctions.setTabText(self.tabWidgetBasicFunctions.indexOf(self.tab_exercise1), _translate("MainWindow", "Zadanie 1"))
        self.plainTextAdding.setPlainText(_translate("MainWindow", "Jak to kiedyś ktoś powiedział: \"Komputer to taki bardziej rozbudowany kalkulator\". Jest w tym sporo prawdy. Komputer potrafi głównie liczyć. Dla jednych będzie to tylko liczenie, a dla drugich aż liczenie.\n"
"Żeby i my potrafiliśmy rozkazać komputerowi liczyć, przekazuje wam znaki, których możemy używać. \n"
"Pamiętajcie, że przy większych działaniach obowiązuje kolejność wykonywania działań (pierwsze nawiasy).\n"
"+ (dodawanie)\n"
"- (odejmowanie)\n"
"* (mnożenie)\n"
"/ (dzielenie)\n"
"% (reszta z dzielenia)\n"
"** (potęgowanie)"))
        self.tabWidgetBasicFunctions.setTabText(self.tabWidgetBasicFunctions.indexOf(self.tab_operators), _translate("MainWindow", "Prosta matematyka"))
        self.pushButtonExercise2.setText(_translate("MainWindow", "Oblicz"))
        self.lineEditExercise2.setPlaceholderText(_translate("MainWindow", "Wpisz działanie"))
        self.TextEditExercise2.setPlainText(_translate("MainWindow", "Drugie zadanie!\n"
"Spróbuj wykonać kilka prostych działań, a ich wynik zobacz poniżej."))
        self.tabWidgetBasicFunctions.setTabText(self.tabWidgetBasicFunctions.indexOf(self.tab_exercise2), _translate("MainWindow", "Zadanie 2"))
import obrazki.obrazki_introduction
import obrazki.obrazki_orders


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
