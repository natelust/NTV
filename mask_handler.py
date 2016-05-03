from PyQt4.QtCore import *
from PyQt4.QtGui import *

import numpy as np
import types
import collections

from .colors import yieldMaskColor


class mask_handler(QWidget):
    def __init__(self, main, parent=None):
        QWidget.__init__(self, parent=parent)
        self.main = main
        if self.main.funloaded != 1:
            raise RuntimeError("No image to mask")
        self.maskImage = np.zeros(list(self.main.image.shape)+[4], dtype=np.uint8)
        self.mainMask = self.main.imshow.canvas.ax.imshow(self.maskImage)
        self.numMasks = 0
        self.maskToColor = {}
        self.maskDict = {}
        self.widLayout = QVBoxLayout(self)
        self.setLayout(self.widLayout)
        self.yielder = yieldMaskColor()
        self.setMinimumWidth(300)
        title = QLabel("Masks:")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        title.setFont(font)
        self.widLayout.addWidget(title)
        self.widLayout.setAlignment(Qt.AlignTop)
        self.transparency = 89

    def add_mask(self, mask, name=None):
        '''
        This function draws mask planes on the image. The widget may take either a single mask
        or a datacube of masks. If a datacube is provided the name argument should either be
        None, or of the same length as the datacube.

        mask - array, if the dimensions must match the image.
        name - the name to assign to the mask plane, if no name is provided
               name defaults to the order of masks added
        '''
        mask = np.array(mask)
        # Handle if multiple masks were passed in at once
        if len(mask.shape) > 2:
            assert isinstance(name, collections.Sequence) and not isinstance(name, types.StringTypes)
            assert len(mask) == len(name) or name is None
            loop = range(len(mask))
        # Set up the loop for single mask
        else:
            loop = range(1)
            mask = [mask]

        if name is None:
            name = ['array'+str(i+self.numMasks) for i in loop]

        base = 0
        print(name)
        for i in loop:
            color = np.uint8(self.yielder.next())
            self.maskToColor[name[i]] = color
            self.maskDict[name[i]] = mask[i]
            locs = np.where(mask[i])
            self.maskImage[locs[0], locs[1], :3] += color
            self.maskImage[locs[0], locs[1], -1] = self.transparency
            base += 1
            self.addDiscription(name[i], color)

        self.maskImage[np.where(self.maskImage > 255)] = 255
        self.numMasks += base
        self.updateMask()

    def updateMask(self):
        self.mainMask.set_data(self.maskImage)
        self.main.imshow.canvas.draw()

    def getColor(self, name):
        '''
        return the color associated with a masked plane
        '''
        return self.maskToColor[name]

    def showMask(self, check, name):
        color = self.getColor(name)
        locs = np.where(self.maskDict[name])
        if check.isChecked():
            self.maskImage[locs[0], locs[1], :3] += color
            self.maskImage[locs[0], locs[1], -1] = self.transparency
        else:
            self.maskImage[locs[0], locs[1], :3] -= color
            self.maskImage[np.where(np.sum(self.maskImage[:, :, :3], axis=-1) == 0)] = [0]*4
        self.updateMask()

    def addDiscription(self, name, color):
        '''
        Add mask label to widget
        '''
        tmp = QWidget()
        layout = QHBoxLayout()
        qcol = QColor(*color)
        cWid = QLabel()
        cWid.setStyleSheet("QWidget { background-color: %s }" % qcol.name())
        cWid.setMinimumWidth(20)
        nWid = QLabel(name)
        check = QCheckBox()
        check.setChecked(True)
        check.stateChanged.connect(lambda: self.showMask(check, name))
        layout.addWidget(check)
        layout.addWidget(cWid)
        layout.addWidget(nWid)
        layout.setAlignment(Qt.AlignLeft)
        tmp.setLayout(layout)
        self.widLayout.addWidget(tmp)
