# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questions_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(693, 272)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 681, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(570, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 200, 231, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 200, 221, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 150, 221, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 100, 171, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_life = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_life.setEnabled(False)
        self.lineEdit_life.setGeometry(QtCore.QRect(40, 30, 31, 22))
        self.lineEdit_life.setObjectName("lineEdit")
        self.lineEdit_balance = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_balance.setEnabled(False)
        self.lineEdit_balance.setGeometry(QtCore.QRect(570, 30, 71, 22))
        self.lineEdit_balance.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вопрос №1"))
        self.label.setText(_translate("Dialog", "Какую фамилию носил известный физик и математик Альберт? "))
        self.label_2.setText(_translate("Dialog", "Жизни:"))
        self.label_3.setText(_translate("Dialog", "Баланс:"))
        self.pushButton.setText(_translate("Dialog", "a) Эйнштейн "))
        self.pushButton_2.setText(_translate("Dialog", "b) Кюри "))
        self.pushButton_3.setText(_translate("Dialog", "d) Ньютон"))
        self.pushButton_4.setText(_translate("Dialog", " c) Тесла "))
        self.label_4.setText(_translate("Dialog", "Стоимость вопроса: 100000"))
        self.lineEdit_life.setText(_translate("Dialog", "3"))
        self.lineEdit_balance.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())