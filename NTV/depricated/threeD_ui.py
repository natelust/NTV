# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threeD.ui'
#
# Created: Wed Jan 22 14:55:07 2014
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

class Ui_threeD(object):
    def setupUi(self, threeD):
        threeD.setObjectName(_fromUtf8("threeD"))
        threeD.resize(426, 83)
        self.verticalLayout = QtGui.QVBoxLayout(threeD)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fnumbar = QtGui.QSlider(threeD)
        self.fnumbar.setOrientation(QtCore.Qt.Horizontal)
        self.fnumbar.setTickPosition(QtGui.QSlider.TicksBelow)
        self.fnumbar.setObjectName(_fromUtf8("fnumbar"))
        self.verticalLayout.addWidget(self.fnumbar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(threeD)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.fnumber = QtGui.QLabel(threeD)
        self.fnumber.setMinimumSize(QtCore.QSize(50, 0))
        self.fnumber.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fnumber.setFrameShadow(QtGui.QFrame.Sunken)
        self.fnumber.setText(_fromUtf8(""))
        self.fnumber.setObjectName(_fromUtf8("fnumber"))
        self.horizontalLayout.addWidget(self.fnumber)
        self.play = QtGui.QCommandLinkButton(threeD)
        self.play.setMinimumSize(QtCore.QSize(0, 41))
        self.play.setMaximumSize(QtCore.QSize(85, 16777215))
        self.play.setObjectName(_fromUtf8("play"))
        self.horizontalLayout.addWidget(self.play)
        self.label_3 = QtGui.QLabel(threeD)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.delay = QtGui.QLineEdit(threeD)
        self.delay.setMinimumSize(QtCore.QSize(40, 0))
        self.delay.setObjectName(_fromUtf8("delay"))
        self.horizontalLayout.addWidget(self.delay)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(threeD)
        QtCore.QMetaObject.connectSlotsByName(threeD)

    def retranslateUi(self, threeD):
        threeD.setWindowTitle(_translate("threeD", "3D Navigator", None))
        self.label.setText(_translate("threeD", "Frame Number", None))
        self.play.setText(_translate("threeD", "play", None))
        self.label_3.setText(_translate("threeD", "Time Delay", None))
        self.delay.setText(_translate("threeD", "0.5", None))

