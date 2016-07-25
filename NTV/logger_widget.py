import logging
from PyQt4 import QtGui


class NTVLogger(logging.Handler):
    def __init__(self, parent=None):
        logging.Handler.__init__(self)
        self.widget = QtGui.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, entry):
        msg = self.format(entry)
        self.widget.appendPlainText(msg)
