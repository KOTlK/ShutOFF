# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shutdown.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 469)
        MainWindow.setStyleSheet("background-color:#101212")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.turnOff = QtWidgets.QPushButton(self.centralwidget)
        self.turnOff.setGeometry(QtCore.QRect(80, 220, 201, 61))
        self.turnOff.setStyleSheet("background-color:#373E3E;\n"
"font: 16px serif;\n"
"color:#C4C4C4;")
        self.turnOff.setObjectName("turnOff")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(80, 310, 201, 61))
        self.cancel.setStyleSheet("background-color:#373E3E;\n"
"font: 16px serif;\n"
"color:#C4C4C4;")
        self.cancel.setObjectName("cancel")
        self.timer = QtWidgets.QTextEdit(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(80, 110, 201, 31))
        self.timer.setStyleSheet("background-color: #7C8383;\n"
"font: 16px serif;")
        self.timer.setObjectName("timer")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 70, 141, 31))
        self.textBrowser.setStyleSheet("background-color:#101212;\n"
"border: no")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.turnOff.setText(_translate("MainWindow", "Turn OFF PC"))
        self.cancel.setText(_translate("MainWindow", "Cancel shutdown"))
        self.timer.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.timer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'serif\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Set your time here</span></p></body></html>"))
