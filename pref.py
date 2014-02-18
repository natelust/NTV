# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pref.ui'
#
# Created: Wed Jan 22 14:54:53 2014
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

class Ui_prefs(object):
    def setupUi(self, prefs):
        prefs.setObjectName(_fromUtf8("prefs"))
        prefs.resize(400, 215)
        self.verticalLayout_2 = QtGui.QVBoxLayout(prefs)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(prefs)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(prefs)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(prefs)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(prefs)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.preview20 = QtGui.QRadioButton(prefs)
        self.preview20.setObjectName(_fromUtf8("preview20"))
        self.buttonGroup = QtGui.QButtonGroup(prefs)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.preview20)
        self.gridLayout.addWidget(self.preview20, 0, 0, 1, 2)
        self.preview5 = QtGui.QRadioButton(prefs)
        self.preview5.setObjectName(_fromUtf8("preview5"))
        self.buttonGroup.addButton(self.preview5)
        self.gridLayout.addWidget(self.preview5, 0, 4, 1, 1)
        self.cutsizeset = QtGui.QLineEdit(prefs)
        self.cutsizeset.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cutsizeset.setObjectName(_fromUtf8("cutsizeset"))
        self.gridLayout.addWidget(self.cutsizeset, 1, 0, 1, 2)
        self.plotup = QtGui.QRadioButton(prefs)
        self.plotup.setObjectName(_fromUtf8("plotup"))
        self.buttonGroup_2 = QtGui.QButtonGroup(prefs)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.plotup)
        self.gridLayout.addWidget(self.plotup, 2, 0, 1, 2)
        self.plotdown = QtGui.QRadioButton(prefs)
        self.plotdown.setObjectName(_fromUtf8("plotdown"))
        self.buttonGroup_2.addButton(self.plotdown)
        self.gridLayout.addWidget(self.plotdown, 2, 3, 1, 2)
        self.overplot = QtGui.QRadioButton(prefs)
        self.overplot.setObjectName(_fromUtf8("overplot"))
        self.buttonGroup_3 = QtGui.QButtonGroup(prefs)
        self.buttonGroup_3.setObjectName(_fromUtf8("buttonGroup_3"))
        self.buttonGroup_3.addButton(self.overplot)
        self.gridLayout.addWidget(self.overplot, 3, 0, 1, 3)
        self.multi = QtGui.QRadioButton(prefs)
        self.multi.setObjectName(_fromUtf8("multi"))
        self.buttonGroup_3.addButton(self.multi)
        self.gridLayout.addWidget(self.multi, 3, 3, 1, 2)
        self.preview10 = QtGui.QRadioButton(prefs)
        self.preview10.setObjectName(_fromUtf8("preview10"))
        self.buttonGroup.addButton(self.preview10)
        self.gridLayout.addWidget(self.preview10, 0, 2, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.ok_sync = QtGui.QPushButton(prefs)
        self.ok_sync.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ok_sync.setObjectName(_fromUtf8("ok_sync"))
        self.verticalLayout_2.addWidget(self.ok_sync)

        self.retranslateUi(prefs)
        QtCore.QMetaObject.connectSlotsByName(prefs)

    def retranslateUi(self, prefs):
        prefs.setWindowTitle(_translate("prefs", "Preference", None))
        self.label.setText(_translate("prefs", "Preview Size", None))
        self.label_2.setText(_translate("prefs", "Default cut size", None))
        self.label_3.setText(_translate("prefs", "Plot Origin", None))
        self.label_4.setText(_translate("prefs", "Dialog Box Behaivor", None))
        self.preview20.setText(_translate("prefs", "20", None))
        self.preview5.setText(_translate("prefs", "5", None))
        self.cutsizeset.setText(_translate("prefs", "3", None))
        self.plotup.setText(_translate("prefs", "Upper", None))
        self.plotdown.setText(_translate("prefs", "Lower", None))
        self.overplot.setText(_translate("prefs", "Overplot", None))
        self.multi.setText(_translate("prefs", "Multi Windows", None))
        self.preview10.setText(_translate("prefs", "10", None))
        self.ok_sync.setText(_translate("prefs", "Ok", None))

