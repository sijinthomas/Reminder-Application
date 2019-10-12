# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reminder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
import threading
import datetime
from PyQt5.QtCore import pyqtSignal
import sqlite3
import time
from viewrecords import Ui_Dialog2
from update import Ui_Dialog3
thr=""

class Ui_Dialog(object):
    
                
    def notify(self):
        #print("hello")
        date=""
        rtime=""
        topic=""
        tid=""
        connection=sqlite3.connect("reminder.db")
        query="SELECT * FROM record WHERE EXECUTED=0 LIMIT 1"
        result=connection.execute(query)
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print(row[0])
            date=row[2]
            rtime=row[3]
            topic=row[0]
            tid=(str(row[5]))
           # tid1=(str(tid))
        print(rtime,topic,tid)

        alarm_input =rtime
        while True:
            try:
                alarm_time = [int(n) for n in alarm_input.split(":")]
                if self.check_alarm_input(alarm_time):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("ERROR: Enter time in HH:MM or HH:MM:SS format")


        # Convert the alarm time from [H:M] or [H:M:S] to second    s
        seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
        alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
        # Get the current time of day in seconds
        now = datetime.datetime.now()
        current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
        time_diff_seconds = alarm_seconds - current_time_seconds
        # If time difference is negative, set alarm for next day
        if time_diff_seconds < 0:
            time_diff_seconds += 86400 # number of seconds in a day

        # Display the amount of time until the alarm goes off
        print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

        # Sleep until the alarm goes off
        time.sleep(time_diff_seconds)

        # Time for the alarm to go off
        print("Wake Up!")
        print("Wake Up!")
        self.showDialog(topic)
        query="UPDATE record set EXECUTED =1 WHERE tid=?"
        cursor = connection.cursor()
        print(type(tid))
        cursor.execute(query,(tid))
        connection.commit()
        print(result)
          
    def showChildWindow(self):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui_Dialog2()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def updateWindow(self):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui_Dialog3()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def check_alarm_input(self,alarm_time):
        if len(alarm_time) == 1: # [Hour] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0:
                return True
            if len(alarm_time) == 2: # [Hour:Minute] Format
                if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0:
                    return True
        elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                    alarm_time[2] < 60 and alarm_time[2] >= 0:
                return True
        return False
            
    def showDialog(self,topic):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(topic)
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            msgBox.done(1)

        
    def regvalue(self):
        TOPIC=self.textEdit.toPlainText()
        DECSRIPTION=(self.textEdit_2.toPlainText())
        DATE = self.dateEdit.date()
        DATE = DATE.toString("yyyy-MM-dd")
        TIME=self.timeEdit.time()
        TIME = TIME.toString("hh:mm:ss")
        EXECUTED=0
        print(TIME)


        connection = sqlite3.connect("reminder.db")
        connection.execute("INSERT INTO record VALUES(?,?,?,?,?,?)",(TOPIC,DECSRIPTION,DATE,TIME,EXECUTED,None))
        connection.commit()

      
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(901, 650)
        Dialog.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 85, 0);\n"
"")
        self.topicname = QtWidgets.QLabel(Dialog)
        self.topicname.setGeometry(QtCore.QRect(100, 95, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.topicname.setFont(font)
        self.topicname.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.topicname.setObjectName("topicname")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 150, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(255, 0, 127);\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 210, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 270, 231, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(352, 95, 121, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 150, 121, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 380, 211, 61))
        self.pushButton.clicked.connect(self.regvalue)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(352, 270, 118, 31))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(350, 210, 121, 31))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 19, 761, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 470, 211, 61))
        self.pushButton_2.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.notify)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 150, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.showChildWindow)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 200, 151, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.updateWindow)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.topicname.setText(_translate("Dialog", "Topic"))
        self.label.setText(_translate("Dialog", "Description"))
        self.label_2.setText(_translate("Dialog", "Date"))
        self.label_3.setText(_translate("Dialog", "Time"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm:yy"))
        self.label_4.setText(_translate("Dialog", "Set Your Reminders"))
        self.pushButton_2.setText(_translate("Dialog", "Start"))
        self.pushButton_3.setText(_translate("Dialog", "View Reminders"))
        self.pushButton_4.setText(_translate("Dialog", "Update Reminders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
