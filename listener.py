import numpy as np
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import json
import time


class listener(QThread):
    '''
    This class is for internal use only. It inherets the QThread class, and is
    used to separate the listening of a zmq connection in interactive mode into
    its own thread, as to not tie up the main event loop
    '''
    import numpy as np
    def __init__(self,parent,port,sock,lock):
        #q = json.dumps(('array',light_frames[0].tolist())) example dump
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
        self.plugin_functions_dict = {}
        self.plugin_functions_desc = []
        self.plugin_functions_name = []
        self.plugin_functions_name.append('show_array')
        self.plugin_functions_desc.append('Displays an array, arugments should be a single array')
        self.plugin_functions_name.append('get_xy')
        self.plugin_functions_desc.append('Gets the coordinates of a mouse position click, no arguments')
        self.register_plugins()
        QObject.connect(self,SIGNAL('got_it'),parent.rec_data)
        #print(self.parent.plugins_module_dict['example'].example.register_functions())
    def run(self):
        while True:
            socks = dict(self.poller.poll())
            if self.sock in socks and socks[self.sock] == self.zmq.POLLIN:
                self.message  = self.sock.recv_string()
                self.loads    = json.loads(self.message)
                if self.loads[0] == 'show_array':
                    try:
                        self.data = np.array(self.loads[1])
                        self.sock.send_string(json.dumps('recived'))
                    except:
                        self.sock.send_string(json.dumps('Failed'))
                    if type(self.data) == np.ndarray:
                        if len(self.data.shape) == 2 or len(self.data.shape) == 3:
                            self.emit(SIGNAL('got_it'),self.data)
                elif self.loads[0] == 'get_xy':
                    if self.parent.funloaded == 0:
                        ret = json.dumps(('na','na'))
                        self.sock.send_string(ret)
                    else:
                        self.get_xy()
                        time.sleep(0.1)
                        self.lock.acquire()
                        self.lock.release()
                elif self.loads[0] == 'list_functions':
                    ret = json.dumps((self.plugin_functions_name,self.plugin_functions_desc))
                    self.sock.send_string(ret)
                elif self.loads[0] in self.plugin_functions_name:
                    plug = self.plugin_functions_dict[self.loads[0]][0]
                    func = self.plugin_functions_dict[self.loads[0]][1]
                    go = 0
                    for key in self.parent.plugins_dock_dict:
                        if str(self.parent.plugins_dock_dict[key].objectName()) == str(plug):
                            go += 1
                            ident = key
                    if go > 0:
                        try:
                            if len(self.loads) > 1:
                                ret = eval('self.parent.plugins_dict[ident].'+func+'(self.loads[1])')
                            else:
                                ret = eval('self.parent.plugins_dict[ident].'+func+'()')
                        except:
                            ret = 'There was an error running the command'
                    else:
                        ret = 'Please open the plugin associated with this funciton'
                    if ret == None:
                        ret == 'recived'
                    self.sock.send_string(json.dumps(ret))
                else:
                    self.sock.send_string(json.dumps('Error'))
            time.sleep(1)

    def get_xy(self):
        self.lock.acquire()
        self.parent.connectclick(self.send_xy)

    def send_xy(self,event):
        string = json.dumps((event.xdata,event.ydata))
        self.sock.send_string(string)
        self.lock.release()

    def register_plugins(self):
        #print(self.parent.plugins_module_dict["example"].example.issquared)
        for plug in self.parent.plugins_module_dict:
            try:
                work = eval('self.parent.plugins_module_dict[plug].'+plug+'.__dict__')
                for key in work.keys():
                    if key == 'register_functions':
                        names,descriptions,functions = eval('self.parent.plugins_module_dict[plug].'+plug+'.register_functions()')
                        #put in logic to make sure names, descriptions, and functions are all the same length!!
                        for i in range(len(names)):
                            self.plugin_functions_dict[names[i]] = [plug,functions[i]]
                            self.plugin_functions_desc.append(descriptions[i])
                            self.plugin_functions_name.append(names[i])
            except:
                pass
