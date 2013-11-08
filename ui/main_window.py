# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Sep 26 18:05:00 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxFormats = QtGui.QComboBox(self.centralwidget)
        self.comboBoxFormats.setGeometry(QtCore.QRect(390, 50, 191, 25))
        self.comboBoxFormats.setObjectName("comboBoxFormats")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.comboBoxFormats.addItem("")
        self.textEditDownload = QtGui.QTextEdit(self.centralwidget)
        self.textEditDownload.setGeometry(QtCore.QRect(10, 50, 371, 25))
        self.textEditDownload.setObjectName("textEditDownload")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label.setObjectName("label")
        self.btnDownload = QtGui.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(10, 90, 79, 31))
        self.btnDownload.setObjectName("btnDownload")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 121, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Youtube-dl-GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(0, QtGui.QApplication.translate("MainWindow", "H264 MP4 1080p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(1, QtGui.QApplication.translate("MainWindow", "H264 MP4 720p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(2, QtGui.QApplication.translate("MainWindow", "WebM 720p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(3, QtGui.QApplication.translate("MainWindow", "WebM 480p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(4, QtGui.QApplication.translate("MainWindow", "H264 MP4 480p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(5, QtGui.QApplication.translate("MainWindow", "H264 FLV 480p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(6, QtGui.QApplication.translate("MainWindow", "H264 FLV 360p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(7, QtGui.QApplication.translate("MainWindow", "H263 240p", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxFormats.setItemText(8, QtGui.QApplication.translate("MainWindow", "3GP video", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Download URL", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDownload.setText(QtGui.QApplication.translate("MainWindow", "Download!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Download Format", None, QtGui.QApplication.UnicodeUTF8))

