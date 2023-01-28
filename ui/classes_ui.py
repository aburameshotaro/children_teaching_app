# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'class.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(654, 494)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidgetClass = QtWidgets.QTabWidget(self)
        self.tabWidgetClass.setObjectName("tabWidgetClass")
        self.tab_welcome = QtWidgets.QWidget()
        self.tab_welcome.setObjectName("tab_welcome")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_welcome)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TextEditWelcome = QtWidgets.QPlainTextEdit(self.tab_welcome)
        self.TextEditWelcome.setObjectName("TextEditWelcome")
        self.gridLayout_2.addWidget(self.TextEditWelcome, 2, 0, 1, 1)
        self.WelcomeImg = QtWidgets.QLabel(self.tab_welcome)
        self.WelcomeImg.setText("")
        self.WelcomeImg.setPixmap(QtGui.QPixmap(":/classes/dog.PNG"))
        self.WelcomeImg.setObjectName("WelcomeImg")
        self.gridLayout_2.addWidget(self.WelcomeImg, 3, 0, 1, 1)
        self.tabWidgetClass.addTab(self.tab_welcome, "")
        self.tab_class = QtWidgets.QWidget()
        self.tab_class.setObjectName("tab_class")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_class)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.IfImg = QtWidgets.QLabel(self.tab_class)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IfImg.sizePolicy().hasHeightForWidth())
        self.IfImg.setSizePolicy(sizePolicy)
        self.IfImg.setMinimumSize(QtCore.QSize(0, 200))
        self.IfImg.setMaximumSize(QtCore.QSize(600, 220))
        self.IfImg.setText("")
        self.IfImg.setPixmap(QtGui.QPixmap(":/classes/class_keyword.jpg"))
        self.IfImg.setObjectName("IfImg")
        self.gridLayout_3.addWidget(self.IfImg, 1, 0, 1, 1)
        self.TextEditIf = QtWidgets.QPlainTextEdit(self.tab_class)
        self.TextEditIf.setMinimumSize(QtCore.QSize(0, 188))
        self.TextEditIf.setObjectName("TextEditIf")
        self.gridLayout_3.addWidget(self.TextEditIf, 0, 0, 1, 1)
        self.tabWidgetClass.addTab(self.tab_class, "")
        self.tab_heritage = QtWidgets.QWidget()
        self.tab_heritage.setObjectName("tab_heritage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_heritage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TextEditElse = QtWidgets.QPlainTextEdit(self.tab_heritage)
        self.TextEditElse.setMinimumSize(QtCore.QSize(0, 0))
        self.TextEditElse.setObjectName("TextEditElse")
        self.gridLayout_4.addWidget(self.TextEditElse, 0, 0, 1, 1)
        self.ElseImg = QtWidgets.QLabel(self.tab_heritage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ElseImg.sizePolicy().hasHeightForWidth())
        self.ElseImg.setSizePolicy(sizePolicy)
        self.ElseImg.setMinimumSize(QtCore.QSize(0, 0))
        self.ElseImg.setMaximumSize(QtCore.QSize(16777215, 250))
        self.ElseImg.setText("")
        self.ElseImg.setPixmap(QtGui.QPixmap(":/classes/inheritance.png"))
        self.ElseImg.setObjectName("ElseImg")
        self.gridLayout_4.addWidget(self.ElseImg, 1, 0, 1, 1)
        self.tabWidgetClass.addTab(self.tab_heritage, "")
        self.tab_exercise1 = QtWidgets.QWidget()
        self.tab_exercise1.setObjectName("tab_exercise1")
        self.pushButtonExercise1 = QtWidgets.QPushButton(self.tab_exercise1)
        self.pushButtonExercise1.setGeometry(QtCore.QRect(180, 320, 131, 23))
        self.pushButtonExercise1.setObjectName("pushButtonExercise1")
        self.TextEditExercise1 = QtWidgets.QPlainTextEdit(self.tab_exercise1)
        self.TextEditExercise1.setGeometry(QtCore.QRect(60, 20, 471, 231))
        self.TextEditExercise1.setObjectName("TextEditExercise1")
        self.labelExercise1 = QtWidgets.QLabel(self.tab_exercise1)
        self.labelExercise1.setGeometry(QtCore.QRect(60, 360, 441, 41))
        self.labelExercise1.setText("")
        self.labelExercise1.setObjectName("labelExercise1")
        self.lineEditExercise1 = QtWidgets.QLineEdit(self.tab_exercise1)
        self.lineEditExercise1.setGeometry(QtCore.QRect(70, 270, 461, 20))
        self.lineEditExercise1.setObjectName("lineEditExercise1")
        self.tabWidgetClass.addTab(self.tab_exercise1, "")
        self.tab_init = QtWidgets.QWidget()
        self.tab_init.setObjectName("tab_init")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_init)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.TextEditConditions = QtWidgets.QPlainTextEdit(self.tab_init)
        self.TextEditConditions.setMinimumSize(QtCore.QSize(0, 0))
        self.TextEditConditions.setObjectName("TextEditConditions")
        self.gridLayout_6.addWidget(self.TextEditConditions, 0, 0, 1, 1)
        self.tabWidgetClass.addTab(self.tab_init, "")
        self.tab_exercise2 = QtWidgets.QWidget()
        self.tab_exercise2.setObjectName("tab_exercise2")
        self.TextEditExercise2 = QtWidgets.QPlainTextEdit(self.tab_exercise2)
        self.TextEditExercise2.setGeometry(QtCore.QRect(70, 10, 441, 251))
        self.TextEditExercise2.setObjectName("TextEditExercise2")
        self.pushButtonExercise2 = QtWidgets.QPushButton(self.tab_exercise2)
        self.pushButtonExercise2.setGeometry(QtCore.QRect(240, 310, 75, 23))
        self.pushButtonExercise2.setObjectName("pushButtonExercise2")
        self.lineEditExercise2 = QtWidgets.QLineEdit(self.tab_exercise2)
        self.lineEditExercise2.setGeometry(QtCore.QRect(130, 270, 291, 20))
        self.lineEditExercise2.setObjectName("lineEditExercise2")
        self.labelExercise2 = QtWidgets.QLabel(self.tab_exercise2)
        self.labelExercise2.setGeometry(QtCore.QRect(70, 350, 401, 41))
        self.labelExercise2.setText("")
        self.labelExercise2.setObjectName("labelExercise2")
        self.tabWidgetClass.addTab(self.tab_exercise2, "")
        self.gridLayout.addWidget(self.tabWidgetClass, 0, 0, 1, 1)

        self.retranslateUi()
        self.tabWidgetClass.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setCentralWidget(self.tabWidgetClass)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Różne ścieżki programu"))
        self.TextEditWelcome.setPlainText(_translate("Form", "O klasie możemy myśleć jak o wpisie w encyklopedii. Ma swoją nazwę (człowiek, pies czy kot) i ma swój opis, który zazwyczaj zaczyna się od nazwy kategorii do której należy. Pies to zwierzę, które ma cztery łapy i szczeka.\n"
"Klasa to bardzo abstrakcyjne pojęcie. Ogólne.\n"
"\n"
"Gdy już mamy zdefiniowana klasę będziemy tworzyć poszczególne obiekty naszej klasy: burka, reksa i aresa. Każdy z nich będzie miał osobne pola (atrybuty takie jak imię, wiek, rasę, wzrost i wagę), ale będą w stanie wykonać takie same metody jak szczekanie() lub pływanie().\n"
"\n"
"Czyli klasa to będzie ogólna definicja, czym jest pies. Obiekty to poszczególne psy - bardzo realne. Bez klasy nie mogłoby być obiektów, bo nie wiedzielibyśmy, co to znaczy pies. Ale bez obiektów pies to byłaby czysta teoria. Nie słyszelibyśmy szczekania, jedynie wiedzielibyśmy czym jest szczekanie, ale nie byłoby żadnego psa, który by szczekał. \n"
"\n"
"Skoro już wiemy, czym jest klasa, to teraz spróbujmy wyjaśnić po co ona jest. Raczej nie będziemy tworzyć piesków w naszym programie, choć brzmi to bardzo kusząco. Klasa pozwala nam na przechowywanie wszystkich związanych ze sobą funkcji w jednym miejscu: klasa do zapisu i odczytu z pliku, klasa do matematycznych operacji, klasa uczeń, która ułatwi nam przechowywanie wszystkich informacji o poszczególnym uczniu."))
        self.tabWidgetClass.setTabText(self.tabWidgetClass.indexOf(self.tab_welcome), _translate("Form", "O klasie słów kilka"))
        self.TextEditIf.setPlainText(_translate("Form", "Klasa definujemy za pomocą słówka pomocniczego class.\n"
"\n"
"class NazwaKlasy:\n"
"    def __init__(self):\n"
"        self.jakas_cecha = 20\n"
"        print(\"Tworzony obiekt\")\n"
"\n"
"    def inna_metoda(self):\n"
"        print(\"Wywołanie metody\")\n"
"\n"
"class to słówko kluczowe, które musi się pojawić na początku definicji klasy. Następnie pojawia się nazwa klasy. Może ona być dowolna, ale dobrą praktyką jest zaczynanie od dużej litery i rozpoczynanie każdej kolejnego słowa nazwy również od dużej litery (PrawidlowaNazwaKlasy). \n"
"\n"
"Po napisaniu pierwszej linijki przyszła pora na opisanie wszystkich metod, jakie będzie miała nasza klasa. Metody, które będą wykonywane przez poszczególne obiekty będą musiały mieć jako pierwszy argument, słówka self. self to właśnie odniesienie do poszczególnego wystąpienia danej klasy - pojedyńczego psa (naszego psa lub psa sąsiadów). Taki obiekt może mieć indywidualne cechy (konkretną wagę i rozmiar). Ale cechą wspólną wszystkich psów będzie, że każdy z nich ma jakąś wagę i jakiś rozmiar, więc jest to zdefiniowane na poziomie klasy, ale może być ustalone dopiero w momencie stworzenia nowego obiektu. Tak samo każdy pies ma swoje imię, ale imię psa jest ustalane dopiero po jego narodzinach.\n"
"\n"
"class Pies(Zwierze):\n"
"    def nadaj_imie(self, imie):\n"
"        self.nazwa = imie"))
        self.tabWidgetClass.setTabText(self.tabWidgetClass.indexOf(self.tab_class), _translate("Form", "class"))
        self.TextEditElse.setPlainText(_translate("Form", "Klasy mogą dziedziczyć po innych klasach. To oznacza, że z automatu otrzymują wszystkie funkcje i atrybuty, jakie miał ich przodek. Klasę, po której dziedziczymy, wpisujemy w nawiasach. Nie jest to mechanizm obowiązkowy. Możemy nawias zostawić pusty.\n"
"\n"
"class NazwaKlasy(Przodek):\n"
"    def inna_metoda(self):\n"
"        print(\"Wywołanie metody\")\n"
"\n"
"Następnie w nawiasach wpisujemy klasę, z której chcemy dziedziczyć cechy. Klasa Pies mogłaby dziedziczyć po klasie Zwierzęta, gdyż psy również będą chodzić, oddychać, jeść i wydawać jakieś odgłosy (posiadać funkcję, które już mogły być zaimplementowane w innej klasie). Czym się będą różnić od typowego zwierzęcia będą funkcję typowe tylko dla psów, jak na przykład wykonanie sztuczki za jedzenie. Pies będzie mógł korzystać, że wszystkich umiejętności Zwierza.\n"
"\n"
"class Pies(Zwierze):\n"
"    def wykonaj_stuczke(self):\n"
"        ...\n"
"\n"
"class Zwierze():\n"
"    def oddychaj(self):\n"
"        ..."))
        self.tabWidgetClass.setTabText(self.tabWidgetClass.indexOf(self.tab_heritage), _translate("Form", "Dziedziczenie"))
        self.pushButtonExercise1.setText(_translate("Form", "Sprawdź"))
        self.TextEditExercise1.setPlainText(_translate("Form", "Pierwsze zadanie!\n"
"Jakiego słówka brakuje w definicji poniższej klasy?\n"
"\n"
"Student():\n"
"    def __init__(self, name):\n"
"        self.name = name\n"
"        self.marks = []\n"
"\n"
"    def addMark(self, mark):\n"
"        self.marks.append(mark)\n"
"\n"
"    def changeLastMark(self,mark):\n"
"        self.marks[-1] = mark\n"
"\n"
"    def calculateAverage(self):\n"
"        return sum(marks)/len(marks)"))
        self.tabWidgetClass.setTabText(self.tabWidgetClass.indexOf(self.tab_exercise1), _translate("Form", "Zadanie 1"))
        self.TextEditConditions.setPlainText(_translate("Form", "Gdy definiujemy nową klasę możemy również zdefiniować funkcję __init__. Jest to specjalna funkcja, która wykonuje się tylko raz podczas tworzenia obiektu. Można tam ustalić takie cechy, którę mają się ustalić na samym początku. Później można je oczywiście zmienić, ale mogą to być jakieś wartości domyślne.\n"
"\n"
"class Pies(Zwierze):\n"
"    def __init__(self):\n"
"        self.nazwa = \"Burek\"\n"
"\n"
"Tym samym każdy tworzony przez nas pies będzie na początku na imię miał \"Burek\". Później będziemy mogli zmienić tą nazwę na inną, ale będzie to domyślna nazwa każdego psa zanim zostanie nazwany.\n"
"Tworzenie obiektu wykonuje się poprzez przywołanie nazwy klasy i dodania nawiasów okrągłych:\n"
"\n"
"Pies() - tworzymy domyślnego psa o nazwie \"Burek\"\n"
"\n"
" Do funkcji __init__ możemy przekazać też argumenty, jakieś cechy które chcemy ustalić w momencie tworzenia obiektu\n"
"\n"
"class Pies(Zwierze):\n"
"    def __init__(self, imie, waga, wzrost):\n"
"        self.nazwa = imie\n"
"        self.waga = waga\n"
"        self.wzrost = wzrost\n"
"\n"
"Wymagane argumenty dodaje się w nawiasie:\n"
"\n"
"Pies(\"Ares\", 5, 25) - tym samym tworzymy psa, który ma na imię \"Ares\", waży 5 kg i ma wzrostu 25 cm. \n"
"\n"
"Stworzonego psa można od razu przypisać do zmiennej, aby później kazać mu wykonywać różne metody albo odwołać się do jego para parametrów. Aby odwołać się do konkretnej metody naszego psa piszemy nazwę jego zmiennej, kropkę i nazwę metody, którą chcemy wywołać lub zmiennej związanej z naszym obiektem.\n"
"\n"
"piesek1 = Pies(\"Ares\", 5, 25)\n"
"piesek1.wykonaj_sztuczke()\n"
"print(\"Nazwa pieska to: \" + piesek1.nazwa)"))
        self.tabWidgetClass.setTabText(self.tabWidgetClass.indexOf(self.tab_init), _translate("Form", "__init__"))
        self.TextEditExercise2.setPlainText(_translate("Form", "Powołaj do życia studenta imieniem Anna \n"
"\n"
"class Student():\n"
"    def __init__(self, name):\n"
"        self.name = name\n"
"        self.marks = []\n"
"\n"
"    def addMark(self, mark):\n"
"        self.marks.append(mark)\n"
"\n"
"    def changeLastMark(self,mark):\n"
"        self.marks[-1] = mark\n"
"\n"
"    def calculateAverage(self):\n"
"        if len(self.marks> 0):\n"
"            return sum(self.marks)/len(self.marks)\n"
"        else:\n"
"            return 1"))
        self.pushButtonExercise2.setText(_translate("Form", "Sprawdź"))
        self.tabWidgetClass.setTabText(self.tabWidgetClass.indexOf(self.tab_exercise2), _translate("Form", "Zadanie 2"))
import obrazki.obrazki_classes
