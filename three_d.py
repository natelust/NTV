try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import numpy as np

from .threeD_ui import Ui_ThreeD

class three_d(QWidget,Ui_ThreeD):
    def __init__(self,main,parent=None):
        QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.main = main
        self.going = 0
        self.mytimer = QTimer()
        QObject.connect(self.fnumbar,SIGNAL('sliderReleased()'),self.save_and_update)
        QObject.connect(self.play,SIGNAL('clicked()'),self.playback)
        QObject.connect(self.main,SIGNAL('update_3d'),self.setup)
        QObject.connect(self.mytimer,SIGNAL('timeout()'),self.update_slider)
        QObject.connect(self.xbutton,SIGNAL('clicked()'),self.change_axis)
        QObject.connect(self.ybutton,SIGNAL('clicked()'),self.change_axis)
        QObject.connect(self.zbutton,SIGNAL('clicked()'),self.change_axis)
        QObject.connect(self.clearbutton,SIGNAL('clicked()'),self.clearfunc)
        self.setup()

    def setup(self):
        if self.mytimer.isActive():
            self.mytimer.stop()
        if self.main.three_d_props.current_axis == 0:
            self.zbutton.setChecked(True)
        if self.main.three_d_props.current_axis == 1:
            self.ybutton.setChecked(True)
        if self.main.three_d_props.current_axis == 2:
            self.xbutton.setChecked(True)
        self.length = self.main.imagecube.shape\
                      [self.main.three_d_props.current_axis] - 1
        self.fnumber.setText(str(self.main.three_d_props.current_frame))
        self.fnumbar.setMinimum(0)
        self.fnumbar.setMaximum(self.length)
        self.fnumbar.setValue(self.main.three_d_props.current_frame)

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
        if self.main.imagecube.dtype != 'object':
            self.main.three_d_props.current_frame = 0
            if self.xbutton.isChecked():
                self.main.three_d_props.current_axis = 2
            if self.ybutton.isChecked():
                self.main.three_d_props.current_axis = 1
            if self.zbutton.isChecked():
                self.main.three_d_props.current_axis = 0
            self.setup()
            self.change_image()
            self.main.drawim()
        else:
            self.zbutton.setChecked(True)
            msg = 'Only the z axis is available with different size arrays'
            QMessageBox.information(self,'Note',msg)


    def change_image(self):
        self.main.three_d_props.current_frame = int(self.fnumbar.value())
        self.fnumber.setText(str(self.main.three_d_props.current_frame))
        if self.main.three_d_props.current_axis == 0:
            self.main.image = self.main.imagecube[self.main.three_d_props.current_frame]
        if self.main.three_d_props.current_axis == 1:
            self.main.image = self.main.imagecube[:,self.main.three_d_props.current_frame,:]
        if self.main.three_d_props.current_axis == 2:
            self.main.image = self.main.imagecube[:,:,self.main.three_d_props.current_frame]
        self.main.scale()
        if str(self.main.three_d_props.current_frame)+\
           str(self.main.three_d_props.current_axis) in\
           self.main.three_d_props.current_properties:
            self.main.white = self.main.three_d_props.current_properties\
                              [str(self.main.three_d_props.current_frame)+\
                               str(self.main.three_d_props.current_axis)]['white']
            self.main.black = self.main.three_d_props.current_properties\
                              [str(self.main.three_d_props.current_frame)+\
                               str(self.main.three_d_props.current_axis)]['black']
            ylim = self.main.three_d_props.current_properties\
                              [str(self.main.three_d_props.current_frame)+\
                               str(self.main.three_d_props.current_axis)]['ylim']
            xlim = self.main.three_d_props.current_properties\
                              [str(self.main.three_d_props.current_frame)+\
                               str(self.main.three_d_props.current_axis)]['xlim']
            lims = [ylim,xlim]
        else:
            lims = 'auto'
            self.main.guess_white_black()
        if self.main.imagecube.dtype != 'object':
            self.main.update_canvas(lims=lims)
        else:
            self.main.setup_image_info()

    def save_and_update(self):
        self.main.three_d_props.current_properties\
            [str(self.main.three_d_props.current_frame)+\
             str(self.main.three_d_props.current_axis)] =\
            {'ylim':self.main.imshow.canvas.ax.get_ylim(),
             'xlim':self.main.imshow.canvas.ax.get_xlim(),
             'white': self.main.white,
             'black': self.main.black}
        self.change_image()

    def update_slider(self):
        next_frame = int(self.fnumbar.value()) + 1
        if next_frame > self.length:
            next_frame = 0
        self.fnumbar.setValue(next_frame)
        self.save_and_update()

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


