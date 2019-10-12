# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 650)
        Dialog.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(174, 91, 221, 41))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 127);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(457, 102, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(174, 151, 221, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(174, 211, 221, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 270, 221, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(457, 151, 141, 41))
        self.textEdit.setObjectName("textEdit")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(457, 212, 141, 41))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(457, 271, 141, 41))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 370, 221, 71))
        self.pushButton.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 571, 51))
        self.label_5.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Topic"))
        self.label_2.setText(_translate("Dialog", "Description"))
        self.label_3.setText(_translate("Dialog", "Date"))
        self.label_4.setText(_translate("Dialog", "Time"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm:ss"))
        self.pushButton.setText(_translate("Dialog", "Update"))
        self.label_5.setText(_translate("Dialog", "Update Your Reminders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
