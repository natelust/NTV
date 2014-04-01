# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threeD.ui'
#
# Created: Mon Feb 24 15:39:35 2014
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

class Ui_ThreeD(object):
    def setupUi(self, ThreeD):
        ThreeD.setObjectName(_fromUtf8("ThreeD"))
        ThreeD.resize(188, 326)
        self.horizontalLayout = QtGui.QHBoxLayout(ThreeD)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(ThreeD)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.fnumber = QtGui.QLabel(self.groupBox)
        self.fnumber.setMinimumSize(QtCore.QSize(0, 0))
        self.fnumber.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fnumber.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fnumber.setFrameShadow(QtGui.QFrame.Sunken)
        self.fnumber.setText(_fromUtf8(""))
        self.fnumber.setObjectName(_fromUtf8("fnumber"))
        self.verticalLayout_2.addWidget(self.fnumber)
        self.play = QtGui.QCommandLinkButton(self.groupBox)
        self.play.setMinimumSize(QtCore.QSize(0, 0))
        self.play.setMaximumSize(QtCore.QSize(100, 40))
        self.play.setAutoFillBackground(True)
        self.play.setDefault(True)
        self.play.setObjectName(_fromUtf8("play"))
        self.verticalLayout_2.addWidget(self.play)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.delay = QtGui.QLineEdit(self.groupBox)
        self.delay.setMinimumSize(QtCore.QSize(0, 0))
        self.delay.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delay.setObjectName(_fromUtf8("delay"))
        self.verticalLayout_2.addWidget(self.delay)
        self.zbutton = QtGui.QRadioButton(self.groupBox)
        self.zbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.zbutton.setChecked(True)
        self.zbutton.setObjectName(_fromUtf8("zbutton"))
        self.verticalLayout_2.addWidget(self.zbutton)
        self.xbutton = QtGui.QRadioButton(self.groupBox)
        self.xbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.xbutton.setObjectName(_fromUtf8("xbutton"))
        self.verticalLayout_2.addWidget(self.xbutton)
        self.ybutton = QtGui.QRadioButton(self.groupBox)
        self.ybutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ybutton.setObjectName(_fromUtf8("ybutton"))
        self.verticalLayout_2.addWidget(self.ybutton)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.clearbutton = QtGui.QPushButton(self.groupBox)
        self.clearbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.clearbutton.setObjectName(_fromUtf8("clearbutton"))
        self.verticalLayout_2.addWidget(self.clearbutton)
        self.horizontalLayout.addWidget(self.groupBox)
        self.fnumbar = QtGui.QSlider(ThreeD)
        self.fnumbar.setOrientation(QtCore.Qt.Vertical)
        self.fnumbar.setInvertedAppearance(True)
        self.fnumbar.setInvertedControls(True)
        self.fnumbar.setTickPosition(QtGui.QSlider.TicksBelow)
        self.fnumbar.setObjectName(_fromUtf8("fnumbar"))
        self.horizontalLayout.addWidget(self.fnumbar)

        self.retranslateUi(ThreeD)
        QtCore.QMetaObject.connectSlotsByName(ThreeD)

    def retranslateUi(self, ThreeD):
        ThreeD.setWindowTitle(_translate("ThreeD", "Form", None))
        self.label.setText(_translate("ThreeD", "Frame Number", None))
        self.play.setText(_translate("ThreeD", "play", None))
        self.label_3.setText(_translate("ThreeD", "Time Delay", None))
        self.delay.setText(_translate("ThreeD", "0.5", None))
        self.zbutton.setText(_translate("ThreeD", "Z-Axis", None))
        self.xbutton.setText(_translate("ThreeD", "X-Axis", None))
        self.ybutton.setText(_translate("ThreeD", "Y-Axis", None))
        self.label_2.setText(_translate("ThreeD", "Reset Scaling", None))
        self.clearbutton.setText(_translate("ThreeD", "Clear", None))

