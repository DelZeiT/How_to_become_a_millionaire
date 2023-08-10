from PyQt5 import uic

balance = 0    # баланс
count_life = 3    # счетчик жизней


# функция открытия окна с вопросами
def open_question_window1():
    Form2, Window2 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/questions_window_ui.ui")
    global form2
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)

    # кнопки
    btn1 = form2.pushButton
    btn1.clicked.connect(clicked_btn1)

    btn2 = form2.pushButton_2
    btn2.clicked.connect(clicked_btn2)

    btn3 = form2.pushButton_3
    btn3.clicked.connect(clicked_btn3)

    btn4 = form2.pushButton_4
    btn4.clicked.connect(clicked_btn4)

    window2.exec_()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1():
    global balance
    balance += 100000
    form2.lineEdit_2.setText(str(balance))
    open_question_window2()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2():
    global count_life
    count_life -= 1
    form2.lineEdit.setText(str(count_life))
    open_question_window2()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3():
    global count_life
    count_life -= 1
    form2.lineEdit.setText(str(count_life))
    open_question_window2()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4():
    global count_life
    count_life -= 1
    form2.lineEdit.setText(str(count_life))
    open_question_window2()


# функция открытия окна со вторым вопросом
def open_question_window2():
    Form3, Window3 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window2_ui.ui")
    global form3
    window3 = Window3()
    form3 = Form3()
    form3.setupUi(window3)

    window3.exec()
