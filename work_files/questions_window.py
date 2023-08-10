from PyQt5 import uic
from PyQt5.QtWidgets import *


# функция открытия окна с вопросами
def open_question_window1():
    Form2, Window2 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/questions_window_ui.ui")

    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)
    window2.exec()

    balance = 0
    count_life = 3

    # кнопки
    btn1 = form2.pushButton
    btn1.clicked.connect(clicked_btn1)

    btn2 = form2.pushButton_2
    btn2.clicked.connect(clicked_btn2)

    btn3 = form2.pushButton_3
    btn3.clicked.connect(clicked_btn3)

    btn4 = form2.pushButton_4
    btn4.clicked.connect(clicked_btn4)


def clicked_btn1(balance, form2):
    balance += 100000
    form2.lineEdit_balance.insert(balance)
    open_question_window2()


def clicked_btn2():
    open_question_window2()


def clicked_btn3():
    open_question_window2()


def clicked_btn4():
    open_question_window2()


def open_question_window2():
    Form3, Window3 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window2_ui.ui")

    window3 = Window3()
    form3 = Form3()
    form3.setupUi(window3)

    window3.exec()
