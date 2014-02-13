from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import plugin_manager as me
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urlr
import json


from .plugman import Ui_PluginManager
from .list_item import Ui_listitem

#this is to get the directory of the containing module to get resources as other
#programs will be actually running this module

loc = me.__file__.rstrip('__init__.py')

class myThread(QThread):
    def __init__(self,url,parent):
        QThread.__init__(self,parent=parent)
        self.parent = parent
        self.url = url
    def run(self):
        try:
            web = urlr.urlopen(url)
            by = BytesIO(self.url.read())
            zp = ZipFile(by)
            self.parent.zp = zp
            for item in zp.namelist():
                if 'manifest' in item:
                    man = item
            rd = zp.open(man).read()
            ld = json.loads(rd.decode())
            version = ld['version']
            self.parent.latestversion.clear()
            self.parent.setText(str(version))
            self.parent.updatebutton.enabled(True)
        except:
            self.parent.latestversion.clear()
            self.parent.latestversion.setFrameStyle(QFrame.StyledPanel|QFrame.Raised)
            self.parent.latestversion.setText('Unavailable')


class plugin_item(QWidget,Ui_listitem):
    def __init__(self,plugin,main):
        QWidget.__init__(self)
        self.setupUi(self)
        self.plugin = plugin
        self.main = main
        self.name.setText(plugin['manifest']['name'])
        self.description.setText(plugin['manifest']['description'])
        self.installedversion.setText(str(plugin['manifest']['version']))
        move = QMovie(os.path.join(loc,'working2.gif'),QByteArray(),self)
        #move.setScaledSize(QSize(72,47))
        self.latestversion.setMovie(move)
        move.start()
        thread = myThread(plugin['manifest']['url'],parent=self)
        thread.start()
        self.connect(self.updatebutton,SIGNAL('clicked()'),self.install)
    def install(self):
        self.zp.extractall(path=self.main.main.user_loc)
        os.rename(os.path.join(self.main.main.user_loc,self.zp.namelist()[0].rstrip('/')),\
                  os.path.join(self.main.main.user_loc,self.plugin['manifest']['module']))



class plugin_manager(QDialog,Ui_PluginManager):
    def __init__(self,main):
        QDialog.__init__(self)
        self.setupUi(self)
        self.main = main
        self.setPalette(main.palette())
        for plug in main.plugins_global_dict:
            tmp = plugin_item(main.plugins_global_dict[plug],self)
            self.local_group_lay.addWidget(tmp)
        QObject.connect(self.accept,SIGNAL('clicked()'),self.close)
        self.exec_()
