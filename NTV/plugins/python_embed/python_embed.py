#! /usr/bin/env python
import numpy as np

class embed():
    '''
    This is a class that adds the ability for ntv to be used from with in a python interpriter.
    In order to use this you must be using python > 2.6 or have the multiprocessing package
    installed.
    To embed this do something like the following example
    #> python
    >>> from NTV.embed import embed
    >>> import numpy
    >>> x = numpy.arange(441)
    >>> x = x.reshape(21,21)
    >>> my_instance = embed()
    >>> my_instance.showArray(x)
    '''
    import zmq
    import numpy
    import numpy as np
    import socket
    import subprocess
    import json
    try:
        import simplejson as json
    except:
        pass
    try:
        import ujson as json
    except:
        pass

    def __init__(self,port=False):
        import zmq
        import numpy
        import socket
        import subprocess
        import json
        try:
            import simplejson as json
        except:
            pass
        try:
            import ujson as json
        except:
            pass
        self.json = json
        try:
            self.port = int(port)
        except:
            self.port = False
        self.zmq = zmq
        self.context = zmq.Context()
        if self.port == False:
            while True:
                self.port = numpy.random.randint(50000,65535)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.bind(('127.0.0.1',self.port))
                    s.close()
                    break
                except:
                    pass

            subprocess.Popen(['./ntviewer','-p '+str(self.port)])
        context = zmq.Context()
        self.sock = context.socket(zmq.REQ)
        self.sock.connect('tcp://127.0.0.1:'+str(self.port))

    def sendData(self,name,data):
        if type(data) == type(np.zeros(0)):
            data = data.tolist()
        #if type(data) != type(''):
        #    data = str(data)
        if type(name) != type(''):
            name = str(name)
        dump = self.json.dumps((name,data))
        self.sock.send_string(dump)
        ret = self.sock.recv_string()
        return ret

    def getData(self,name):
        if type(name) != type(''):
            name = str(name)
        dump = self.json.dumps((name,))
        self.sock.send_string(dump)
        tup = self.sock.recv_string()
        res = self.json.loads(tup)
        return res

    def showArray(self,array):
        self.sendData('show_array',array)

    def get_yx(self):
        res = list(self.getData('get_xy'))
        return res[1],res[0]
