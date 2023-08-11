from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

balance = 0    # баланс
count_life = 3    # счетчик жизней


# функция открытия окна с вопросами
def open_question_window1():
    app1 = QApplication([])
    Form, Window = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/questions_window_ui.ui")
    global form
    window = Window()
    form = Form()
    form.setupUi(window)

    # кнопки с вариантами ответа на первый вопрос
    btn1 = form.pushButton
    btn1.clicked.connect(clicked_btn1)

    btn2 = form.pushButton_2
    btn2.clicked.connect(clicked_btn2)

    btn3 = form.pushButton_3
    btn3.clicked.connect(clicked_btn3)

    btn4 = form.pushButton_4
    btn4.clicked.connect(clicked_btn4)

    window.exec_()
    app1.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1():
    global balance
    balance += 100000
    form.lineEdit_2.setText(str(balance))
    open_question_window2()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2():
    global count_life
    count_life -= 1
    form.lineEdit.setText(str(count_life))
    open_question_window2()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3():
    global count_life
    count_life -= 1
    form.lineEdit.setText(str(count_life))
    open_question_window2()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4():
    global count_life
    count_life -= 1
    form.lineEdit.setText(str(count_life))
    open_question_window2()


# функция открытия окна со вторым вопросом
def open_question_window2():
    app2 = QApplication([])
    Form2, Window2 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window2_ui.ui")
    global form2
    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)

    global balance
    global count_life
    form2.lineEdit.setText(str(count_life))
    form2.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на второй вопрос
    btn1_2 = form2.pushButton       # Норвегия
    btn1_2.clicked.connect(clicked_btn1_2)

    btn2_2 = form2.pushButton_2     # Канада
    btn2_2.clicked.connect(clicked_btn2_2)

    btn3_2 = form2.pushButton_3     # Япония
    btn3_2.clicked.connect(clicked_btn3_2)

    btn4_2 = form2.pushButton_4     # Аргентина
    btn4_2.clicked.connect(clicked_btn4_2)

    window2.exec()
    app2.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_2():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form2.lineEdit.setText(str(count_life))
    open_question_window3()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_2():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form2.lineEdit.setText(str(count_life))
    open_question_window3()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn3_2():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    form2.lineEdit.setText(str(count_life))
    open_question_window3()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn4_2():
    global balance
    balance += 100000
    form2.lineEdit_2.setText(str(balance))
    open_question_window3()


# функция открытия окна с третьим вопросом
def open_question_window3():
    app3 = QApplication([])
    Form3, Window3 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window3_ui.ui")
    global form3
    window3 = Window3()
    form3 = Form3()
    form3.setupUi(window3)

    global balance
    global count_life
    form3.lineEdit.setText(str(count_life))
    form3.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на третий вопрос
    btn1_3 = form3.pushButton       # Медведь
    btn1_3.clicked.connect(clicked_btn1_3)

    btn2_3 = form3.pushButton_2     # Бегемот
    btn2_3.clicked.connect(clicked_btn2_3)

    btn3_3 = form3.pushButton_3     # Лев
    btn3_3.clicked.connect(clicked_btn3_3)

    btn4_3 = form3.pushButton_4     # Жираф
    btn4_3.clicked.connect(clicked_btn4_3)

    window3.exec()
    app3.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_3():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form3.lineEdit.setText(str(count_life))
        open_question_window4()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_3():
    global balance
    balance += 100000
    form3.lineEdit_2.setText(str(balance))
    open_question_window4()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_3():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form3.lineEdit.setText(str(count_life))
        open_question_window4()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_3():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form3.lineEdit.setText(str(count_life))
        open_question_window4()


# функция открытия окна с четвертым вопросом
def open_question_window4():
    app4 = QApplication([])
    Form4, Window4 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window4_ui.ui")
    global form4
    window4 = Window4()
    form4 = Form4()
    form4.setupUi(window4)

    global balance
    global count_life
    form4.lineEdit.setText(str(count_life))
    form4.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на четвертый вопрос
    btn1_4 = form4.pushButton
    btn1_4.clicked.connect(clicked_btn1_4)

    btn2_4 = form4.pushButton_2
    btn2_4.clicked.connect(clicked_btn2_4)

    btn3_4 = form4.pushButton_3
    btn3_4.clicked.connect(clicked_btn3_4)

    btn4_4 = form4.pushButton_4
    btn4_4.clicked.connect(clicked_btn4_4)

    window4.exec()
    app4.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_4():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form4.lineEdit.setText(str(count_life))
        open_question_window5()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_4():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form4.lineEdit.setText(str(count_life))
        open_question_window5()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_4():
    global balance
    balance += 100000
    form4.lineEdit_2.setText(str(balance))
    open_question_window5()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_4():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form4.lineEdit.setText(str(count_life))
        open_question_window5()


# функция открытия окна с пятым вопросом
def open_question_window5():
    app5 = QApplication([])
    Form5, Window5 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window5_ui.ui")
    global form5
    window5 = Window5()
    form5 = Form5()
    form5.setupUi(window5)

    global balance
    global count_life
    form5.lineEdit.setText(str(count_life))
    form5.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на пятый вопрос
    btn1_5 = form5.pushButton
    btn1_5.clicked.connect(clicked_btn1_5)

    btn2_5 = form5.pushButton_2
    btn2_5.clicked.connect(clicked_btn2_5)

    btn3_5 = form5.pushButton_3
    btn3_5.clicked.connect(clicked_btn3_5)

    btn4_5 = form5.pushButton_4
    btn4_5.clicked.connect(clicked_btn4_5)

    window5.exec()
    app5.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_5():
    global balance
    balance += 100000
    form5.lineEdit_2.setText(str(balance))
    open_question_window6()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_5():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form5.lineEdit.setText(str(count_life))
        open_question_window6()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_5():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form5.lineEdit.setText(str(count_life))
        open_question_window6()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_5():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form5.lineEdit.setText(str(count_life))
        open_question_window6()


# функция открытия окна с шестым вопросом
def open_question_window6():
    app6 = QApplication([])
    Form6, Window6 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window6_ui.ui")
    global form6
    window6 = Window6()
    form6 = Form6()
    form6.setupUi(window6)

    global balance
    global count_life
    form6.lineEdit.setText(str(count_life))
    form6.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на шестой вопрос
    btn1_6 = form6.pushButton
    btn1_6.clicked.connect(clicked_btn1_6)

    btn2_6 = form6.pushButton_2
    btn2_6.clicked.connect(clicked_btn2_6)

    btn3_6 = form6.pushButton_3
    btn3_6.clicked.connect(clicked_btn3_6)

    btn4_6 = form6.pushButton_4
    btn4_6.clicked.connect(clicked_btn4_6)

    window6.exec()
    app6.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_6():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form6.lineEdit.setText(str(count_life))
        open_question_window7()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_6():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form6.lineEdit.setText(str(count_life))
        open_question_window7()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_6():
    global balance
    balance += 100000
    form6.lineEdit_2.setText(str(balance))
    open_question_window7()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_6():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form6.lineEdit.setText(str(count_life))
        open_question_window7()


# функция открытия окна с седьмым вопросом
def open_question_window7():
    app7 = QApplication([])
    Form7, Window7 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window7_ui.ui")
    global form7
    window7 = Window7()
    form7 = Form7()
    form7.setupUi(window7)

    global balance
    global count_life
    form7.lineEdit.setText(str(count_life))
    form7.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на седьмой вопрос
    btn1_7 = form7.pushButton
    btn1_7.clicked.connect(clicked_btn1_7)

    btn2_7 = form7.pushButton_2
    btn2_7.clicked.connect(clicked_btn2_7)

    btn3_7 = form7.pushButton_3
    btn3_7.clicked.connect(clicked_btn3_7)

    btn4_7 = form7.pushButton_4
    btn4_7.clicked.connect(clicked_btn4_7)

    window7.exec()
    app7.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_7():
    global balance
    balance += 100000
    form7.lineEdit_2.setText(str(balance))
    open_question_window8()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_7():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form7.lineEdit.setText(str(count_life))
        open_question_window8()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_7():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form7.lineEdit.setText(str(count_life))
        open_question_window8()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_7():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form7.lineEdit.setText(str(count_life))
        open_question_window8()


# функция открытия окна с восьмым вопросом
def open_question_window8():
    app8 = QApplication([])
    Form8, Window8 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window8_ui.ui")
    global form8
    window8 = Window8()
    form8 = Form8()
    form8.setupUi(window8)

    global balance
    global count_life
    form8.lineEdit.setText(str(count_life))
    form8.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на восьмой вопрос
    btn1_8 = form8.pushButton
    btn1_8.clicked.connect(clicked_btn1_8)

    btn2_8 = form8.pushButton_2
    btn2_8.clicked.connect(clicked_btn2_8)

    btn3_8 = form8.pushButton_3
    btn3_8.clicked.connect(clicked_btn3_8)

    btn4_8 = form8.pushButton_4
    btn4_8.clicked.connect(clicked_btn4_8)

    window8.exec()
    app8.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_8():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form8.lineEdit.setText(str(count_life))
        open_question_window9()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_8():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form8.lineEdit.setText(str(count_life))
        open_question_window9()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_8():
    global balance
    balance += 100000
    form8.lineEdit_2.setText(str(balance))
    open_question_window9()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_8():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form8.lineEdit.setText(str(count_life))
        open_question_window9()


# функция открытия окна с девятым вопросом
def open_question_window9():
    app9 = QApplication([])
    Form9, Window9 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window9_ui.ui")
    global form9
    window9 = Window9()
    form9 = Form9()
    form9.setupUi(window9)

    global balance
    global count_life
    form9.lineEdit.setText(str(count_life))
    form9.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на девятый вопрос
    btn1_9 = form9.pushButton
    btn1_9.clicked.connect(clicked_btn1_9)

    btn2_9 = form9.pushButton_2
    btn2_9.clicked.connect(clicked_btn2_9)

    btn3_9 = form9.pushButton_3
    btn3_9.clicked.connect(clicked_btn3_9)

    btn4_9 = form9.pushButton_4
    btn4_9.clicked.connect(clicked_btn4_9)

    window9.exec()
    app9.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_9():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form9.lineEdit.setText(str(count_life))
        open_question_window10()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_9():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form9.lineEdit.setText(str(count_life))
        open_question_window10()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_9():
    global balance
    balance += 100000
    form9.lineEdit_2.setText(str(balance))
    open_question_window10()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_9():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form9.lineEdit.setText(str(count_life))
        open_question_window10()


# функция открытия окна с десятым вопросом
def open_question_window10():
    app10 = QApplication([])
    Form10, Window10 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window10_ui.ui")
    global form10
    window10 = Window10()
    form10 = Form10()
    form10.setupUi(window10)

    global balance
    global count_life
    form10.lineEdit.setText(str(count_life))
    form10.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на десятый вопрос
    btn1_10 = form10.pushButton
    btn1_10.clicked.connect(clicked_btn1_10)

    btn2_10 = form10.pushButton_2
    btn2_10.clicked.connect(clicked_btn2_10)

    btn3_10 = form10.pushButton_3
    btn3_10.clicked.connect(clicked_btn3_10)

    btn4_10 = form10.pushButton_4
    btn4_10.clicked.connect(clicked_btn4_10)

    window10.exec()
    app10.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_10():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form10.lineEdit.setText(str(count_life))
        open_question_window11()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_10():
    global balance
    balance += 100000
    if balance == 1000000:
        victory_window()
    form10.lineEdit_2.setText(str(balance))
    open_question_window11()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_10():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form10.lineEdit.setText(str(count_life))
        open_question_window11()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_10():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form10.lineEdit.setText(str(count_life))
        open_question_window11()


# функция открытия окна с одиннадцатым вопросом
def open_question_window11():
    app11 = QApplication([])
    Form11, Window11 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window11_ui.ui")
    global form11
    window11 = Window11()
    form11 = Form11()
    form11.setupUi(window11)

    global balance
    global count_life
    form11.lineEdit.setText(str(count_life))
    form11.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на одиннадцатый вопрос
    btn1_11 = form11.pushButton
    btn1_11.clicked.connect(clicked_btn1_11)

    btn2_11 = form11.pushButton_2
    btn2_11.clicked.connect(clicked_btn2_11)

    btn3_11 = form11.pushButton_3
    btn3_11.clicked.connect(clicked_btn3_11)

    btn4_11 = form11.pushButton_4
    btn4_11.clicked.connect(clicked_btn4_11)

    window11.exec()
    app11.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_11():
    global balance
    balance += 100000
    if balance == 1000000:
        victory_window()
    form11.lineEdit_2.setText(str(balance))
    open_question_window12()


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_11():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form11.lineEdit.setText(str(count_life))
        open_question_window12()


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_11():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form11.lineEdit.setText(str(count_life))
        open_question_window12()


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_11():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form11.lineEdit.setText(str(count_life))
        open_question_window12()


# функция открытия окна с двенацдатым вопросом
def open_question_window12():
    app12 = QApplication([])
    Form12, Window12 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/question_window12_ui.ui")
    global form12
    window12 = Window12()
    form12 = Form12()
    form12.setupUi(window12)

    global balance
    global count_life
    form12.lineEdit.setText(str(count_life))
    form12.lineEdit_2.setText(str(balance))

    # кнопки с вариантами ответа на двенадцатый вопрос
    btn1_12 = form12.pushButton
    btn1_12.clicked.connect(clicked_btn1_12)

    btn2_12 = form12.pushButton_2
    btn2_12.clicked.connect(clicked_btn2_12)

    btn3_12 = form12.pushButton_3
    btn3_12.clicked.connect(clicked_btn3_12)

    btn4_12 = form12.pushButton_4
    btn4_12.clicked.connect(clicked_btn4_12)

    window12.exec()
    app12.exec()


# функция нажатия кнопки с первым вариантом ответа
def clicked_btn1_12():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form12.lineEdit.setText(str(count_life))


# функция нажатия кнопки со вторым вариантом ответа
def clicked_btn2_12():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form12.lineEdit.setText(str(count_life))


# функция нажатия кнопки с третьим вариантом ответа
def clicked_btn3_12():
    global count_life
    global balance
    count_life -= 1
    balance -= 100000
    if count_life <= 0:
        defeat_window()
    else:
        form12.lineEdit.setText(str(count_life))


# функция нажатия кнопки с четвертым вариантом ответа
def clicked_btn4_12():
    global balance
    balance += 100000
    if balance == 1000000:
        victory_window()
    form12.lineEdit_2.setText(str(balance))


# функция окна с поздравлениями
def victory_window():
    appV = QApplication([])
    FormV, WindowV = uic.loadUiType(
        "C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/victory_window_ui.ui")
    windowV = WindowV()
    formV = FormV()
    formV.setupUi(windowV)

    windowV.exec()
    appV.exec()


def defeat_window():
    appD = QApplication([])
    FormD, WindowD = uic.loadUiType(
        "C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/defeat_window_ui.ui")
    windowD = WindowD()
    formD = FormD()
    formD.setupUi(windowD)

    windowD.exec()
    appD.exec()
