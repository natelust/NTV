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
        QObject.connect(self,SIGNAL('got_it'),parent.rec_data)
        CommandRegistry.commands.append(commandObject('NTV','show_array','Arguments: array'))
        CommandRegistry.commands.append(commandObject('NTV','get_xy','Arguments: None'))

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
                        ret = getattr(self, obj.function)(*args, **kwargs)
                        self.sock.send_pyobj(ret)
                    else:
                        makeNew = True
                        for key in self.parent.plugins_dock_dict.keys():
                            if self.parent.plugins_dock_dict[key].widget().__class__.__name__ == obj.name:
                                makeNew = False
                                break        
                        if makeNew:
                            self.parent.pluginQactions[obj.name].trigger()
                            # Now find the name of the key, as it may be a ctime
                            # Sleep to give the plugin time to be created on the other thread
                            time.sleep(0.5)
                            for key in self.parent.plugins_dock_dict.keys():
                                if self.parent.plugins_dock_dict[key].widget().__class__.__name__ == obj.name:
                                    break
                        self.emit(SIGNAL('RUNCOMMAND'), getattr(self.parent.plugins_dock_dict[key].widget(),\
                                      obj.function), args, kwargs)
                        # The thread is terminated here, and will be restarted due to some issues with
                        # Drawing cross threads, and returning asyncronously across threads
                        break
                except:
                    ret = None
                    self.sock.send_pyobj(ret)
            time.sleep(1)

    def show_array(self,array):
        self.emit(SIGNAL('got_it'), array)

    def get_xy(self):
        self.parent.connectclick(self.send_xy)
        while True:
            if self.coords != None:
                coords = self.coords[:]
                self.coords = None
                return(coords)
            time.sleep(0.2)

    def send_xy(self,event):
        self.coords = (event.xdata,event.ydata)
