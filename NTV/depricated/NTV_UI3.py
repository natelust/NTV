# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NTV.ui'
#
# Created: Thu Jan 16 14:47:07 2014
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

class Ui_NTV(object):
    def setupUi(self, NTV):
        NTV.setObjectName(_fromUtf8("NTV"))
        NTV.resize(1208, 705)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 231, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 231, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 231, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 231, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        NTV.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/sole.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NTV.setWindowIcon(icon)
        NTV.setAnimated(True)
        NTV.setDocumentMode(False)
        self.centy = QtGui.QWidget(NTV)
        self.centy.setAcceptDrops(True)
        self.centy.setObjectName(_fromUtf8("centy"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centy)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 100, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filelab = QtGui.QLabel(self.centy)
        self.filelab.setMinimumSize(QtCore.QSize(400, 0))
        self.filelab.setMaximumSize(QtCore.QSize(400, 16777215))
        self.filelab.setObjectName(_fromUtf8("filelab"))
        self.horizontalLayout.addWidget(self.filelab)
        self.pushButton = QtGui.QPushButton(self.centy)
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtGui.QLabel(self.centy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.sizeofcut = QtGui.QLineEdit(self.centy)
        self.sizeofcut.setMinimumSize(QtCore.QSize(75, 0))
        self.sizeofcut.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sizeofcut.setObjectName(_fromUtf8("sizeofcut"))
        self.horizontalLayout.addWidget(self.sizeofcut)
        self.ycheckbox = QtGui.QCheckBox(self.centy)
        self.ycheckbox.setObjectName(_fromUtf8("ycheckbox"))
        self.horizontalLayout.addWidget(self.ycheckbox)
        self.xcheckbox = QtGui.QCheckBox(self.centy)
        self.xcheckbox.setObjectName(_fromUtf8("xcheckbox"))
        self.horizontalLayout.addWidget(self.xcheckbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame = QtGui.QFrame(self.centy)
        self.frame.setMaximumSize(QtCore.QSize(214, 524))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.minipix = QtGui.QLabel(self.frame)
        self.minipix.setMinimumSize(QtCore.QSize(200, 200))
        self.minipix.setMaximumSize(QtCore.QSize(200, 200))
        self.minipix.setFrameShape(QtGui.QFrame.StyledPanel)
        self.minipix.setFrameShadow(QtGui.QFrame.Raised)
        self.minipix.setText(_fromUtf8(""))
        self.minipix.setObjectName(_fromUtf8("minipix"))
        self.verticalLayout.addWidget(self.minipix)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.minlab = QtGui.QLabel(self.frame)
        self.minlab.setMaximumSize(QtCore.QSize(140, 40))
        self.minlab.setFrameShape(QtGui.QFrame.StyledPanel)
        self.minlab.setFrameShadow(QtGui.QFrame.Sunken)
        self.minlab.setText(_fromUtf8(""))
        self.minlab.setObjectName(_fromUtf8("minlab"))
        self.gridLayout.addWidget(self.minlab, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.maxlab = QtGui.QLabel(self.frame)
        self.maxlab.setMaximumSize(QtCore.QSize(140, 40))
        self.maxlab.setFrameShape(QtGui.QFrame.StyledPanel)
        self.maxlab.setFrameShadow(QtGui.QFrame.Sunken)
        self.maxlab.setText(_fromUtf8(""))
        self.maxlab.setObjectName(_fromUtf8("maxlab"))
        self.gridLayout.addWidget(self.maxlab, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.xdim = QtGui.QLabel(self.frame)
        self.xdim.setMaximumSize(QtCore.QSize(140, 40))
        self.xdim.setFrameShape(QtGui.QFrame.StyledPanel)
        self.xdim.setFrameShadow(QtGui.QFrame.Sunken)
        self.xdim.setText(_fromUtf8(""))
        self.xdim.setObjectName(_fromUtf8("xdim"))
        self.gridLayout.addWidget(self.xdim, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.ydim = QtGui.QLabel(self.frame)
        self.ydim.setMaximumSize(QtCore.QSize(140, 40))
        self.ydim.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ydim.setFrameShadow(QtGui.QFrame.Sunken)
        self.ydim.setText(_fromUtf8(""))
        self.ydim.setObjectName(_fromUtf8("ydim"))
        self.gridLayout.addWidget(self.ydim, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.pixval = QtGui.QLabel(self.frame)
        self.pixval.setMaximumSize(QtCore.QSize(140, 40))
        self.pixval.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pixval.setFrameShadow(QtGui.QFrame.Sunken)
        self.pixval.setText(_fromUtf8(""))
        self.pixval.setObjectName(_fromUtf8("pixval"))
        self.gridLayout.addWidget(self.pixval, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lincheck = QtGui.QRadioButton(self.frame)
        self.lincheck.setObjectName(_fromUtf8("lincheck"))
        self.horizontalLayout_3.addWidget(self.lincheck)
        self.logcheck = QtGui.QRadioButton(self.frame)
        self.logcheck.setObjectName(_fromUtf8("logcheck"))
        self.horizontalLayout_3.addWidget(self.logcheck)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cmapbox = QtGui.QComboBox(self.frame)
        self.cmapbox.setObjectName(_fromUtf8("cmapbox"))
        self.verticalLayout.addWidget(self.cmapbox)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centy)
        self.label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.clipslide = QtGui.QSlider(self.centy)
        self.clipslide.setOrientation(QtCore.Qt.Vertical)
        self.clipslide.setObjectName(_fromUtf8("clipslide"))
        self.verticalLayout_2.addWidget(self.clipslide)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ygview = QtGui.QGraphicsView(self.centy)
        self.ygview.setEnabled(True)
        self.ygview.setMinimumSize(QtCore.QSize(100, 450))
        self.ygview.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ygview.setObjectName(_fromUtf8("ygview"))
        self.gridLayout_2.addWidget(self.ygview, 0, 0, 1, 1)
        self.imshow = MPL_Widget(self.centy)
        self.imshow.setMinimumSize(QtCore.QSize(450, 450))
        self.imshow.setObjectName(_fromUtf8("imshow"))
        self.gridLayout_2.addWidget(self.imshow, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(0, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.xgview = QtGui.QGraphicsView(self.centy)
        self.xgview.setMinimumSize(QtCore.QSize(0, 100))
        self.xgview.setMaximumSize(QtCore.QSize(16777215, 150))
        self.xgview.setObjectName(_fromUtf8("xgview"))
        self.gridLayout_2.addWidget(self.xgview, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        NTV.setCentralWidget(self.centy)
        self.menubar = QtGui.QMenuBar(NTV)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuImage = QtGui.QMenu(self.menubar)
        self.menuImage.setObjectName(_fromUtf8("menuImage"))
        NTV.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(NTV)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        NTV.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(NTV)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(NTV)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHeader = QtGui.QAction(NTV)
        self.actionHeader.setObjectName(_fromUtf8("actionHeader"))
        self.actionAbout = QtGui.QAction(NTV)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHeader_2 = QtGui.QAction(NTV)
        self.actionHeader_2.setObjectName(_fromUtf8("actionHeader_2"))
        self.actionPreferences = QtGui.QAction(NTV)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionBlink = QtGui.QAction(NTV)
        self.actionBlink.setObjectName(_fromUtf8("actionBlink"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuImage.addAction(self.actionHeader_2)
        self.menuImage.addAction(self.actionBlink)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(NTV)
        QtCore.QMetaObject.connectSlotsByName(NTV)

    def retranslateUi(self, NTV):
        NTV.setWindowTitle(_translate("NTV", "NTV", None))
        self.filelab.setText(_translate("NTV", "TextLabel", None))
        self.pushButton.setText(_translate("NTV", "Pick Star", None))
        self.label_3.setText(_translate("NTV", "Aperture Radius", None))
        self.ycheckbox.setText(_translate("NTV", "Show Y view", None))
        self.xcheckbox.setText(_translate("NTV", "Show X view", None))
        self.label_2.setText(_translate("NTV", "Min Value", None))
        self.label_4.setText(_translate("NTV", "Max Value", None))
        self.label_6.setText(_translate("NTV", "X Dim", None))
        self.label_8.setText(_translate("NTV", "Y Dim", None))
        self.label_5.setText(_translate("NTV", "Pixel Value", None))
        self.lincheck.setText(_translate("NTV", "Linear", None))
        self.logcheck.setText(_translate("NTV", "Log", None))
        self.label.setText(_translate("NTV", "Clip Point", None))
        self.menuFile.setTitle(_translate("NTV", "File", None))
        self.menuHelp.setTitle(_translate("NTV", "Help", None))
        self.menuImage.setTitle(_translate("NTV", "Image", None))
        self.actionOpen.setText(_translate("NTV", "Open", None))
        self.actionOpen.setShortcut(_translate("NTV", "Ctrl+O", None))
        self.actionQuit.setText(_translate("NTV", "Quit", None))
        self.actionHeader.setText(_translate("NTV", "Header", None))
        self.actionHeader.setShortcut(_translate("NTV", "Ctrl+H", None))
        self.actionAbout.setText(_translate("NTV", "About", None))
        self.actionHeader_2.setText(_translate("NTV", "Header", None))
        self.actionHeader_2.setShortcut(_translate("NTV", "Ctrl+H", None))
        self.actionPreferences.setText(_translate("NTV", "Preferences", None))
        self.actionBlink.setText(_translate("NTV", "Blink", None))

from mpl_pyqt4_widget import MPL_Widget
import icons_rc
