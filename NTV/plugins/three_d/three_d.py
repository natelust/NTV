try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import numpy as np
import astropy.io.fits as astroIo

from .threeD_ui import Ui_ThreeD

def sort(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   place  = []
   for i,item in enumerate(seq):
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
       place.append(i)
   return result,place


class three_d(QWidget,Ui_ThreeD):
    def __init__(self, main, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.main = main
        self.imageCube = None
        self.headerCube = None
        self.current_frame = 0
        self.current_axis = 0
        self.frame_properties = {}
        self.going = 0
        self.mytimer = QTimer()
        QObject.connect(self.fnumbar,SIGNAL('sliderReleased()'),self.save_scale_and_color)
        QObject.connect(self.play,SIGNAL('clicked()'),self.playback)
        QObject.connect(self.main,SIGNAL('update_3d'),self.setup)
        QObject.connect(self.mytimer,SIGNAL('timeout()'),self.update_slider)
        QObject.connect(self.xbutton,SIGNAL('clicked()'),self.change_axis)
        QObject.connect(self.ybutton,SIGNAL('clicked()'),self.change_axis)
        QObject.connect(self.zbutton,SIGNAL('clicked()'),self.change_axis)
        QObject.connect(self.clearbutton,SIGNAL('clicked()'),self.clearfunc)
        QObject.connect(self.LoadImageButton, SIGNAL('clicked()'), self.loadImage)

    def setup(self):
        if self.mytimer.isActive():
            self.mytimer.stop()
        self.length = self.imageCube.shape[self.current_axis] - 1
        self.fnumber.setText(str(self.current_frame))
        self.fnumbar.setMinimum(0)
        self.fnumbar.setMaximum(self.length)
        self.fnumbar.setValue(self.current_frame)

    def loadImage(self):
        '''
        Create a load dialog box to process incoming images
        '''
        if self.main.funloaded:
            try:
                file = str(QFileDialog.getOpenFileName(self, 'Select additional File','~/'))
            except:
                pass
            if file and file.find('fits') != -1 or file.find('FIT') != -1 or\
                    file.find('fit') != -1:
                image, header = astroIo.getdata(file, header=True)
                self.addImage(image)
                if len(image.shape) == 3:
                    [self.addHeader(header) for x in range(image.shape[0])]
                else:
                    self.addHeader(header)

    def addImage(self, image):
        if self.imageCube != None:
            # Check to make sure the imageCube is in fact a cube
            if len(self.imageCube.shape) < 3:
                self.imageCube = np.expand_dims(self.imageCube, 0)
            if len(image.shape) < 3:
                image = np.expand_dims(image, axis=0)
            try:
                # This statement will work for files of the same size
                self.imageCube = np.append(self.imageCube, image, axis=0)
            except:
                # This catches when the arrays are not the same size
                decomp_one = np.split(self.imageCube, self.imageCube.shape[0], axis=0)
                decomp_two = np.split(image, image.shape[0], axis=0)
                self.imageCube = np.array(decomp_one + decomp_two, dtype='object')
        else:
            # This gets invoked when there is no image in the class
            self.imageCube = np.expand_dims(image,0)
        self.setup()

    def addHeader(self, header):
        if self.headerCube:
            self.headerCube.append(header)
        else:
            self.headerCube = [header]

    def clearfunc(self):
        if str(self.main.three_d_props.current_frame)+\
           str(self.main.three_d_props.current_axis) in\
           self.main.three_d_props.current_properties:
            del self.main.three_d_props.current_properties[\
                str(self.main.three_d_props.current_frame)+\
                str(self.main.three_d_props.current_axis)]
            self.change_image()
        else:
            self.change_image()


    def change_axis(self):
        if self.imageCube.dtype != 'object':
            self.current_frame = 0
            if self.xbutton.isChecked():
                self.current_axis = 2
            if self.ybutton.isChecked():
                self.current_axis = 1
            if self.zbutton.isChecked():
                self.current_axis = 0
            self.setup()
            self.change_image()
            self.main.drawim()
        else:
            self.zbutton.setChecked(True)
            msg = 'Only the z axis is available with different size arrays'
            QMessageBox.information(self,'Note',msg)


    def change_image(self):
        self.current_frame = int(self.fnumbar.value())
        self.fnumber.setText(str(self.current_frame))
        if self.current_axis == 0:
            self.main.image = self.imageCube[self.current_frame]
            self.main.head = self.headerCube[self.current_frame]
        if self.current_axis == 1:
            self.main.image = self.imageCube[:,self.current_frame,:]
        if self.current_axis == 2:
            self.main.image = self.imageCube[:,:,self.current_frame]
        self.main.scale()

        name = str(self.current_frame)+str(self.current_axis)
        if name not in self.frame_properties:
            self.main.guess_white_black()
            if self.main.orig == 'upper':
                self.main.imshow.canvas.ax.set_ylim([self.main.imageedit.shape[0]-0.5,-0.5])
            else:
                self.main.imshow.canvas.ax.set_ylim([-0.5,self.main.imageedit.shape[0]-0.5])
            self.main.imshow.canvas.ax.set_xlim([-0.5,self.main.imageedit.shape[1]-0.5])

        if self.imageCube.dtype != 'object':
            self.replay_history()
            self.main.update_canvas()
        else:
            self.main.setup_image_info()
            self.replay_history()


    def replay_history(self):
        name = str(self.current_frame)+str(self.current_axis)
        if name in self.frame_properties:
            for func, args in self.frame_properties[name]:
                func(args)

    def save_scale_and_color(self):
        #This saves the extents and scaling from the last image
        frame = "{}{}".format(self.current_frame,self.current_axis)
        frame_extents = [self.main.set_extents, [self.main.imshow.canvas.ax.get_ylim(),
            self.main.imshow.canvas.ax.get_xlim()]]
        frame_scale = [self.main.set_scale, [self.main.white, self.main.black]]
        self.frame_properties[frame]  = [frame_extents, frame_scale]
        self.change_image()


    def update_slider(self):
        next_frame = int(self.fnumbar.value()) + 1
        if next_frame > self.length:
            next_frame = 0
        self.fnumbar.setValue(next_frame)
        self.save_scale_and_color()

    def playback(self):
        if self.going == 0:
            self.play.setText('Stop')
            speed = float(self.delay.text())
            self.mytimer.start(1000*speed)
            self.going = 1
        else:
            self.mytimer.stop()
            self.play.setText('Play')
            self.going = 0


