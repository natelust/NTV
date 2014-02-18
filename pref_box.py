from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .pref import Ui_prefs

class pref_box(QDialog,Ui_prefs):
    def __init__(self,pref,parent):
        QDialog.__init__(self)
        self.setupUi(self)
        #this next part is a hack since button groups are not properly handeled by pyuic4
        self.bgroup1 = QButtonGroup()
        self.bgroup1.addButton(self.preview20)
        self.bgroup1.addButton(self.preview10)
        self.bgroup1.addButton(self.preview5)
        self.bgroup2 = QButtonGroup()
        self.bgroup2.addButton(self.plotup)
        self.bgroup2.addButton(self.plotdown)
        self.bgroup3 = QButtonGroup()
        self.bgroup3.addButton(self.overplot)
        self.bgroup3.addButton(self.multi)
        #end hack
        self.pref = pref
        self.parent = parent
        self.preview_size = self.pref.value('previewsize')
        if self.preview_size == 20:
            self.preview20.setChecked(1)
        if self.preview_size == 10:
            self.preview10.setChecked(1)
        if self.preview_size == 5:
            self.preview5.setChecked(1)
        self.cut_size = str(self.pref.value('cutsize'))
        self.cutsizeset.setText(self.cut_size)
        self.origin_set = self.pref.value('origin')
        if self.origin_set == 'upper':
            self.plotup.setChecked(1)
        if self.origin_set == 'lower':
            self.plotdown.setChecked(1)
        self.dbox = self.pref.value('dbox')
        if self.dbox == 1:
            self.overplot.setChecked(1)
        if self.dbox == 0:
            self.multi.setChecked(1)
        QObject.connect(self.ok_sync,SIGNAL('clicked()'),self.accept)
        QObject.connect(self,SIGNAL('reload'),parent.read_config)
        QObject.connect(self,SIGNAL('redraw'),parent.drawim)
        self.exec_()
    def accept(self):
        if self.preview20.isChecked():
            self.pref.setValue('previewsize',20)
        if self.preview10.isChecked():
            self.pref.setValue('previewsize',10)
        if self.preview5.isChecked():
            self.pref.setValue('previewsize',5)
        self.pref.setValue('cutsize',int(self.cutsizeset.text()))
        if self.plotup.isChecked():
            self.pref.setValue('origin','upper')
        if self.plotdown.isChecked():
            self.pref.setValue('origin','lower')
        if self.overplot.isChecked():
            self.pref.setValue('dbox',1)
        if self.multi.isChecked():
            self.pref.setValue('dbox',0)
        self.pref.sync()
        self.parent.homeImage = 1
        self.emit(SIGNAL('reload'))
        self.emit(SIGNAL('redraw'))
        self.close()
