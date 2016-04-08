try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

from collections import namedtuple
import inspect
import importlib

commandObject = namedtuple("commandObject", "name function signature")

# Define a decorator to check image loading status
def ifImage(func):
    def _wrapper(self, *args, **kwargs):
        if self.funloaded == 1:
            ret = func(self, *args, **kwargs)
        else:
            ret = None
        return ret
    return _wrapper

#this class is used in the plugin system to create a dock item which can be tracked
#in closing
class myDockWidget(QDockWidget):
    def __init__(self,name,ident,persist,parent=None):
        QDockWidget.__init__(self,name,parent=parent)
        self.ident = ident
        self.persist = persist
    def closeEvent(self,event):
        if self.persist:
            event.ignore()
            self.hide()
        else:
            self.emit(SIGNAL('closing'),self.ident)
            event.accept()

class CommandRegistry():
    commands = []

def hasCommands(*methods):
    commandObject = importlib.import_module("NTV.utils").commandObject
    CommandRegistry = importlib.import_module("NTV.utils").CommandRegistry
    def classFactory(cls):
        for meth in methods:
            CommandRegistry.commands.append(commandObject(cls.__name__,
                            meth,
                            inspect.getargspec(getattr(cls,meth)).__repr__()))
        return cls
    return classFactory
