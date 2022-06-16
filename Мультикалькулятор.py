import sys
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLCDNumber
from PyQt5.QtWidgets import QInputDialog, QLabel, QLineEdit, QWidget
from PyQt5.QtCore import Qt
import math

c = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '00']
part_1 = " название валюты\n(например - USD) и новое значение, затем\n нажмите "
part_2 = "снова на Edit\n(Вы изменяете курс относительно рубля)"
Regarding_km = {'m': '1000', 'mm': '1000000', 'cm': '100000', 'mi': '0.62137',
                'yd': '1093.613298', 'ft': '3280.839895', 'in': '39370.07874', 'nmi': '0.54'}

Regarding_kg = {'mg': '1000000', 'g': '1000', 't': '0.001', 'uk': '0.000984206528',
                'us': '0.001102311311', 'lb': '2.204622476', 'ou': '35.273991',
                'st': '0.157473', 'ct': '5000'}

class Arithmometer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.peremensy_1 = ''  # Первая переменная вводимая пользователем
        self.peremensy_2 = ''  # Вторая переменная вводимая пользователем
        self.check_active_number = False  # Проверяем какое число должен вводить пользователь
        self.destvie = ''  # Здесь записывается действие, которое должен совершить калькулятор
        self.btn1.clicked.connect(self.run)  # Активируем все кнопки
        self.btn2.clicked.connect(self.run)
        self.btn3.clicked.connect(self.run)
        self.btn4.clicked.connect(self.run)
        self.btn5.clicked.connect(self.run)
        self.btn6.clicked.connect(self.run)
        self.btn7.clicked.connect(self.run)
        self.btn8.clicked.connect(self.run)
        self.btn9.clicked.connect(self.run)
        self.btn0.clicked.connect(self.run)
        self.btn_minus.clicked.connect(self.run)
        self.btn_eq.clicked.connect(self.run)
        self.btn_plus.clicked.connect(self.run)
        self.btn_sqrt.clicked.connect(self.run)
        self.btn_fact.clicked.connect(self.run)
        self.btn_mult.clicked.connect(self.run)
        self.btn_clear.clicked.connect(self.run)
        self.btn_div.clicked.connect(self.run)
        self.btn_dot.clicked.connect(self.run)
        self.btn_pow.clicked.connect(self.run)
        self.btn_square.clicked.connect(self.run)
        self.btn_sqrt3.clicked.connect(self.run)
        self.btn_00.clicked.connect(self.run)
        self.btn_nega.clicked.connect(self.run)
        self.btn_percent.clicked.connect(self.run)


    def run(self):
        try:
            p = self.sender().text()  # Что вводит пользователь
            if p in c:  # Если это является цифрой или точкой
                if p == '.':
                    if self.check_active_number:  # Если это первое число
                        if len(self.peremensy_1) > 0:  # Если точку поставить после введённых цифр
                            self.peremensy_1 += str(p)  # Добавляем точки
                        else:  # Если точку поставим сначала, до того как пользователь ввёл цифры
                            self.peremensy_1 += ('0' + str(p))  # Добавляет точки
                        self.table.display(self.peremensy_1)  # Выводит на дисплей
                    else:  # Если это второе число
                        if len(self.peremensy_2) > 0:
                            self.peremensy_2 += str(p)
                        else:
                            self.peremensy_2 += ('0' + str(p))
                        self.table.display(self.peremensy_2)
                elif self.check_active_number:  # Если это первое число
                    self.peremensy_1 += str(p)  # Добавляет цифру в виде строки
                    self.table.display(self.peremensy_1)
                else:  # Если это второе число
                    self.peremensy_2 += str(p)
                    self.table.display(self.peremensy_2)
            if p == '-':  # Если пользователь введёт операцию с использованием сразу двух переменных
                self.table.display(self.peremensy_1)  # Выводит на дисплей другую переменную
                self.destvie = '-'  # Запоминает действие, совершонное пользовотелем в виде знака
                self.check_active_number = True  # Переключаемся на запись второй переменной
            if p == '+':
                self.table.display(self.peremensy_1)
                self.destvie = '+'
                self.check_active_number = True                
            if p == '*':
                self.table.display(self.peremensy_1)
                self.destvie = '*'
                self.check_active_number = True                
            if p == '/':
                self.table.display(self.peremensy_1)
                self.destvie = '/'
                self.check_active_number = True                
            if p == '^':
                self.table.display(self.peremensy_1)
                self.check_active_number = True
                self.destvie = '^'
            if p == '√':  # Если пользователь введёт операцию с использованием одной переменной
                operation = float(self.peremensy_2) ** 0.5  # Производит необходимую операцию
                self.table.display(operation)
                self.destvie = '√'
                self.peremensy_1 = ''
                self.peremensy_2 = operation
            if p == 'С':  # Если пользователь введёт операцию 'clear', то
                self.peremensy_1 = ''  # Очищяет все переменные и действия
                self.check_active_number = False
                self.peremensy_2 = ''
                self.destvie = ''
                self.table.display('')
            if p == '^2':
                operation = float(self.peremensy_2) ** 2
                self.table.display(operation)
                self.destvie = '^2'
                self.peremensy_1 = ''
                self.peremensy_2 = operation
            if p == '3√':
                operation = float(self.peremensy_2) ** (1 / 3)
                self.table.display(operation)
                self.destvie = '3√'
                self.peremensy_1 = ''
                self.peremensy_2 = operation
            if p == '+/-':  # Если пользователю нужно поменять знак числа которое он вводит
                if self.check_active_number:  # Если это первое число
                    if self.peremensy_1[0] == '-':  # Если число отрицательное
                        self.peremensy_1 = self.peremensy_1[1::]  # Перезаписывает его, но без '-'
                        self.table.display(self.peremensy_1)
                    else:
                        self.peremensy_1 = '-' + self.peremensy_1  # Добаввляет '-'
                        self.table.display(self.peremensy_1)
                else:  # Если это второе число
                    if self.peremensy_2[0] == '-':  # Также как и с первым числом
                        self.peremensy_2 = self.peremensy_2[1::]
                        self.table.display(self.peremensy_2)
                    else:
                        self.peremensy_2 = '-' + self.peremensy_2
                        self.table.display(self.peremensy_2)
            if p == '%':
                operation = float(self.peremensy_2) / 100
                self.table.display(operation)
                self.destvie = '%'
                self.peremensy_1 = ''
                self.peremensy_2 = operation
            if p == '!':
                factorial = math.factorial(int(self.peremensy_2))
                self.table.display(factorial)
                self.destvie = '!'
                self.peremensy_1 = ''
                self.peremensy_2 = factorial

            if p == '=':  # Если пользователь ввёл равно
                if self.destvie == '-':  # Если перед этим он нажал на '-'
                    operation = float(self.peremensy_2) - float(self.peremensy_1)
                    self.table.display(operation)  # Записывает операцию запрошенную пользователем
                    self.peremensy_1 = ''  # Опустошаем первую переменную
                    self.peremensy_2 = operation  # Запишем продукт операции во вторую
                if self.destvie == '+':
                    operation = float(self.peremensy_2) + float(self.peremensy_1)
                    self.table.display(operation)
                    self.peremensy_1 = ''
                    self.peremensy_2 = operation
                if self.destvie == '*':
                    operation = float(self.peremensy_2) * float(self.peremensy_1)
                    self.table.display(operation)
                    self.peremensy_1 = ''
                    self.peremensy_2 = operation
                if self.destvie == '/':
                    operation = float(self.peremensy_2) / float(self.peremensy_1)
                    self.table.display(operation)
                    self.peremensy_1 = ''
                    self.peremensy_2 = operation
                if self.destvie == '^':
                    operation = float(self.peremensy_2) ** float(self.peremensy_1)
                    self.table.display(operation)
                    self.peremensy_1 = ''
                    self.peremensy_2 = operation
        except:  # В случае если что-то пойдет не правильно программа выведит 'error'
            self.table.display('error')
            self.peremensy_1 = ''  # И опустошит переменные
            self.check_active_number = False
            self.peremensy_2 = ''
            self.destvie = ''

class Currency(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.number_edit = 0
        self.Regarding_RUB = {'USD': '0.0126', 'EUR': '0.01079 ', 'BYN': '0.033 ',
                              'KZT': '5.4064', 'TRY': '0.1052', 'UAH': '0.3586'}
        # Создаём словарь с Валютами и их курсом относительно Рубля        
    def initUI(self):
        self.setGeometry(550, 100, 300, 550)
        self.setWindowTitle('Валюта')

        self.name_label = QLabel(self)
        self.name_label.setText("После выполнения операции\nнажмите на кнопку 'Clear/Anew'")
        self.name_label.move(10, 500)
        self.name_label.resize(300, 40)

        self.name_label = QLabel(self)
        self.name_label.setText("Российский рубль\n          (RUB)")
        self.name_label.move(30, 30)
        self.name_input_RUB = QLineEdit(self)
        self.name_input_RUB.resize(150, 26)
        self.name_input_RUB.move(130, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Доллар США\n      (USD)")
        self.name_label.move(40, 70)
        self.name_input_USD = QLineEdit(self)
        self.name_input_USD.resize(150, 26)
        self.name_input_USD.move(130, 70)

        self.name_label = QLabel(self)
        self.name_label.setText(" Евро\n(EUR)")
        self.name_label.move(58, 110)
        self.name_input_EUR = QLineEdit(self)
        self.name_input_EUR.resize(150, 26)
        self.name_input_EUR.move(130, 110)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Украинская гривна\n          (UAH)")
        self.name_label.move(29, 150)
        self.name_input_UAH = QLineEdit(self)
        self.name_input_UAH.resize(150, 26)
        self.name_input_UAH.move(130, 150)

        self.name_label = QLabel(self)
        self.name_label.setText("Турецкая лира\n      (TRY)")
        self.name_label.move(40, 190)
        self.name_input_TRY = QLineEdit(self)
        self.name_input_TRY.resize(150, 26)
        self.name_input_TRY.move(130, 190)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Белорусский рубль\n          (BYN)")
        self.name_label.move(28, 230)
        self.name_input_BYN = QLineEdit(self)
        self.name_input_BYN.resize(150, 26)
        self.name_input_BYN.move(130, 230)

        self.name_label = QLabel(self)
        self.name_label.setText("Казахстанский тенге \n             (KZT)")
        self.name_label.resize(150, 26)
        self.name_label.move(20, 270)
        self.name_input_KZT = QLineEdit(self)
        self.name_input_KZT.resize(150, 26)
        self.name_input_KZT.move(130, 270)
        
        self.btn = QPushButton('Count', self)
        self.btn.move(30, 350)
        self.btn.clicked.connect(self.run)
        
        self.btn = QPushButton('Clear/Anew', self)
        self.btn.move(170, 350)
        self.btn.clicked.connect(self.clear)

        self.btn = QPushButton('Edit', self)
        self.btn.move(170, 400)
        self.btn.clicked.connect(self.Edit)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Неверно введены данные!")
        self.name_label.resize(150, 26)
        self.name_label.move(30, 300)
        self.name_label.hide()
        
        self.name_input_edit = QLineEdit(self)
        self.name_input_edit.resize(150, 26)
        self.name_input_edit.move(10, 400)
        self.name_input_edit.hide()

        self.name_label_edit = QLabel(self)
        self.name_label_edit.setText("↑↑↑ Напишите через пробел: Краткое" + part_1 + part_2)
        self.name_label_edit.resize(300, 60)
        self.name_label_edit.move(10, 430)
        self.name_label_edit.hide()


    def run(self):
        self.name_RUB = self.name_input_RUB.text()  # Получит текст из поля ввода
        self.name_USD = self.name_input_USD.text()
        self.name_EUR = self.name_input_EUR.text()
        self.name_UAH = self.name_input_UAH.text()
        self.name_TRY = self.name_input_TRY.text()
        self.name_BYN = self.name_input_BYN.text()
        self.name_KZT = self.name_input_KZT.text()
        self.name_label.hide()  # Скрывает Текст с сообщением об ошибке
        try:
            if len(self.name_RUB) > 0:  # Если вводится в поле ... , то производим вычисления
                self.name_input_USD.setText(str(float(self.name_RUB) * float(self.Regarding_RUB['USD'])))
                self.name_input_EUR.setText(str(float(self.name_RUB) * float(self.Regarding_RUB['EUR'])))
                self.name_input_UAH.setText(str(float(self.name_RUB) * float(self.Regarding_RUB['UAH'])))
                self.name_input_TRY.setText(str(float(self.name_RUB) * float(self.Regarding_RUB['TRY'])))
                self.name_input_BYN.setText(str(float(self.name_RUB) * float(self.Regarding_RUB['BYN'])))
                self.name_input_KZT.setText(str(float(self.name_RUB) * float(self.Regarding_RUB['KZT'])))
            elif len(self.name_USD) > 0:
                # Высчитывает сначало в Рублях, а затем переводит в нужную валюту
                Regarding_USD = float(self.name_USD) / float(self.Regarding_RUB['USD'])
                self.name_input_RUB.setText(str(Regarding_USD))
                self.name_input_EUR.setText(str(Regarding_USD * float(self.Regarding_RUB['EUR'])))
                self.name_input_UAH.setText(str(Regarding_USD * float(self.Regarding_RUB['UAH'])))
                self.name_input_TRY.setText(str(Regarding_USD * float(self.Regarding_RUB['TRY'])))
                self.name_input_BYN.setText(str(Regarding_USD * float(self.Regarding_RUB['BYN'])))
                self.name_input_KZT.setText(str(Regarding_USD * float(self.Regarding_RUB['KZT'])))
            elif len(self.name_EUR) > 0:
                Regarding_EUR = float(self.name_EUR) / float(self.Regarding_RUB['EUR'])
                self.name_input_RUB.setText(str(Regarding_EUR))
                self.name_input_USD.setText(str(Regarding_EUR * float(self.Regarding_RUB['USD'])))
                self.name_input_UAH.setText(str(Regarding_EUR * float(self.Regarding_RUB['UAH'])))
                self.name_input_TRY.setText(str(Regarding_EUR * float(self.Regarding_RUB['TRY'])))
                self.name_input_BYN.setText(str(Regarding_EUR * float(self.Regarding_RUB['BYN'])))
                self.name_input_KZT.setText(str(Regarding_EUR * float(self.Regarding_RUB['KZT'])))
            elif len(self.name_UAH) > 0:
                Regarding_UAH = float(self.name_UAH) / float(self.Regarding_RUB['UAH'])
                self.name_input_RUB.setText(str(Regarding_UAH))
                self.name_input_USD.setText(str(Regarding_UAH * float(self.Regarding_RUB['USD'])))
                self.name_input_EUR.setText(str(Regarding_UAH * float(self.Regarding_RUB['EUR'])))
                self.name_input_TRY.setText(str(Regarding_UAH * float(self.Regarding_RUB['TRY'])))
                self.name_input_BYN.setText(str(Regarding_UAH * float(self.Regarding_RUB['BYN'])))
                self.name_input_KZT.setText(str(Regarding_UAH * float(self.Regarding_RUB['KZT'])))
            elif len(self.name_TRY) > 0:
                Regarding_TRY = float(self.name_TRY) / float(self.Regarding_RUB['TRY'])
                self.name_input_RUB.setText(str(Regarding_TRY))
                self.name_input_USD.setText(str(Regarding_TRY * float(self.Regarding_RUB['USD'])))
                self.name_input_EUR.setText(str(Regarding_TRY * float(self.Regarding_RUB['EUR'])))
                self.name_input_UAH.setText(str(Regarding_TRY * float(self.Regarding_RUB['UAH'])))
                self.name_input_BYN.setText(str(Regarding_TRY * float(self.Regarding_RUB['BYN'])))
                self.name_input_KZT.setText(str(Regarding_TRY * float(self.Regarding_RUB['KZT'])))
            elif len(self.name_BYN) > 0:
                Regarding_BYN = float(self.name_BYN) / float(self.Regarding_RUB['BYN'])
                self.name_input_RUB.setText(str(Regarding_BYN))
                self.name_input_USD.setText(str(Regarding_BYN * float(self.Regarding_RUB['USD'])))
                self.name_input_EUR.setText(str(Regarding_BYN * float(self.Regarding_RUB['EUR'])))
                self.name_input_TRY.setText(str(Regarding_BYN * float(self.Regarding_RUB['TRY'])))
                self.name_input_UAH.setText(str(Regarding_BYN * float(self.Regarding_RUB['UAH'])))
                self.name_input_KZT.setText(str(Regarding_BYN * float(self.Regarding_RUB['KZT'])))
            elif len(self.name_KZT) > 0:
                Regarding_KZT = float(self.name_KZT) / float(self.Regarding_RUB['KZT'])
                self.name_input_RUB.setText(str(Regarding_KZT))
                self.name_input_USD.setText(str(Regarding_KZT * float(self.Regarding_RUB['USD'])))
                self.name_input_EUR.setText(str(Regarding_KZT * float(self.Regarding_RUB['EUR'])))
                self.name_input_TRY.setText(str(Regarding_KZT * float(self.Regarding_RUB['TRY'])))
                self.name_input_UAH.setText(str(Regarding_KZT * float(self.Regarding_RUB['UAH'])))
                self.name_input_BYN.setText(str(Regarding_KZT * float(self.Regarding_RUB['BYN'])))
        except:  # В случае ошибки очищяем все строки и выводим Текст с сообщением об ошибке
            self.clear()
            self.name_label.show()

    def clear(self):  # Функция очищения строк
        self.name_input_USD.setText('')
        self.name_input_RUB.setText('')
        self.name_input_EUR.setText('')
        self.name_input_UAH.setText('')
        self.name_input_TRY.setText('')
        self.name_input_BYN.setText('')
        self.name_input_KZT.setText('')

    def Edit(self):  # Функция для изменения курса валюты относительно рубля
        self.name_label_edit.show()  # Показываем строку и информацию для изменения курса
        self.name_input_edit.show()
        self.name_edit = self.name_input_edit.text().split(' ')  # Создаёт список из имени валюты и
        try:  # его новым курсом относительно Рубля
            self.name_label.hide()  # Если всё верно то скрываем Текст с сообщением об ошибке
            if len(self.name_edit) > 1:  # Если пользователь что-то введёт
                self.number_edit = 1  # Присвоит значение
                if float(self.name_edit[1]) > 0:  # Если значение нового курса больше 0
                    self.Regarding_RUB[self.name_edit[0]] = str(float(self.name_edit[1]))
                    self.name_edit = ''  # Присвоит ключу из списка нужный аргумент
                else:
                    1 / 0  # Выбрасит из try
            else:
                if self.number_edit == 1:  # Если Присвоил значение
                    self.number_edit = 0  # Присвоим значение
                    self.name_label_edit.hide()  # Скрывает строку и информацию для изменения курса
                    self.name_input_edit.hide()  # Это нужно для того чтобы суметь скрыть строку
        except:  # В случае ошибки очищяем строку и выводим Текст с сообщением об ошибке
            self.name_label.show()            
            self.name_input_edit.setText('')
            

class Distance(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 100, 300, 550)
        self.setWindowTitle('Расстояние')
        
        self.name_label = QLabel(self)
        self.name_label.setText("После выполнения операции\nнажмите на кнопку 'Clear/Anew'")
        self.name_label.move(10, 500)
        self.name_label.resize(300, 40)
        self.name_label = QLabel(self)
        
        self.name_label.setText("Километр (km)")
        self.name_label.move(30, 30)
        self.name_input_km = QLineEdit(self)
        self.name_input_km.resize(150, 26)
        self.name_input_km.move(130, 30)
        self.name_label = QLabel(self)
        
        self.name_label.setText("Метр (m)")
        self.name_label.move(30, 70)
        self.name_input_m = QLineEdit(self)
        self.name_input_m.resize(150, 26)
        self.name_input_m.move(130, 70)

        self.name_label = QLabel(self)
        self.name_label.setText("Сантиметр (cm)")
        self.name_label.move(30, 110)
        self.name_input_cm = QLineEdit(self)
        self.name_input_cm.resize(150, 26)
        self.name_input_cm.move(130, 110)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Миллиметр (mm)")
        self.name_label.move(30, 150)
        self.name_input_mm = QLineEdit(self)
        self.name_input_mm.resize(150, 26)
        self.name_input_mm.move(130, 150)

        self.name_label = QLabel(self)
        self.name_label.setText("Миля (mi)")
        self.name_label.move(30, 190)
        self.name_input_mi = QLineEdit(self)
        self.name_input_mi.resize(150, 26)
        self.name_input_mi.move(130, 190)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Ярд (yd)")
        self.name_label.move(30, 230)
        self.name_input_yd = QLineEdit(self)
        self.name_input_yd.resize(150, 26)
        self.name_input_yd.move(130, 230)

        self.name_label = QLabel(self)
        self.name_label.setText("Фут (ft)")
        self.name_label.move(30, 270)
        self.name_input_ft = QLineEdit(self)
        self.name_input_ft.resize(150, 26)
        self.name_input_ft.move(130, 270)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Дюйм (in)")
        self.name_label.move(30, 310)
        self.name_input_in = QLineEdit(self)
        self.name_input_in.resize(150, 26)
        self.name_input_in.move(130, 310)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Морская миля (nmi)")
        self.name_label.move(30, 350)
        self.name_input_nmi = QLineEdit(self)
        self.name_input_nmi.resize(150, 26)
        self.name_input_nmi.move(130, 350)
        
        self.btn = QPushButton('Count', self)
        self.btn.move(30, 400)
        self.btn.clicked.connect(self.run)
        
        self.btn = QPushButton('Clear/Anew', self)
        self.btn.move(170, 400)
        self.btn.clicked.connect(self.clear)

        self.name_label = QLabel(self)
        self.name_label.setText("Неверно введены данные!")
        self.name_label.resize(150, 26)
        self.name_label.move(30, 450)
        self.name_label.hide()
        
    def run(self):
        self.name_km = self.name_input_km.text()  # Получим текст из поля ввода
        self.name_m = self.name_input_m.text()
        self.name_cm = self.name_input_cm.text()
        self.name_mm = self.name_input_mm.text()
        self.name_mi = self.name_input_mi.text()
        self.name_yd = self.name_input_yd.text()
        self.name_ft = self.name_input_ft.text()
        self.name_in = self.name_input_in.text()
        self.name_nmi = self.name_input_nmi.text()
        self.name_label.hide()  # Скрывает Текст с сообщением об ошибке
        try:  # Такой же принцип как и в валюте
            if len(self.name_km) > 0:
                self.name_input_m.setText(str(float(self.name_km) * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(float(self.name_km) * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(float(self.name_km) * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(float(self.name_km) * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(float(self.name_km) * float(Regarding_km['yd'])))
                self.name_input_ft.setText(str(float(self.name_km) * float(Regarding_km['ft'])))
                self.name_input_in.setText(str(float(self.name_km) * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(float(self.name_km) * float(Regarding_km['nmi'])))
            elif len(self.name_m) > 0:
                Regarding_m = float(self.name_m) / float(Regarding_km['m'])
                self.name_input_km.setText(str(Regarding_m))
                self.name_input_cm.setText(str(Regarding_m * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(Regarding_m * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(Regarding_m * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(Regarding_m * float(Regarding_km['yd'])))
                self.name_input_ft.setText(str(Regarding_m * float(Regarding_km['ft'])))
                self.name_input_in.setText(str(Regarding_m * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(Regarding_m * float(Regarding_km['nmi'])))
            elif len(self.name_cm) > 0:
                Regarding_cm = float(self.name_cm) / float(Regarding_km['cm'])
                self.name_input_km.setText(str(Regarding_cm))
                self.name_input_m.setText(str(Regarding_cm * float(Regarding_km['m'])))
                self.name_input_mm.setText(str(Regarding_cm * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(Regarding_cm * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(Regarding_cm * float(Regarding_km['yd'])))
                self.name_input_ft.setText(str(Regarding_cm * float(Regarding_km['ft'])))
                self.name_input_in.setText(str(Regarding_cm * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(Regarding_cm * float(Regarding_km['nmi'])))
            elif len(self.name_mm) > 0:
                Regarding_mm = float(self.name_mm) / float(Regarding_km['mm'])
                self.name_input_km.setText(str(Regarding_mm))
                self.name_input_m.setText(str(Regarding_mm * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(Regarding_mm * float(Regarding_km['cm'])))
                self.name_input_mi.setText(str(Regarding_mm * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(Regarding_mm * float(Regarding_km['yd'])))
                self.name_input_ft.setText(str(Regarding_mm * float(Regarding_km['ft'])))
                self.name_input_in.setText(str(Regarding_mm * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(Regarding_mm * float(Regarding_km['nmi'])))
            elif len(self.name_mi) > 0:
                Regarding_mi = float(self.name_mi) / float(Regarding_km['mi'])
                self.name_input_km.setText(str(Regarding_mi))
                self.name_input_m.setText(str(Regarding_mi * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(Regarding_mi * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(Regarding_mi * float(Regarding_km['mm'])))
                self.name_input_yd.setText(str(Regarding_mi * float(Regarding_km['yd'])))
                self.name_input_ft.setText(str(Regarding_mi * float(Regarding_km['ft'])))
                self.name_input_in.setText(str(Regarding_mi * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(Regarding_mi * float(Regarding_km['nmi'])))
            elif len(self.name_yd) > 0:
                Regarding_yd = float(self.name_yd) / float(Regarding_km['yd'])
                self.name_input_km.setText(str(Regarding_yd))
                self.name_input_m.setText(str(Regarding_yd * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(Regarding_yd * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(Regarding_yd * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(Regarding_yd * float(Regarding_km['mi'])))
                self.name_input_ft.setText(str(Regarding_yd * float(Regarding_km['ft'])))
                self.name_input_in.setText(str(Regarding_yd * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(Regarding_yd * float(Regarding_km['nmi'])))
            elif len(self.name_ft) > 0:
                Regarding_ft = float(self.name_ft) / float(Regarding_km['ft'])
                self.name_input_km.setText(str(Regarding_ft))
                self.name_input_m.setText(str(Regarding_ft * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(Regarding_ft * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(Regarding_ft * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(Regarding_ft * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(Regarding_ft * float(Regarding_km['yd'])))
                self.name_input_in.setText(str(Regarding_ft * float(Regarding_km['in'])))
                self.name_input_nmi.setText(str(Regarding_ft * float(Regarding_km['nmi'])))
            elif len(self.name_in) > 0:
                Regarding_in = float(self.name_in) / float(Regarding_km['in'])
                self.name_input_km.setText(str(Regarding_in))
                self.name_input_m.setText(str(Regarding_in * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(Regarding_in * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(Regarding_in * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(Regarding_in * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(Regarding_in * float(Regarding_km['yd'])))
                self.name_input_ft.setText(str(Regarding_in * float(Regarding_km['ft'])))
                self.name_input_nmi.setText(str(Regarding_in * float(Regarding_km['nmi'])))
            elif len(self.name_nmi) > 0:
                Regarding_nmi = float(self.name_nmi) / float(Regarding_km['nmi'])
                self.name_input_km.setText(str(Regarding_nmi))
                self.name_input_m.setText(str(Regarding_nmi * float(Regarding_km['m'])))
                self.name_input_cm.setText(str(Regarding_nmi * float(Regarding_km['cm'])))
                self.name_input_mm.setText(str(Regarding_nmi * float(Regarding_km['mm'])))
                self.name_input_mi.setText(str(Regarding_nmi * float(Regarding_km['mi'])))
                self.name_input_yd.setText(str(Regarding_nmi * float(Regarding_km['yd'])))
                self.name_input_in.setText(str(Regarding_nmi * float(Regarding_km['in'])))
                self.name_input_ft.setText(str(Regarding_nmi * float(Regarding_km['ft'])))
        except:
            self.clear()
            self.name_label.show()

    def clear(self):
        self.name_input_km.setText('')
        self.name_input_m.setText('')
        self.name_input_cm.setText('')
        self.name_input_mm.setText('')
        self.name_input_mi.setText('')
        self.name_input_yd.setText('')
        self.name_input_ft.setText('')
        self.name_input_in.setText('')
        self.name_input_nmi.setText('')


class Weight(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 100, 300, 550)
        self.setWindowTitle('Масса')
        
        self.name_label = QLabel(self)
        self.name_label.setText("После выполнения операции\nнажмите на кнопку 'Clear/Anew'")
        self.name_label.move(10, 500)
        self.name_label.resize(300, 40)
        self.name_label = QLabel(self)
        
        self.name_label.setText("Килограмм (kg)")
        self.name_label.move(30, 30)
        self.name_input_kg = QLineEdit(self)
        self.name_input_kg.resize(150, 26)
        self.name_input_kg.move(130, 30)
        self.name_label = QLabel(self)        

        self.name_label.setText("Грамм (g)")
        self.name_label.move(30, 70)
        self.name_input_g = QLineEdit(self)
        self.name_input_g.resize(150, 26)
        self.name_input_g.move(130, 70)

        self.name_label = QLabel(self)
        self.name_label.setText("Миллиграмм (mg)")
        self.name_label.move(30, 110)
        self.name_input_mg = QLineEdit(self)
        self.name_input_mg.resize(150, 26)
        self.name_input_mg.move(130, 110)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Метрическая тонна\n(t)")
        self.name_label.move(30, 150)
        self.name_input_t = QLineEdit(self)
        self.name_input_t.resize(150, 26)
        self.name_input_t.move(130, 150)

        self.name_label = QLabel(self)
        self.name_label.setText("Длинная тонна\n(ton uk)")
        self.name_label.move(30, 190)
        self.name_input_uk = QLineEdit(self)
        self.name_input_uk.resize(150, 26)
        self.name_input_uk.move(130, 190)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Короткая тонна\n(ton us)")
        self.name_label.move(30, 230)
        self.name_input_us = QLineEdit(self)
        self.name_input_us.resize(150, 26)
        self.name_input_us.move(130, 230)

        self.name_label = QLabel(self)
        self.name_label.setText("Фунт (ld)")
        self.name_label.move(30, 270)
        self.name_input_lb = QLineEdit(self)
        self.name_input_lb.resize(150, 26)
        self.name_input_lb.move(130, 270)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Унция (ounce)")
        self.name_label.move(30, 310)
        self.name_input_ou = QLineEdit(self)
        self.name_input_ou.resize(150, 26)
        self.name_input_ou.move(130, 310)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Стоун (st)")
        self.name_label.move(30, 350)
        self.name_input_st = QLineEdit(self)
        self.name_input_st.resize(150, 26)
        self.name_input_st.move(130, 350)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Карат (ct)")
        self.name_label.move(30, 390)
        self.name_input_ct = QLineEdit(self)
        self.name_input_ct.resize(150, 26)
        self.name_input_ct.move(130, 390)
        
        self.btn = QPushButton('Count', self)
        self.btn.move(30, 460)
        self.btn.clicked.connect(self.run)
        
        self.btn = QPushButton('Clear/Anew', self)
        self.btn.move(170, 460)
        self.btn.clicked.connect(self.clear)

        self.name_label = QLabel(self)
        self.name_label.setText("Неверно введены данные!")
        self.name_label.resize(150, 26)
        self.name_label.move(30, 430)
        self.name_label.hide()
        
    def run(self):
        self.name_kg = self.name_input_kg.text()  # Получим текст из поля ввода
        self.name_mg = self.name_input_mg.text()
        self.name_g = self.name_input_g.text()
        self.name_t = self.name_input_t.text()
        self.name_uk = self.name_input_uk.text()
        self.name_us = self.name_input_us.text()
        self.name_lb = self.name_input_lb.text()
        self.name_ou = self.name_input_ou.text()
        self.name_st = self.name_input_st.text()
        self.name_ct = self.name_input_ct.text()
        self.name_label.hide()  # Скрывает Текст с сообщением об ошибке
        try:  # Такой же принцип как и в валюте
            if len(self.name_kg) > 0:
                self.name_input_mg.setText(str(float(self.name_kg) * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(float(self.name_kg) * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(float(self.name_kg) * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(float(self.name_kg) * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(float(self.name_kg) * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(float(self.name_kg) * float(Regarding_kg['lb'])))
                self.name_input_ou.setText(str(float(self.name_kg) * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(float(self.name_kg) * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(float(self.name_kg) * float(Regarding_kg['ct'])))
            elif len(self.name_mg) > 0:
                Regarding_mg = float(self.name_mg) / float(Regarding_kg['mg'])
                self.name_input_kg.setText(str(Regarding_mg))
                self.name_input_g.setText(str(Regarding_mg * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_mg * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_mg * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_mg * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_mg * float(Regarding_kg['lb'])))
                self.name_input_ou.setText(str(Regarding_mg * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(Regarding_mg * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_mg * float(Regarding_kg['ct'])))
            elif len(self.name_g) > 0:
                Regarding_g = float(self.name_g) / float(Regarding_kg['g'])
                self.name_input_kg.setText(str(Regarding_g))
                self.name_input_mg.setText(str(Regarding_g * float(Regarding_kg['mg'])))
                self.name_input_t.setText(str(Regarding_g * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_g * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_g * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_g * float(Regarding_kg['lb'])))
                self.name_input_ou.setText(str(Regarding_g * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(Regarding_g * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_g * float(Regarding_kg['ct'])))
            elif len(self.name_t) > 0:
                Regarding_t = float(self.name_t) / float(Regarding_kg['t'])
                self.name_input_kg.setText(str(Regarding_t))
                self.name_input_mg.setText(str(Regarding_t * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_t * float(Regarding_kg['g'])))
                self.name_input_uk.setText(str(Regarding_t * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_t * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_t * float(Regarding_kg['lb'])))
                self.name_input_ou.setText(str(Regarding_t * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(Regarding_t * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_t * float(Regarding_kg['ct'])))
            elif len(self.name_uk) > 0:
                Regarding_uk = float(self.name_uk) / float(Regarding_kg['uk'])
                self.name_input_kg.setText(str(Regarding_uk))
                self.name_input_mg.setText(str(Regarding_uk * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_uk * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_uk * float(Regarding_kg['t'])))
                self.name_input_us.setText(str(Regarding_uk * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_uk * float(Regarding_kg['lb'])))
                self.name_input_ou.setText(str(Regarding_uk * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(Regarding_uk * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_uk * float(Regarding_kg['ct'])))
            elif len(self.name_us) > 0:
                Regarding_us = float(self.name_us) / float(Regarding_kg['us'])
                self.name_input_kg.setText(str(Regarding_us))
                self.name_input_mg.setText(str(Regarding_us * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_us * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_us * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_us * float(Regarding_kg['uk'])))
                self.name_input_lb.setText(str(Regarding_us * float(Regarding_kg['lb'])))
                self.name_input_ou.setText(str(Regarding_us * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(Regarding_us * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_us * float(Regarding_kg['ct'])))
            elif len(self.name_lb) > 0:
                Regarding_lb = float(self.name_lb) / float(Regarding_kg['lb'])
                self.name_input_kg.setText(str(Regarding_lb))
                self.name_input_mg.setText(str(Regarding_lb * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_lb * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_lb * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_lb * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_lb * float(Regarding_kg['us'])))
                self.name_input_ou.setText(str(Regarding_lb * float(Regarding_kg['ou'])))
                self.name_input_st.setText(str(Regarding_lb * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_lb * float(Regarding_kg['ct'])))
            elif len(self.name_ou) > 0:
                Regarding_ou = float(self.name_ou) / float(Regarding_kg['ou'])
                self.name_input_kg.setText(str(Regarding_ou))
                self.name_input_mg.setText(str(Regarding_ou * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_ou * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_ou * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_ou * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_ou * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_ou * float(Regarding_kg['lb'])))
                self.name_input_st.setText(str(Regarding_ou * float(Regarding_kg['st'])))
                self.name_input_ct.setText(str(Regarding_ou * float(Regarding_kg['ct'])))
            elif len(self.name_ct) > 0:
                Regarding_ct = float(self.name_ct) / float(Regarding_kg['ct'])
                self.name_input_kg.setText(str(Regarding_ct))
                self.name_input_mg.setText(str(Regarding_ct * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_ct * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_ct * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_ct * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_ct * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_ct * float(Regarding_kg['lb'])))
                self.name_input_st.setText(str(Regarding_ct * float(Regarding_kg['st'])))
                self.name_input_ou.setText(str(Regarding_ct * float(Regarding_kg['ou'])))

            elif len(self.name_st) > 0:
                Regarding_st = float(self.name_st) / float(Regarding_kg['st'])
                self.name_input_kg.setText(str(Regarding_st))
                self.name_input_mg.setText(str(Regarding_st * float(Regarding_kg['mg'])))
                self.name_input_g.setText(str(Regarding_st * float(Regarding_kg['g'])))
                self.name_input_t.setText(str(Regarding_st * float(Regarding_kg['t'])))
                self.name_input_uk.setText(str(Regarding_st * float(Regarding_kg['uk'])))
                self.name_input_us.setText(str(Regarding_st * float(Regarding_kg['us'])))
                self.name_input_lb.setText(str(Regarding_st * float(Regarding_kg['lb'])))
                self.name_input_ct.setText(str(Regarding_st * float(Regarding_kg['ct'])))
                self.name_input_ou.setText(str(Regarding_st * float(Regarding_kg['ou'])))
        except:
            self.clear()
            self.name_label.show()

    def clear(self):
        self.name_input_kg.setText('')
        self.name_input_mg.setText('')
        self.name_input_g.setText('')
        self.name_input_t.setText('')
        self.name_input_lb.setText('')
        self.name_input_ou.setText('')
        self.name_input_uk.setText('')
        self.name_input_us.setText('')
        self.name_input_st.setText('')
        self.name_input_ct.setText('')


class Choice_of_Action(QMainWindow):
    def __init__(self):  # Этот класс нужен для запуска той функции, которую выбрал пользователь
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 100, 120)
        self.setWindowTitle('Диалоговые окна')
        
        self.button = QPushButton(self)
        self.button.move(10, 10)
        self.button.resize(100, 100)
        self.button.setText("Click on me")
        self.button.clicked.connect(self.run)
        
    def run(self):
        country, ok_pressed = QInputDialog.getItem(
            self, "Выберите продукт использования", "Что будешь использовать?",
            ("Калькулятор", "Валюта", "Расcтояние", "Масса"), 1, False)
        if country == "Калькулятор":  # Какое действие выбрал пользователь, тот класс и запускается
            self.bobs = Choice_of_Action()
            self.bobs.show()
            self.bobs = Arithmometer()
            self.bobs.show()
        if country == "Валюта":
            self.bobs = Choice_of_Action()
            self.bobs.show()
            self.bobs = Currency()
            self.bobs.show()
        if country == "Расcтояние":
            self.bobs = Choice_of_Action()
            self.bobs.show()                
            self.bobs = Distance()
            self.bobs.show()
        if country == "Масса":
            self.bobs = Choice_of_Action()
            self.bobs.show()
            self.bobs = Weight()
            self.bobs.show()            

if __name__ == '__main__':  # Запускаем сначала класс в котором пользователь выбирает действие
    app = QApplication(sys.argv)
    ex = Choice_of_Action()
    ex.show()
    sys.exit(app.exec())