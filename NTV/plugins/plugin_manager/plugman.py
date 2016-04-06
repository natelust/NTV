# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugman.ui'
#
# Created: Mon Feb 17 14:33:39 2014
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

class Ui_PluginManager(object):
    def setupUi(self, PluginManager):
        PluginManager.setObjectName(_fromUtf8("PluginManager"))
        PluginManager.setWindowModality(QtCore.Qt.ApplicationModal)
        PluginManager.resize(646, 584)
        self.verticalLayout_4 = QtGui.QVBoxLayout(PluginManager)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(PluginManager)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 562, 455))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.local_group = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        self.local_group.setObjectName(_fromUtf8("local_group"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.local_group)
        self.verticalLayout_13.setMargin(0)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.local_group_lay = QtGui.QVBoxLayout()
        self.local_group_lay.setObjectName(_fromUtf8("local_group_lay"))
        self.verticalLayout_13.addLayout(self.local_group_lay)
        self.verticalLayout_9.addWidget(self.local_group)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 560, 386))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.remote_group = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.remote_group.setObjectName(_fromUtf8("remote_group"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.remote_group)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.remote_group_lay = QtGui.QVBoxLayout()
        self.remote_group_lay.setObjectName(_fromUtf8("remote_group_lay"))
        self.verticalLayout_11.addLayout(self.remote_group_lay)
        self.verticalLayout_8.addWidget(self.remote_group)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.install_location = QtGui.QLineEdit(self.tab_2)
        self.install_location.setObjectName(_fromUtf8("install_location"))
        self.horizontalLayout.addWidget(self.install_location)
        self.install_button = QtGui.QPushButton(self.tab_2)
        self.install_button.setObjectName(_fromUtf8("install_button"))
        self.horizontalLayout.addWidget(self.install_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.accept = QtGui.QPushButton(PluginManager)
        self.accept.setMaximumSize(QtCore.QSize(100, 16777215))
        self.accept.setObjectName(_fromUtf8("accept"))
        self.verticalLayout.addWidget(self.accept)
        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(PluginManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PluginManager)

    def retranslateUi(self, PluginManager):
        PluginManager.setWindowTitle(_translate("PluginManager", "Plugin Manager", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PluginManager", "Installed", None))
        self.label.setText(_translate("PluginManager", "Install Plugin from URL", None))
        self.install_button.setText(_translate("PluginManager", "Go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PluginManager", "Available", None))
        self.accept.setText(_translate("PluginManager", "OK", None))

