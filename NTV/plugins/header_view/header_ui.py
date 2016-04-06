# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'header.ui'
#
# Created: Sun Feb 16 20:57:45 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_header(object):
    def setupUi(self, header):
        header.setObjectName(_fromUtf8("header"))
        header.resize(503, 599)
        header.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(header)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cardlist = QtGui.QListWidget(header)
        self.cardlist.setObjectName(_fromUtf8("cardlist"))
        self.verticalLayout.addWidget(self.cardlist)
        self.okbutton = QtGui.QPushButton(header)
        self.okbutton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.okbutton.setObjectName(_fromUtf8("okbutton"))
        self.verticalLayout.addWidget(self.okbutton)

        self.retranslateUi(header)
        QtCore.QMetaObject.connectSlotsByName(header)

    def retranslateUi(self, header):
        header.setWindowTitle(_translate("header", "Header", None))
        self.okbutton.setText(_translate("header", "OK", None))

