# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloaderUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Downloader):
        Downloader.setObjectName(_fromUtf8("Downloader"))
        Downloader.resize(391, 72)
        self.lineEdit = QtGui.QLineEdit(Downloader)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 271, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.checkBox = QtGui.QCheckBox(Downloader)
        self.checkBox.setGeometry(QtCore.QRect(290, 30, 16, 31))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton = QtGui.QPushButton(Downloader)
        self.pushButton.setGeometry(QtCore.QRect(310, 30, 75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Downloader)
        self.label.setGeometry(QtCore.QRect(20, 3, 351, 20))
        self.label.setText(_fromUtf8("https://www.youtube.com/watch?v=IdneKLhsWOQ \n asdasdasdasdasds"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Downloader)
        QtCore.QMetaObject.connectSlotsByName(Downloader)

    def retranslateUi(self, Downloader):
        Downloader.setWindowTitle(_translate("Downloader", "Awesome Downloader", None))
        self.pushButton.setText(_translate("Downloader", "Download", None))

