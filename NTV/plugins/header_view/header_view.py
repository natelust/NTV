try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import numpy as np

from .header_ui import Ui_header

class header_view(QDialog,Ui_header):
    def __init__(self,cards,parent=None):
        super(header_view,self).__init__(parent)
        self.setupUi(self)
        font = QFont("Courier",11)
        font.setFixedPitch(1)
        self.cardlist.setFont(font)
        key = []
        keymax = 0
        value = []
        extra = []
        for index in range(len(cards)):
            item = cards[index]
            #item = str(item).split('=')
            one = str(item[0]).strip()
            two = str(item[1]).strip()
            try:
                extra.append(str(item[2]).strip())
            except:
                extra.append('')
            key.append(one)
            value.append(two)
            if len(one) > keymax:
                keymax = len(one)
        for k in range(len(key)):
            string = np.chararray(1,keymax+5-len(key[k]))
            string=(keymax+5-len(key[k]))*' '
            res = key[k]+str(string)+'=  '+value[k]+' / '+extra[k]
            temp = QListWidgetItem(res)
            temp.setTextAlignment(1)
            self.cardlist.addItem(temp)
        QObject.connect(self.okbutton,SIGNAL('clicked()'),self.close)
        self.exec_()

