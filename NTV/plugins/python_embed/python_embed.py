#! /usr/bin/env python
import numpy as np
import functools
import time
from NTV.utils import commandObject

def interact(obj, self, *args, **kwargs):
    self.sock.send_pyobj([obj, args, kwargs])
    ret = self.sock.recv_pyobj()
    return ret
    

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
    >>> my_instance.show_array(x)
    '''
    import zmq
    import numpy
    import numpy as np
    import socket
    import subprocess
    from NTV.utils import commandObject
    import json

    def __init__(self,port=False):
        import zmq
        import numpy
        import socket
        import subprocess
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

            subprocess.Popen(['ntviewer','-p '+str(self.port)])
        context = zmq.Context()
        self.sock = context.socket(zmq.REQ)
        self.sock.connect('tcp://127.0.0.1:'+str(self.port))
        time.sleep(1)
        self.buildFunctionList()

    def buildFunctionList(self):
        request = commandObject('listener', 'None', 'None')
        self.sock.send_pyobj([request, 'None', 'None'])
        commandFunctions = self.sock.recv_pyobj()
        for cmd in commandFunctions:
            setattr(self,cmd.function, functools.partial(interact, cmd, self))
            setattr(getattr(self,cmd.function),'__doc__',cmd.signature)
