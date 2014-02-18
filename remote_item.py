# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote_item.ui'
#
# Created: Mon Feb 17 14:33:21 2014
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

class Ui_remote_item(object):
    def setupUi(self, remote_item):
        remote_item.setObjectName(_fromUtf8("remote_item"))
        remote_item.resize(400, 316)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(remote_item.sizePolicy().hasHeightForWidth())
        remote_item.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(remote_item)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalGroupBox = QtGui.QGroupBox(remote_item)
        self.verticalGroupBox.setObjectName(_fromUtf8("verticalGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalWidget = QtGui.QWidget(self.verticalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.name = QtGui.QLabel(self.horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.installbutton = QtGui.QPushButton(self.horizontalWidget)
        self.installbutton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.installbutton.setObjectName(_fromUtf8("installbutton"))
        self.horizontalLayout.addWidget(self.installbutton)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.label = QtGui.QLabel(self.verticalGroupBox)
        self.label.setMaximumSize(QtCore.QSize(16777215, 4))
        self.label.setFrameShape(QtGui.QFrame.HLine)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalWidget_2 = QtGui.QWidget(self.verticalGroupBox)
        self.horizontalWidget_2.setObjectName(_fromUtf8("horizontalWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.description = QtGui.QLabel(self.horizontalWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setMinimumSize(QtCore.QSize(0, 0))
        self.description.setFrameShape(QtGui.QFrame.NoFrame)
        self.description.setFrameShadow(QtGui.QFrame.Sunken)
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.horizontalLayout_2.addWidget(self.description)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.verticalLayout_2.addWidget(self.verticalGroupBox)

        self.retranslateUi(remote_item)
        QtCore.QMetaObject.connectSlotsByName(remote_item)

    def retranslateUi(self, remote_item):
        remote_item.setWindowTitle(_translate("remote_item", "Plugin", None))
        self.name.setText(_translate("remote_item", "Name", None))
        self.installbutton.setText(_translate("remote_item", "Install", None))
        self.description.setText(_translate("remote_item", "Description", None))

