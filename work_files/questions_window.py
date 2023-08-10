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

    # кнопки с вариантами ответа на первый вопрос
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

    global balance
    global count_life
    form3.lineEdit.setText(str(count_life))
    form3.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на второй вопрос
    btn1_2 = form3.pushButton       # Норвегия
    btn1_2.clicked.connect(clicked_btn1_2)

    btn2_2 = form3.pushButton_2     # Канада
    btn2_2.clicked.connect(clicked_btn2_2)

    btn3_2 = form3.pushButton_3     # Япония
    btn3_2.clicked.connect(clicked_btn3_2)

    btn4_2 = form3.pushButton_4     # Аргентина
    btn4_2.clicked.connect(clicked_btn4_2)

    window3.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_2():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form3.lineEdit.setText(str(count_life))
    open_question_window3()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_2():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form3.lineEdit.setText(str(count_life))
    open_question_window3()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn3_2():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form3.lineEdit.setText(str(count_life))
    open_question_window3()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn4_2():
    global balance
    balance += 100000
    form3.lineEdit_2.setText(str(balance))
    open_question_window3()


# функция открытия окна с третьим вопросом
def open_question_window3():
    Form4, Window4 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window3_ui.ui")
    global form4
    window4 = Window4()
    form4 = Form4()
    form4.setupUi(window4)

    global balance
    global count_life
    form4.lineEdit.setText(str(count_life))
    form4.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на третий вопрос
    btn1_3 = form4.pushButton       # Медведь
    btn1_3.clicked.connect(clicked_btn1_3)

    btn2_3 = form4.pushButton_2     # Бегемот
    btn2_3.clicked.connect(clicked_btn2_3)

    btn3_3 = form4.pushButton_3     # Лев
    btn3_3.clicked.connect(clicked_btn3_3)

    btn4_3 = form4.pushButton_4     # Жираф
    btn4_3.clicked.connect(clicked_btn4_3)

    window4.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_3():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form4.lineEdit.setText(str(count_life))
    open_question_window4()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_3():
    global balance
    balance += 100000
    form4.lineEdit_2.setText(str(balance))
    open_question_window4()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_3():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form4.lineEdit.setText(str(count_life))
    open_question_window4()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_3():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form4.lineEdit.setText(str(count_life))
    open_question_window4()


# функция открытия окна с четвертым вопросом
def open_question_window4():
    Form5, Window5 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window3_ui.ui")
    global form5
    window5 = Window5()
    form5 = Form5()
    form4.setupUi(window5)

    global balance
    global count_life
    form4.lineEdit.setText(str(count_life))
    form4.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на третий вопрос
    btn1_4 = form5.pushButton       # Медведь
    btn1_4.clicked.connect(clicked_btn1_4)

    btn2_4 = form4.pushButton_2     # Бегемот
    btn2_4.clicked.connect(clicked_btn2_4)

    btn3_4 = form4.pushButton_3     # Лев
    btn3_4.clicked.connect(clicked_btn3_4)

    btn4_4 = form4.pushButton_4     # Жираф
    btn4_4.clicked.connect(clicked_btn4_4)

    window5.exec()

# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_4():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form4.lineEdit.setText(str(count_life))
    # open_question_window5()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_4():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form4.lineEdit.setText(str(count_life))
    # open_question_window5()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_4():
    global balance
    balance += 100000
    form4.lineEdit_2.setText(str(balance))
    # open_question_window5()

# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_4():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form4.lineEdit.setText(str(count_life))
    # open_question_window5()
