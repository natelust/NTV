from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import plugin_manager as me
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urlr
import json
import shutil


from .plugman import Ui_PluginManager
from .list_item import Ui_listitem
from .remote_item import Ui_remote_item

#this is to get the directory of the containing module to get resources as other
#programs will be actually running this module

loc = me.__file__.rstrip('__init__.py')

def read_version(zp):
    for item in zp.namelist():
        if 'manifest' in item:
            man = item
    rd = zp.open(man).read()
    ld = json.loads(rd.decode())
    version = ld['version']
    return version

def install_plugin(url,user_loc):
    web = urlr.urlopen(url)
    by = BytesIO(web.read())
    web.close()
    zp = ZipFile(by)
    for item in zp.namelist():
        if 'manifest' in item:
            man = item
    rd = zp.open(man).read()
    ld = json.loads(rd.decode())
    zp.extractall(path=user_loc)
    os.rename(os.path.join(user_loc,\
                  zp.namelist()[0].rstrip('/')),\
                  os.path.join(user_loc,\
                  ld['module']))


class myThread(QThread):
    def __init__(self,url,parent):
        QThread.__init__(self,parent=parent)
        self.parent = parent
        self.url = url
    def run(self):
        try:
            web = urlr.urlopen(self.url)
            by = BytesIO(web.read())
            web.close()
            zp = ZipFile(by)
            self.parent.main.zip_dict[self.parent.plugin['manifest']['module']] = zp
            version = read_version(zp)
            self.parent.latestversion.clear()
            self.parent.latestversion.setText(str(version))
            self.parent.updatebutton.setEnabled(True)

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
        self.latestversion.setMovie(move)
        move.start()
        if plugin['manifest']['module'] not in self.main.zip_dict:
            thread = myThread(plugin['manifest']['url'],parent=self)
            thread.start()
        else:
            version = read_version(self.main.zip_dict[plugin['manifest']['module']])
            self.latestversion.clear()
            self.latestversion.setText(str(version))
            self.updatebutton.setEnabled(True)
        if plugin['dir'] == self.main.main.user_loc:
            self.uninstallbutton.setEnabled(True)
        self.connect(self.updatebutton,SIGNAL('clicked()'),self.install)
        self.connect(self.uninstallbutton,SIGNAL('clicked()'),self.uninstall)

    def install(self):
        zp = self.main.zip_dict[self.plugin['manifest']['module']]
        zp.extractall(path=self.main.main.user_loc)
        try:
            shutil.rmtree(os.path.join(\
                          self.main.main.user_loc,\
                          self.plugin['manifest']['module']))
        except:
            pass
        os.rename(os.path.join(self.main.main.user_loc,\
                  zp.namelist()[0].rstrip('/')),\
                  os.path.join(self.main.main.user_loc,\
                  self.plugin['manifest']['module']))
        self.updatebutton.setEnabled(False)
        self.updatebutton.setText('Installed')
        self.uninstallbutton.setEnabled(True)
        self.main.update_count += 1
    def uninstall(self):
        try:
            shutil.rmtree(os.path.join(\
                          self.main.main.user_loc,\
                          self.plugin['manifest']['module']))
            msg = '''Note the plugin has been removed from the user directory but may still be present as a module shipped with NTV'''
            QMessageBox.information(self,'Success',msg)
            self.updatebutton.setEnabled(True)
            self.updatebutton.setText('Update')
            self.uninstallbutton.setEnabled(False)
            self.main.reload_plugins()
        except:
            msg = '''There was an error uninstalling the plugin please remove from the file system manually'''
            QMessageBox.warning(self,'Error',msg)

class remote_item(QWidget,Ui_remote_item):
    def __init__(self,plugin,main):
        QWidget.__init__(self)
        self.setupUi(self)
        self.plugin = plugin
        self.main = main
        self.name.setText(plugin['name'])
        self.description.setText(plugin['description'])
        self.connect(self.installbutton,SIGNAL('clicked()'),self.install)

    def install(self):
        install_plugin(self.plugin['url'],self.main.main.user_loc)
        self.installbutton.setText('Installed')
        self.installbutton.setEnabled(False)
        self.main.reload_plugins()

class plugin_manager(QDialog,Ui_PluginManager):
    def __init__(self,main):
        QDialog.__init__(self)
        self.setupUi(self)
        self.main = main
        self.setPalette(main.palette())
        self.zip_dict = {}
        self.process_plugins()

        QObject.connect(self.accept,SIGNAL('clicked()'),self.close)
        QObject.connect(self.install_button,SIGNAL('clicked()'),self.install)
        self.exec_()

    def reload_plugins(self):
        self.main.reload_plugins()
        for i in reversed(range(self.local_group_lay.count())):
            self.local_group_lay.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.remote_group_lay.count())):
            self.remote_group_lay.itemAt(i).widget().setParent(None)
        self.process_plugins()

    def process_plugins(self):
        self.update_count = 0
        installed_names = []
        for plug in self.main.plugins_global_dict:
            tmp = plugin_item(self.main.plugins_global_dict[plug],self)
            self.local_group_lay.addWidget(tmp)
            installed_names.append(self.main.\
                            plugins_global_dict[plug]['manifest']['name'])
        temp_file = open(os.path.join(loc,'plugin_list.txt'),'r')
        full_list = temp_file.read()
        temp_file.close()
        self.full_list_split = full_list.split('|')
        for entry in self.full_list_split:
            jentry = json.loads(entry)
            if jentry['name'] not in installed_names:
                self.remote_group_lay.addWidget(remote_item(jentry,self))

    def install(self):
        url = str(self.install_location.text())
        if self.check_url(url):
            try:
                install_plugin(url,self.main.user_loc)
                title = 'Success'
                msg   = 'The plugin has been successfully installed'
                self.install_location.clear()
                self.reload_plugins()
            except:
                title = 'Error'
                msg   = 'The plugin did not install correctly please check the url'
            QMessageBox.warning(self,title,msg)
        else:
            msg = 'Could not find plugin, please check for a valid url'
            QMessageBox.warning(self,'Error',msg)
            self.install_location.clear()

    def check_url(self,url):
        if url == '':
            return False
        try:
            web = urlr.urlopen(url)
        except:
            return False
        resp = web.status
        web.close()
        return resp == 200

    def closeEvent(self,event):
        if self.update_count >0:
            msg = '''Any core modules that have been updated will require a restart for new functionality'''
            QMessageBox.warning(self,'Alert',msg)
        self.main.reload_plugins()
        event.accept()
