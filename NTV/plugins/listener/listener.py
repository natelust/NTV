import numpy as np
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import time
from NTV.utils import commandObject, CommandRegistry

class listener(QThread):
    '''
    This class is for internal use only. It inherets the QThread class, and is
    used to separate the listening of a zmq connection in interactive mode into
    its own thread, as to not tie up the main event loop
    '''
    import numpy as np
    def __init__(self,parent,port,sock,lock):
        #zmq server must be in push mode for socket
        import zmq
        self.zmq = zmq
        QThread.__init__(self)
        self.conn                  = port
        self.sock                  = sock
        self.poller                = zmq.Poller()
        self.poller.register(self.sock,zmq.POLLIN)
        self.parent                = parent
        self.lock                  = lock
        self.coords                = None

    def run(self):
        while True:
            socks = dict(self.poller.poll())
            if self.sock in socks and socks[self.sock] == self.zmq.POLLIN:
                obj,args,kwargs = self.sock.recv_pyobj()
                try:
                    if obj.name == 'listener':
                        ret = CommandRegistry.commands
                        self.sock.send_pyobj(ret)
                    elif obj.name == 'NTV':
                        self.emit(SIGNAL('RUNCOMMAND'), obj.pipe, getattr(self.parent, obj.function), args, kwargs)
                        break
                        #self.sock.send_pyobj(ret)
                    else:
                        plug = self.findOrOpenPlugin(obj.name)
                        self.emit(SIGNAL('RUNCOMMAND'), obj.pipe, getattr(self.findOrOpenPlugin(obj.name),
                            obj.function), args, kwargs)
                        # The thread is terminated here, and will be restarted due to some issues with
                        # Drawing cross threads, and returning asyncronously across threads
                        break
                except:
                    ret = None
                    self.sock.send_pyobj(ret)
            time.sleep(1)

    def scanPlugins(self, name):
        ident = None
        for key in self.parent.plugins_dock_dict.keys():
            if self.parent.plugins_dock_dict[key].widget().__class__.__name__ == name:
                ident = key
                break
        return ident

    def findOrOpenPlugin(self, name):
        ident = self.scanPlugins(name)
        if ident is None:
            self.parent.pluginQactions[name].trigger()
            # Sleep to give plugin time to be created on other thread
            time.sleep(0.5)
            # Find key associated with plugin name
            ident = self.scanPlugins(name)
        return self.parent.plugins_dock_dict[ident].widget()
