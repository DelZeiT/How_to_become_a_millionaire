from PyQt5 import uic
from PyQt5.QtWidgets import *
from questions_window import open_question_window1
Form, Window = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/start_window_ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


# функция открытия окна с вопросами
def start_questions_window():
    open_question_window1()


form.pushButton.clicked.connect(start_questions_window)


window.show()
app.exec()