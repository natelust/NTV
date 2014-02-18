# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_item.ui'
#
# Created: Mon Feb 17 14:44:42 2014
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

class Ui_listitem(object):
    def setupUi(self, listitem):
        listitem.setObjectName(_fromUtf8("listitem"))
        listitem.resize(400, 316)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(listitem.sizePolicy().hasHeightForWidth())
        listitem.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(listitem)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalGroupBox = QtGui.QGroupBox(listitem)
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
        self.gridGroupBox = QtGui.QGroupBox(self.horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridGroupBox.sizePolicy().hasHeightForWidth())
        self.gridGroupBox.setSizePolicy(sizePolicy)
        self.gridGroupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.gridGroupBox)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridGroupBox)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.installedversion = QtGui.QLabel(self.gridGroupBox)
        self.installedversion.setMaximumSize(QtCore.QSize(16777215, 100))
        self.installedversion.setAutoFillBackground(True)
        self.installedversion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.installedversion.setFrameShadow(QtGui.QFrame.Raised)
        self.installedversion.setScaledContents(True)
        self.installedversion.setObjectName(_fromUtf8("installedversion"))
        self.gridLayout.addWidget(self.installedversion, 0, 1, 1, 1)
        self.latestversion = QtGui.QLabel(self.gridGroupBox)
        self.latestversion.setMaximumSize(QtCore.QSize(16777215, 100))
        self.latestversion.setAutoFillBackground(True)
        self.latestversion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.latestversion.setFrameShadow(QtGui.QFrame.Raised)
        self.latestversion.setScaledContents(True)
        self.latestversion.setObjectName(_fromUtf8("latestversion"))
        self.gridLayout.addWidget(self.latestversion, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.gridGroupBox)
        self.verticalLayout.addWidget(self.horizontalWidget)
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
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.horizontalLayout_2.addWidget(self.description)
        self.verticalFrame = QtGui.QFrame(self.horizontalWidget_2)
        self.verticalFrame.setObjectName(_fromUtf8("verticalFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.updatebutton = QtGui.QPushButton(self.verticalFrame)
        self.updatebutton.setEnabled(False)
        self.updatebutton.setMaximumSize(QtCore.QSize(85, 16777215))
        self.updatebutton.setObjectName(_fromUtf8("updatebutton"))
        self.verticalLayout_3.addWidget(self.updatebutton)
        self.uninstallbutton = QtGui.QPushButton(self.verticalFrame)
        self.uninstallbutton.setEnabled(False)
        self.uninstallbutton.setMaximumSize(QtCore.QSize(85, 16777215))
        self.uninstallbutton.setObjectName(_fromUtf8("uninstallbutton"))
        self.verticalLayout_3.addWidget(self.uninstallbutton)
        self.horizontalLayout_2.addWidget(self.verticalFrame)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.verticalLayout_2.addWidget(self.verticalGroupBox)

        self.retranslateUi(listitem)
        QtCore.QMetaObject.connectSlotsByName(listitem)

    def retranslateUi(self, listitem):
        listitem.setWindowTitle(_translate("listitem", "Plugin", None))
        self.name.setText(_translate("listitem", "Name", None))
        self.label_3.setText(_translate("listitem", "Latest Version", None))
        self.label_2.setText(_translate("listitem", "Installed Version", None))
        self.installedversion.setText(_translate("listitem", "TextLabel", None))
        self.latestversion.setText(_translate("listitem", "TextLabel", None))
        self.description.setText(_translate("listitem", "Description", None))
        self.updatebutton.setText(_translate("listitem", "Update", None))
        self.uninstallbutton.setText(_translate("listitem", "Uninstall", None))

