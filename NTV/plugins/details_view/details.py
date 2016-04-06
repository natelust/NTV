# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'details.ui'
#
# Created: Tue Feb 18 01:43:59 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(418, 580)
        Dialog.setMaximumSize(QtCore.QSize(800, 580))
        Dialog.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.xval = QtGui.QLabel(Dialog)
        self.xval.setFrameShape(QtGui.QFrame.StyledPanel)
        self.xval.setFrameShadow(QtGui.QFrame.Sunken)
        self.xval.setText(_fromUtf8(""))
        self.xval.setObjectName(_fromUtf8("xval"))
        self.gridLayout.addWidget(self.xval, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.counts = QtGui.QLabel(Dialog)
        self.counts.setFrameShape(QtGui.QFrame.StyledPanel)
        self.counts.setFrameShadow(QtGui.QFrame.Sunken)
        self.counts.setText(_fromUtf8(""))
        self.counts.setObjectName(_fromUtf8("counts"))
        self.gridLayout.addWidget(self.counts, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.background = QtGui.QLabel(Dialog)
        self.background.setFrameShape(QtGui.QFrame.StyledPanel)
        self.background.setFrameShadow(QtGui.QFrame.Sunken)
        self.background.setText(_fromUtf8(""))
        self.background.setObjectName(_fromUtf8("background"))
        self.gridLayout.addWidget(self.background, 3, 1, 1, 1)
        self.yval = QtGui.QLabel(Dialog)
        self.yval.setFrameShape(QtGui.QFrame.StyledPanel)
        self.yval.setFrameShadow(QtGui.QFrame.Sunken)
        self.yval.setText(_fromUtf8(""))
        self.yval.setObjectName(_fromUtf8("yval"))
        self.gridLayout.addWidget(self.yval, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.qtframe = QtGui.QFrame(Dialog)
        self.qtframe.setMinimumSize(QtCore.QSize(200, 200))
        self.qtframe.setMaximumSize(QtCore.QSize(200, 200))
        self.qtframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qtframe.setFrameShadow(QtGui.QFrame.Raised)
        self.qtframe.setObjectName(_fromUtf8("qtframe"))
        self.vis = MPL_Widget1(self.qtframe)
        self.vis.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.vis.setMinimumSize(QtCore.QSize(200, 200))
        self.vis.setMaximumSize(QtCore.QSize(200, 200))
        self.vis.setObjectName(_fromUtf8("vis"))
        self.horizontalLayout.addWidget(self.qtframe)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radprof = MPL_Widget(self.tab_3)
        self.radprof.setMinimumSize(QtCore.QSize(300, 0))
        self.radprof.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.radprof.setObjectName(_fromUtf8("radprof"))
        self.verticalLayout_2.addWidget(self.radprof)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horcut = MPL_Widget(self.tab_4)
        self.horcut.setMinimumSize(QtCore.QSize(300, 0))
        self.horcut.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.horcut.setObjectName(_fromUtf8("horcut"))
        self.verticalLayout_3.addWidget(self.horcut)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.vertcut = MPL_Widget(self.tab_5)
        self.vertcut.setMinimumSize(QtCore.QSize(300, 0))
        self.vertcut.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.vertcut.setObjectName(_fromUtf8("vertcut"))
        self.verticalLayout_4.addWidget(self.vertcut)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.okbutton = QtGui.QPushButton(Dialog)
        self.okbutton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.okbutton.setObjectName(_fromUtf8("okbutton"))
        self.verticalLayout.addWidget(self.okbutton)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Details", None))
        self.label.setText(_translate("Dialog", "X Center", None))
        self.label_3.setText(_translate("Dialog", "Y Center", None))
        self.label_5.setText(_translate("Dialog", "Counts", None))
        self.label_7.setText(_translate("Dialog", "Background", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Radial Profile", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Horizontal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Vertical", None))
        self.okbutton.setText(_translate("Dialog", "ok", None))

from mpl_pyqt4_widget_new import MPL_Widget1
from mpl_pyqt4_widget import MPL_Widget
