# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 432)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.labelEnterData = QtWidgets.QLabel(self.centralWidget)
        self.labelEnterData.setGeometry(QtCore.QRect(160, 125, 61, 21))
        self.labelEnterData.setObjectName("labelEnterData")
        self.buttonHour = QtWidgets.QPushButton(self.centralWidget)
        self.buttonHour.setGeometry(QtCore.QRect(220, 120, 71, 32))
        self.buttonHour.setObjectName("buttonHour")
        self.buttonDay = QtWidgets.QPushButton(self.centralWidget)
        self.buttonDay.setGeometry(QtCore.QRect(290, 120, 71, 32))
        self.buttonDay.setObjectName("buttonDay")
        self.buttonStart = QtWidgets.QPushButton(self.centralWidget)
        self.buttonStart.setGeometry(QtCore.QRect(190, 71, 113, 41))
        self.buttonStart.setObjectName("buttonStart")
        self.labelStartInfo = QtWidgets.QLabel(self.centralWidget)
        self.labelStartInfo.setGeometry(QtCore.QRect(300, 80, 71, 21))
        self.labelStartInfo.setObjectName("labelStartInfo")
        self.buttonStop = QtWidgets.QPushButton(self.centralWidget)
        self.buttonStop.setGeometry(QtCore.QRect(190, 160, 113, 41))
        self.buttonStop.setObjectName("buttonStop")
        self.textState = QtWidgets.QTextBrowser(self.centralWidget)
        self.textState.setGeometry(QtCore.QRect(120, 220, 271, 111))
        self.textState.setObjectName("textState")
        self.labelState = QtWidgets.QLabel(self.centralWidget)
        self.labelState.setGeometry(QtCore.QRect(120, 200, 71, 16))
        self.labelState.setObjectName("labelState")
        self.buttonQuit = QtWidgets.QPushButton(self.centralWidget)
        self.buttonQuit.setGeometry(QtCore.QRect(370, 360, 113, 32))
        self.buttonQuit.setObjectName("buttonQuit")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 161, 51))
        self.label.setObjectName("label")
        self.button_10s = QtWidgets.QPushButton(self.centralWidget)
        self.button_10s.setGeometry(QtCore.QRect(360, 120, 113, 32))
        self.button_10s.setObjectName("button_10s")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelEnterData.setText(_translate("MainWindow", "数据入库："))
        self.buttonHour.setText(_translate("MainWindow", "/hour"))
        self.buttonDay.setText(_translate("MainWindow", "/day"))
        self.buttonStart.setText(_translate("MainWindow", "start"))
        self.labelStartInfo.setText(_translate("MainWindow", "(默认/hour)"))
        self.buttonStop.setText(_translate("MainWindow", "stop"))
        self.labelState.setText(_translate("MainWindow", "状态显示栏："))
        self.buttonQuit.setText(_translate("MainWindow", "quit"))
        self.label.setText(_translate("MainWindow", "PM25及天气数据入库系统"))
        self.button_10s.setText(_translate("MainWindow", "/10s(测试)"))

