# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yusuk/Pyside2UicFrontEnd/PUFE.ui',
# licensing of 'C:/Users/yusuk/Pyside2UicFrontEnd/PUFE.ui' applies.
#
# Created: Thu Oct  3 11:26:53 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 152)
        MainWindow.setMinimumSize(QtCore.QSize(1051, 152))
        MainWindow.setMaximumSize(QtCore.QSize(1051, 152))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(10, 10, 1031, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox1.setFont(font)
        self.groupBox1.setObjectName("groupBox1")
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit1.setGeometry(QtCore.QRect(10, 20, 811, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton2.setGeometry(QtCore.QRect(930, 20, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton1 = QtWidgets.QPushButton(self.groupBox1)
        self.pushButton1.setGeometry(QtCore.QRect(830, 20, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.groupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox2.setGeometry(QtCore.QRect(10, 80, 1031, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox2.setFont(font)
        self.groupBox2.setObjectName("groupBox2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.groupBox2)
        self.lineEdit2.setGeometry(QtCore.QRect(10, 20, 711, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton5 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton5.setGeometry(QtCore.QRect(930, 20, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton4 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton4.setGeometry(QtCore.QRect(830, 20, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton3 = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton3.setGeometry(QtCore.QRect(730, 20, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Pyside2-uic Front End", None, -1))
        self.groupBox1.setTitle(QtWidgets.QApplication.translate("MainWindow", "LOCATION OF pyside2-uic.bat", None, -1))
        self.pushButton2.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
        self.pushButton1.setText(QtWidgets.QApplication.translate("MainWindow", "RESET", None, -1))
        self.groupBox2.setTitle(QtWidgets.QApplication.translate("MainWindow", "LOCATION OF UI FILE", None, -1))
        self.pushButton5.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
        self.pushButton4.setText(QtWidgets.QApplication.translate("MainWindow", "EXEC", None, -1))
        self.pushButton3.setText(QtWidgets.QApplication.translate("MainWindow", "RESET", None, -1))

