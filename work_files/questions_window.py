from PyQt5 import uic
from PyQt5.QtWidgets import *


def open_questions_window():
    Form2, Window2 = uic.loadUiType("C:/_PYTHON_PROJECT_/How_to_become_millioner_py/ui_ui_files/questions_window_ui.ui")

    window2 = Window2()
    form2 = Form2()
    form2.setupUi(window2)


    window2.exec()