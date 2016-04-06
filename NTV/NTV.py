#! /usr/bin/env python
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import numpy as np
import astropy.io.fits as astroIo
import astropy.wcs as astroWcs
from astropy.coordinates import SkyCoord
import matplotlib.pyplot
import sys
import time
import json
import textwrap
import matplotlib.pyplot as plt
import matplotlib as mpl
from threading import Lock
import os
import importlib
import NTV as me
from utils import ifImage, myDockWidget


if sys.platform == 'darwin':
    plug_loc = os.path.expanduser('~/Library/Application Support/NTV')
elif sys.platform == 'win32':
    plug_loc = os.path.join(environ['APPDATA'], 'NTV')
else:
    plug_loc = os.path.expanduser(os.path.join("~", "." + 'NTV'))

if os.path.isdir(plug_loc) == False:
    os.mkdir(plug_loc)

plug_loc = os.path.join(plug_loc,'plugins')
if os.path.isdir(plug_loc) == False:
    os.mkdir(plug_loc)



#each of the rstrips is to deal with python 2/3 compatability
cwd = me.__file__.rstrip('__init__.py').rstrip('NTV.py').rstrip('NTV.pyc')
sys.path.insert(1,cwd)
sys.path.insert(1,cwd+'UI_DIR')
sys.path.insert(1,cwd+'plugins')
sys.path.insert(1,plug_loc)

base_loc = os.path.join(cwd,'plugins')
user_loc = plug_loc


def find_plugins():
    plugins_dict = {}

    base_loc  = os.path.join(cwd,'plugins')
    base_list = os.listdir(base_loc)
    for i in base_list:
        if os.path.isdir(os.path.join(base_loc,i)) and i.startswith('__') == False:
            try:
                manifest = json.load(open(os.path.join(base_loc,i,'manifest.txt'),'r'))
                plugins_dict[i] = {'manifest':manifest,'dir':base_loc}
            except Exception as e:
                print(e)

    user_list = os.listdir(plug_loc)
    for i in user_list:
        if os.path.isdir(os.path.join(plug_loc,i)) and i.startswith('__') == False:
            manifest = json.load(open(os.path.join(user_loc,i,'manifest.txt'),'r'))
            plugins_dict[i] = {'manifest':manifest,'dir':user_loc}
    return plugins_dict

plugins_global_dict = find_plugins()

for plug in plugins_global_dict:
    if plugins_global_dict[plug]['manifest']['type'] == 'core':
        globals()[plug] = getattr(importlib.import_module('{}.{}'.format(plug,plug)),plug)


from UI_DIR.NTV_UI import Ui_NTV

#This variable is purely used for internal coding practices to force a config rewrite
Update_config = False

class NTV(QMainWindow,Ui_NTV):
    '''
    This is the main program. It implements the event loop, and handles user interaction.
    This can be either ran from the supplied script, or embeding it in a python session,
    see the embed class for details on how to do that. Data can be either loaded into the
    program with open from the file menu, by dragging and dropping files, invoking a file
    path from the command line, or using the showArray method if using in embed mode.
    '''
    def __init__(self,file=None,parent=None,port=None):
        super(NTV,self).__init__(parent)
        self.setupUi(self)
        self.setDockOptions(QMainWindow.ForceTabbedDocks |QMainWindow.VerticalTabs)
        #These lines set the application data used to save the settings
        QCoreApplication.setOrganizationName('NTV_project')
        QCoreApplication.setOrganizationDomain('code.google.com/p/ntv/')
        QCoreApplication.setApplicationName('NTV')
        self.settings = QSettings('NTV_project', 'NTV')
        #check to see if a config file has been created if not create one
        if self.settings.value('has_config').toInt()[0] == 0:
            self.write_config()
        #If new preference objects are added,
        if Update_config == True:
            self.write_config()

        #load the information from the save file
        self.read_config()
        #change the scope of the pipe object in order for it to be referenced from other parts of the class
        self.port     = port

        #start by hiding the x and y views of the image
        self.ygview.hide()
        self.xgview.hide()

        #Constants used by program, funloaded gets set to 1 when there is a
        #file loaded, provides a check for manipulating functions
        #homeImage is used to tell draw new image without preserving limits
        self.funloaded = 0
        self.head = None
        self.imagecube = None
        self.homeImage = 0
        self.details_view_dict = {}
        self.mpl_conn_dict = {}
        self.current_ax = None #the figure axes the mouse is in, window or colorbar
        self.plugins_dict = {}
        self.plugins_module_dict = {}
        self.plugins_dock_dict = {}
        self.plugins_dock_list = []
        self.base_loc = base_loc
        self.user_loc = user_loc
        self.wcs = None

        #Set some UI elements

        #This handels dranging and dropping operations
        self.centy.dragEnterEvent = self.lbDragEnterEvent
        self.centy.dropEvent = self.lbDropEvent

        #set ui element
        self.filelab.setText("<font color=red>Load File</font>")

        #populate the colormap drop down box with available color maps
        self.cmaplist = list(matplotlib.cm.datad.keys())
        self.cmapbox.insertItems(0, self.cmaplist)
        self.cmapbox.setCurrentIndex(self.cmaplist.index('Blues_r'))

        #create some scenes for rending objects
        self.minipix_scene = QGraphicsScene() #the mini-privew window scene
        self.minipix_scene.setBackgroundBrush(QColor(255,255,255))
        self.minipix.setScene(self.minipix_scene) #the widget that displays the mini-preview

        self.pixval_scene = QGraphicsScene()#scene to render the current mouse location
                                            #and value in the figure
        self.pixval_scene.setBackgroundBrush(QColor(210,231,236))
        self.pixval.setScene(self.pixval_scene)#widget that renders the pixvalues

        self.sceney = QGraphicsScene()
        self.ygview.setScene(self.sceney)
        self.sceney.setBackgroundBrush(QColor(255,255,255))

        self.scenex = QGraphicsScene()
        self.xgview.setScene(self.scenex)
        self.scenex.setBackgroundBrush(QColor(255,255,255))

        #disable opengl on linux machines as there are many bugs and tearning with it
        if sys.platform == 'darwin' or sys.platform == 'win32':
            #if opengl is present, use it to cut down on cpu useage
            try:
                from PyQt4 import QtOpenGL
                self.minipix.setViewport(QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers)))
                self.pixval.setViewport(QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers)))
                self.gyview.setViewport(QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers)))
                self.gxview.setViewport(QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers)))
            except:
                pass

        #These connect each of the UI elements with their associated action
        QObject.connect(self.cmapbox,SIGNAL('activated(int)'),self.cmapupdate)
        self.imshow.canvas.fig.canvas.mpl_connect('motion_notify_event',self.mouseplace)
        self.imshow.canvas.fig.canvas.mpl_connect('axes_enter_event',self.which_axis)
        QObject.connect(self.lincheck,SIGNAL('toggled(bool)'),self.change_scale)
        QObject.connect(self.actionOpen,SIGNAL('triggered()'),self.open)
        QObject.connect(self.actionHeader_2,SIGNAL('triggered()'),self.header)
        QObject.connect(self.actionAbout,SIGNAL('triggered()'),self.about)
        QObject.connect(self.actionQuit,SIGNAL('triggered()'),self.close)
        QObject.connect(self.actionPreferences,SIGNAL('triggered()'),self.prefer)
        QObject.connect(self.pushButton,SIGNAL('clicked()'),self.getclick)
        QObject.connect(self.ycheckbox,SIGNAL('toggled(bool)'),self.showy)
        QObject.connect(self.xcheckbox,SIGNAL('toggled(bool)'),self.showx)
        self.imshow.canvas.fig.canvas.mpl_connect('motion_notify_event',
                                                  self.color_press_motion)
        self.imshow.canvas.fig.canvas.mpl_connect('button_press_event',
                                                  self.color_press_motion)
        self.imshow.canvas.fig.canvas.mpl_connect('button_release_event',self.color_right_rel)
        self.imshow.canvas.fig.canvas.mpl_connect('motion_notify_event',self.color_right_rel)
        self.imshow.canvas.fig.canvas.mpl_connect('scroll_event',self.color_right_rel)
        self.imshow.toolbar.actions()[0].triggered.connect(self.nav_home)

        #fuctions for minimap scaling
        self.func = lambda x,max,min: (255/(max-min))*x-(255*max/(max-min))+255

        #save the plugins dict into the class
        self.plugins_global_dict = plugins_global_dict
        #create the link to update plugins
        self.menuPlugins.addAction('Plugin Manager',self.run_manager)
        self.menuPlugins.addSeparator()
        #force three d plugin to be added and linked properly so that it can always
        #be brought back up
        self.threeDaction = self.menuImage.addAction('Three D',self.plugin_clicked)
        self.threeDaction.setObjectName('three_d')
        self.plugins_module_dict['three_d'] = importlib.import_module('three_d.three_d')

        #load in the addon plugins
        self.load_plugins()

        #This checks for files loaded with the program from the command line
        if file:
            self.process_file(file,'actionOpen')

        #Checks to see if a port was passed, ie if the program is being used in embeded mode, if so,
        #starts the thread that will listen to the pipe It is important that this be last, so the program
        #can be fully initiated so the listener can detect which modules are loaded
        try:
            #check to see if zmp is available, if so bind to a port to talk over
            import zmq
            context = zmq.Context()
            self.sock    = context.socket(zmq.REP)
            self.lock    = Lock()
            #            self.sock = context.socket(zmq.PULL)
            if port == None:
                self.port = self.sock.bind_to_random_port('tcp://127.0.0.1')
            else:
                    self.sock.bind('tcp://127.0.0.1:'+str(self.port))
                    self.recive = listener(self,self.port,self.sock,self.lock)
                    self.recive.start()
                    self.setWindowTitle('NTV - Listening on tcp://127.0.0.1:'+str(self.port))
        except:
            self.setWindowTitle('NTV - Error with ZMQ')


    def closeEvent(self,event):
        '''
        This function overloads the closing of the window function, it cleans up the openQL
        functions, and unbinds the socket currently bound
        '''
        self.minipix.setParent(None)
        self.pixval.setParent(None)
        try:
            self.gyview.setParent(None)
            self.gxview.setParent(None)
            del self.gyview, self.gview
        except:
            pass
        del self.minipix, self.pixval
        try:
            self.sock.unbind('tcp://127.0.0.1:'+str(self.port))
        except:
            pass
        event.accept()

    def run_manager(self):
        plugman = plugin_manager(self)

    def reload_plugins(self):
        self.menuPlugins.clear()
        self.menuPlugins.addAction('Plugin Manager',self.run_manager)
        self.menuPlugins.addSeparator()
        self.plugins_global_dict = find_plugins()
        self.load_plugins()


    def load_plugins(self):
        self.plugins_dir_list = []
        for plug in self.plugins_global_dict:
            if self.plugins_global_dict[plug]['manifest']['type'] == 'addon':
                self.plugins_dir_list.append(plug)
        qactions = [self.menuPlugins.addAction(\
                    self.plugins_global_dict[x]['manifest']['name'].title(),\
                    self.plugin_clicked)\
                    for x in self.plugins_dir_list]
        for i in range(len(qactions)):
            qactions[i].setObjectName(self.plugins_dir_list[i])
        for plug in self.plugins_dir_list:
            self.plugins_module_dict[plug] = importlib.import_module('%s.%s'%(plug,plug))


    @ifImage
    def plugin_clicked(self, plugin=None, hidden=False):
        '''
        This function handles when plugins are clicked, and generates the
        toolbar popup on the right side of the image.
        '''
        # Get the name of the plugin which was clicked
        if not plugin or type(plugin) != type(''):
            plugin = str(self.sender().objectName())

        # If the dictionary which contains the currently active plugins
        # already contains the name of the plugin, then the plugin must be
        # active, and persistent, simply show the plugin and raise it to
        # view
        if plugin in self.plugins_dock_dict and not hidden:
            self.plugins_dock_dict[plugin].show()
            self.plugins_dock_dict[plugin].raise_()

        # Else the Plugin needs to be created. If the plugin is persistent,
        # use the name of the plugin in the dictionary, else use the
        # current time as the dictionary key
        else:
            try:
                if self.plugins_global_dict[plugin]['manifest']["persistant"] == 'True':
                    ident   = plugin
                    persist = True
                else:
                    ident  = time.ctime()
                    persist = False
            except:
                ident   = time.ctime()
                persist = False
            tmp = self.plugins_module_dict[plugin]
            self.plugins_dock_dict[ident] = myDockWidget(plugin,ident,persist,parent=self)
            self.plugins_dock_dict[ident].setWindowTitle(self.plugins_global_dict[plugin]['manifest']['name'])
            QObject.connect(self.plugins_dock_dict[ident],SIGNAL('closing'),self.plugin_closed)
            self.plugins_dock_dict[ident].setObjectName(plugin)
            self.plugins_dock_dict[ident].setAllowedAreas(Qt.RightDockWidgetArea)
            self.plugins_dict[ident] = getattr(tmp,plugin)(self, parent=self.plugins_dock_dict[ident])
            self.plugins_dock_dict[ident].setWidget(self.plugins_dict[ident])

            # If the plugin should be hidden, hide it
            if hidden:
                self.plugins_dock_dict[ident].hide()

            # If there are no dock widgets, create one, else append new
            # widgets by adding tabs
            if len(self.plugins_dock_list) < 1:
                self.addDockWidget(Qt.RightDockWidgetArea,self.plugins_dock_dict[ident])
                self.plugins_dock_list.append(ident)
            else:
                self.tabifyDockWidget(self.plugins_dock_dict[self.plugins_dock_list\
                                  [-1]],self.plugins_dock_dict[ident])
                self.plugins_dock_list.append(ident)

    def plugin_closed(self,ident):
        QObject.disconnect(self.plugins_dock_dict[ident],SIGNAL('closing'),self.plugin_closed)
        try:
            del self.plugins_dict[ident]
            del self.plugins_dock_dict[ident]
            for i in range(len(self.plugins_dock_list)):
                if self.plugins_dock_list[i] == ident:
                    del self.plugins_dock_list[i]
        except:
            pass
        pass

    @ifImage
    def which_axis(self,event):
        '''
        sets the figure axes the mouse last in, differentiates between the figure and the
        colorbar
        '''
        self.current_ax = event.inaxes

    def showy(self):
        '''
        This function toggles the y virtical view around the cursor
        '''
        if self.ycheckbox.isChecked():
            self.ygview.show()

        else:
            self.ygview.hide()

    def showx(self):
        '''
        This function toggles the x virtical view around the cursor
        '''
        if self.xcheckbox.isChecked():
            self.xgview.show()
        else:
            self.xgview.hide()


    def prefer(self):
        pref_box(self.settings,parent=self)

    def about(self):
        '''
        displays the about message
        '''
        msg = '''NTV
        This program is to help visualize astronomical data, and update
        available tools such as ATV which is an idl project. NTV is
        designed to integrate better with python and is designed to be 
        easily exteded for future needs.

        Website:
        Written by: Nate Lust, University of Central Florida.
        '''
        QMessageBox.about(self,'NTV about',textwrap.dedent(msg))

    def write_config(self):
        '''
        Initialize the config file if one dose not exist
        '''
        self.settings.setValue('previewsize',20)
        self.settings.setValue('cutsize',3)
        self.settings.setValue('origin','upper')
        self.settings.setValue('dbox',0)
        self.settings.setValue('has_config',1)
        self.settings.sync()

    def read_config(self):
        '''
        reads the config file from the system and sets the constants, and program flow
        based on this.
        '''
        if sys.version_info[0] >= 3:
            self.previewsetting = int(self.settings.value('previewsize'))
            self.previewsize = self.previewsetting
            self.rebinfactor = 200/self.previewsize/2
            self.cutrad = int(self.settings.value('cutsize'))
            self.orig = self.settings.value('origin')
            self.dboxplot = int(self.settings.value('dbox'))
            self.sizeofcut.setText(str(self.cutrad))
        else:
            self.previewsetting = self.settings.value('previewsize').toInt()[0]
            self.previewsize = self.previewsetting
            self.rebinfactor = 200/float(self.previewsize)/2.
            self.cutrad = self.settings.value('cutsize').toInt()[0]
            self.orig = self.settings.value('origin').toString()
            self.dboxplot = self.settings.value('dbox').toInt()[0]
            self.sizeofcut.setText(str(self.cutrad))

    def check_preview(self):
        '''
        This is to check to make sure that the preview size is less than the size of a fits file,
        if it is now, it decreases the preview size.
        '''
        if self.image.shape[0]<self.previewsize*2 or self.image.shape[1]<self.previewsize*2:
            self.previewsize = 5
            self.rebinfactor=200/self.previewsize/2

    @ifImage
    def header(self):
        '''
        This function serves to create a header_view instance to show
        the header information in a dialog box
        '''
        if self.head != None:
            hd = self.head
            self.head_view = header_view(hd.cards)

    def rec_data(self,array):
        '''
        This is the fucntion that is used to update the image variable of
        the class if the program is used in embeded mode, and an array is
        passed to the pipe.
        '''
        self.image = array
        self.filelab.setText("<font color=blue>Numpy Array</font>")
        self.loadinfo(image)

    def getclick(self):
        '''
        This is just a wrapper class to pass the get star button event to the
        drawbox function. Uses the mpl backend to connect to the canvas object
        and get the event.
        '''
        self.connectclick(self.drawbox)

    @ifImage
    def connectclick(self,func):
        '''
        connect a button press on the mpl canvas to a supplied function
        '''
        self.imshow.canvas.fig.canvas.setCursor(QCursor(Qt.CrossCursor))
        ident = time.ctime()
        self.mpl_conn_dict[ident] = self.imshow.canvas.\
                                        fig.canvas.mpl_connect('button_press_event',\
                                        lambda x: self.revert_mouse(x, func, ident))

    def revert_mouse(self,event,func,ident):
        '''
        reset the mouse cursor back to normal after the click
        '''
        self.imshow.canvas.fig.canvas.mpl_disconnect(self.mpl_conn_dict[ident])
        del self.mpl_conn_dict[ident]
        self.imshow.canvas.fig.canvas.setCursor(QCursor(Qt.ArrowCursor))
        if self.current_ax == self.imshow.canvas.ax:
            func(event)


    def del_detail_list_item(self,listno):
        '''
        This function removes references to details views once they have been closed
        '''
        del self.details_view_dict[listno]

    @ifImage
    def drawbox(self,event):
        '''
        This function recives an event from the mpl canvas and passes certain data to the
        constructor function of the details view class
        '''
        #get aperature size from size of cut widget
        cutv = int(self.sizeofcut.text())
        #create an instance of details_view class. The if statement is to check and see
        #if the box should be overplotted or not
        if self.dboxplot == 0:
            ident = time.ctime()
            self.details_view_dict[ident] = details_view(self,\
                 ident,self.image,\
                 self.imageedit,event.xdata,event.ydata,cutv,self.white,self.black,\
                 self.z,self.dboxplot)
        if self.dboxplot == 1:
            #Try statement is to catch if there is not a window open already
            try:
                #Save the location on the screen to restore too
                self.detail_geometry = self.details_box.geometry()
                #close the existing box
                self.details_box.close()
            except:
                pass
            #Create the window to keep track of details view
            self.details_box = details_view(self,0,self.image,self.imageedit\
                               ,event.xdata,event.ydata,cutv,self.white,self.black,\
                               self.z,self.dboxplot)
            try:
                #Try and reset the geometry, try is used to catch if the window is not open
                self.details_box.setGeometry(self.detail_geometry)
            except:
                pass


    def open(self):
        '''
        Impliments open from the file menu and updates the program accordingly
        '''
        #This is to ensure the loading of info happens correctly and that ntv dosnt stay stuf on embed
        #try statement simply to catch the terminal output
        try:
            file = str(QFileDialog.getOpenFileName(self,'Select Files to Process','~/'))
        except:
            pass
        if file != '':
            sender = self.sender().objectName()
            self.process_file(file,sender)


    def process_file(self,file,sender):
        '''
        checks to see if a loaded file is a fits files, and if so passes it to be
        loaded, if not it notifys the user
        '''
        if file.find('fits') != -1 or file.find('FIT')!=-1 or file.find('fit')!=-1:
            self.path = file
            self.loadinfo()
        else:
            self.filelab.setText('<font color=red>Invalid Format</font>')

    def lbDragEnterEvent(self, event):
        '''
        updates the mouse for drop events. Should be updated in the future for proper
        handeling of file detection
        '''
        event.accept()

    def lbDropEvent(self, event):
        '''
        Gets a file that was dropped to the program, checks for compatability and up dates
        the image accordinly. TO DO: change file checking to its own separate function to
        call, was not an issue orrigionally
        '''
        link=event.mimeData().urls()
        file = str(link[0].toLocalFile())
        self.process_file(file)

    @ifImage
    def mouseplace(self,event):
        '''
        Handles the mouse motion over the imshow mpl canvas object. This function now 
        also updates the x and y views if they are visible
        need better handeling of sizes and edge handeling for x and y views
        '''
        if self.current_ax == self.imshow.canvas.ax:
                #makes sure the mouse is on the data canvas
            if event.ydata != None and event.xdata != None:
                # This next bit is to handle the preview problem at the boundary.
                # It will create the preview based
                # on mouse position, and boundary value if you get close to boundary.
                ystart = event.ydata-self.previewsize
                ystop  = event.ydata+self.previewsize
                xstart = event.xdata-self.previewsize
                xstop  = event.xdata+self.previewsize
                ydif = 0
                xdif = 0
                if event.ydata<self.previewsize:
                    ystart = 0
                    ystop = self.previewsize*2
                    ydif = self.previewsize-event.ydata
                if event.ydata>self.image.shape[0]-1-self.previewsize:
                    ystart = self.image.shape[0]-1-self.previewsize*2
                    ystop = self.image.shape[0]-1
                    ydif = (self.image.shape[0]-1-event.ydata)-self.previewsize
                if event.xdata<self.previewsize:
                    xstart = 0
                    xstop  = self.previewsize*2
                    xdif = self.previewsize-event.xdata
                if event.xdata>self.image.shape[1]-1-self.previewsize:
                    xstart = self.image.shape[1]-1-self.previewsize*2
                    xstop  = self.image.shape[1]-1
                    xdif = (self.image.shape[1]-1-event.xdata)-self.previewsize
                if np.abs(ydif) > self.previewsize-3:
                    ydif = self.previewsize-3
                    if ydif <0:
                        ydif = -1*ydif
                if np.abs(xdif) > self.previewsize-3:
                    ydif = self.previewsize-3
                    if xdif <0:
                        xdif = -1*xdif

                self.impix = self.imageedit[ystart:ystop,xstart:xstop].copy()

                #This next few lines is to simply set the values of several pixels to white in order to draw a cross hair
                smmask = np.zeros(self.impix.shape,dtype=bool)
                smmask[self.previewsize-2-ydif,self.previewsize-xdif] = True
                smmask[self.previewsize-1-ydif,self.previewsize-xdif] = True
                smmask[self.previewsize+1-ydif,self.previewsize-xdif] = True
                smmask[self.previewsize+2-ydif,self.previewsize-xdif] = True
                smmask[self.previewsize-ydif,self.previewsize-2-xdif] = True
                smmask[self.previewsize-ydif,self.previewsize-1-xdif] = True
                smmask[self.previewsize-ydif,self.previewsize+1-xdif] = True
                smmask[self.previewsize-ydif,self.previewsize+2-xdif] = True
                #This next bit is to convert the numpy array into something that can be displayed as a pixmap.
                self.impix = self.func(self.impix,self.white,self.black)
                self.impix[self.impix>255] = 255
                self.impix[self.impix<0] = 0
                gray = self.impix.astype(np.uint8)
                if self.orig == 'lower':
                    gray[:,:] = gray[::-1,:]
                new_mask = gray > 240
                gray[smmask] = 255
                gray[smmask*new_mask] = 0
                h, w = gray.shape
                gray = self.z(gray,alpha=True,bytes=True)
                gray = gray.astype(np.uint8)
                gray[:,:,:3] = gray[:,:,:3][:,:,::-1]
                result = QImage(gray, w, h,\
                         QImage.Format_RGB32)
                self.minipix_scene.clear()
                pixmap = QPixmap.fromImage(result)
                self.minipix_scene.addPixmap(pixmap)
                matrix = QMatrix()
                matrix.scale(self.rebinfactor-0.1, self.rebinfactor-0.1)
                self.minipix.setMatrix(matrix)
                self.minipix_scene.update()
                self.pixval_scene.clear()
                #try:
                coord = SkyCoord(*self.wcs.all_pix2world(event.xdata, event.ydata, 0,
                                 ra_dec_order=True), unit='deg')
                hour = coord.ra.hour
                raMinute = (hour-int(hour))*60
                raSecond = (raMinute - int(raMinute))*60
                dec = coord.dec.deg
                decMinute = (dec - int(dec))*60
                decSecond = (decMinute - int(decMinute))*60
                ra = "{:.0f}:{:.0f}:{:.2f}".format(hour, raMinute, raSecond)
                dec = "{:.0f}:{:.0f}:{:.2f}".format(dec, decMinute, decSecond)
                #except:
                #    ra,dec = (0.0,0.0)
                text_save = QGraphicsTextItem('%s\n%.2f\n%.2f\n%s\n%s'%(self.image[event.ydata,\
                                     event.xdata], event.xdata, event.ydata, ra, dec))
                text_save.setPos(0,0)
                self.pixval_scene.addItem(text_save)
                self.pixval_scene.update()

                #this next part is to mess with the y cut view
                if self.ycheckbox.isChecked():
                                self.sceney.clear()
                                #set to viewing every other pixel if in full frame
                                if np.abs(self.imshow.canvas.ax.get_ylim()[0] -self.imshow.canvas.ax.get_ylim()[1]) == self.imageedit.shape[0]:
                                    self.ybarheights = self.imageedit[::2,event.xdata]
                                    self.ybaroffset=0
                                else:
                                    self.ybarheights = self.imageedit[int(self.imshow.canvas.ax.get_ylim()[1]):int(self.imshow.canvas.ax.get_ylim()[0]),event.xdata]
                                    self.ybaroffset=2
                                for index in np.arange(len(self.ybarheights)):
                                    self.sceney.addRect(0,index+index*self.ybaroffset,(self.ybarheights[index]-self.ybarheights.min())*(self.ygview.size().width()/(self.ybarheights.max()-self.ybarheights.min())),self.ybaroffset,brush=QBrush(QColor(23,108,179)),
                                    pen=QPen(QColor(23,108,179)))

                                maxy = QGraphicsTextItem("Maxium: "+str(self.ybarheights.max()))
                                maxy.setPos((self.ybarheights.max()-self.ybarheights.min())*(self.ygview.size().width()/(self.ybarheights.max()-self.ybarheights.min())),index+index*self.ybaroffset+10)
                                maxy.rotate(90)
                                self.sceney.addItem(maxy)
                                medy = QGraphicsTextItem("Minimum: "+str(self.ybarheights.min()))
                                medy.setPos((self.ybarheights.max()-self.ybarheights.min())*0.2*(self.ygview.size().width()/(self.ybarheights.max()-self.ybarheights.min())),index+index*self.ybaroffset+10)
                                medy.rotate(90)
                                self.sceney.addItem(medy)
                                self.ygview.fitInView(0.,0.,self.ygview.size().width(),self.ygview.size().height())

                if self.xcheckbox.isChecked():
                                self.scenex.clear()
                                #set to viewing every other pixel if in full frame

                                if self.imshow.canvas.ax.get_xlim()[1] -self.imshow.canvas.ax.get_xlim()[0] == self.imageedit.shape[1]:
                                    self.xbarheights = self.imageedit[event.ydata,::2]
                                    self.xbaroffset=0

                                else:
                                    self.xbarheights = self.imageedit[event.ydata,int(self.imshow.canvas.ax.get_xlim()[0]):int(self.imshow.canvas.ax.get_xlim()[1])]
                                    self.xbaroffset=2
                                for indexx in np.arange(len(self.xbarheights)):
                                    self.scenex.addRect(indexx+indexx*self.xbaroffset,0,self.xbaroffset,-1*(self.xbarheights[indexx]-self.xbarheights.min())*(self.xgview.size().height()/(self.xbarheights.max()-self.xbarheights.min())),brush=QBrush(QColor(23,108,179)),
                                    pen=QPen(QColor(23,108,179)))
                                maxx = QGraphicsTextItem("Maxium: "+str(self.xbarheights.max()))
                                maxx.setPos(indexx+indexx*self.xbaroffset+10,-1*(self.xbarheights.max()-self.xbarheights.min())*(self.xgview.size().height()/(self.xbarheights.max()-self.xbarheights.min())))
                                self.scenex.addItem(maxx)
                                medx = QGraphicsTextItem("Minimum: "+str(self.xbarheights.min()))
                                medx.setPos(indexx+indexx*self.xbaroffset+10,-1*(self.xbarheights.max()-self.xbarheights.min())*0.2*(self.xgview.size().height()/(self.xbarheights.max()-self.xbarheights.min())))
                                self.scenex.addItem(medx)
                                self.xgview.fitInView(0.,0.,self.xgview.size().width(),self.xgview.size().height())



    def make_white_black(self):
        if self.contrast < 0.001:
            self.contrast = 0.01
        self.white = self.gray+self.max_m_min*self.contrast
        self.black = self.gray-self.max_m_min*self.contrast
        if self.white > self.imageedit.max():
            self.white = self.imageedit.max()
        if self.black < self.imageedit.min():
            self.black = self.imageedit.min()
        self.update_canvas()

    def guess_white_black(self):
        try:
            hist,bin_edges = np.histogram(abs(self.imageedit).flat,100)
            cdf = np.cumsum(np.log(hist[hist>0]))
            cdf = cdf / float(cdf[-1])
            self.white = bin_edges[:-1][cdf<=0.60][-1]
            self.black = bin_edges[:-1][cdf<=0.20][-1]
        except:
            mean = np.mean(self.imageedit)
            self.white = mean + np.std(self.imageedit)
            self.black = mean - np.std(self.imageedit)


    def make_gray_const(self):
        self.max_m_min = self.imageedit.max()-self.imageedit.min()
        self.contrast = ((self.white - self.black)/2./self.max_m_min)
        self.gray = self.black+(self.white-self.black)/2.


    def update_canvas(self):
        self.make_gray_const()
        self.emit(SIGNAL('update_main_canvas'))
        self.imdata.set_data(self.imageedit)
        self.imdata.colorbar.set_array(self.imageedit)
        self.imdata.colorbar.boundaries = np.linspace(self.imageedit.min(),self.imageedit.max(),1000)
        self.imdata.colorbar.autoscale()
        self.imdata.set_clim(vmax=self.white,vmin=self.black)
        self.imdata.changed()
        self.imshow.canvas.draw()


    def color_press_motion(self,event):
        if event.button == 1 and event.inaxes == self.colorbar.ax and event.dblclick == False:
            self.last_gray = self.gray
            self.gray = self.max_m_min*event.ydata+self.imageedit.min()
            self.make_white_black()
        if event.button == 1 and event.inaxes == self.colorbar.ax and event.dblclick:
            self.gray = self.last_gray
            self.make_white_black()
            tmp = self.plugins_module_dict['levels']
            self.level_view = eval('tmp.levels(self,None)')


    def color_right_rel(self,event):
        if event.button ==3 and event.inaxes == self.colorbar.ax and int(event.ydata*10)%1 == 0:
            self.contrast = abs((self.gray-self.imageedit.min())/self.max_m_min-event.ydata)
            self.make_white_black()
        if event.button == 'up' and event.inaxes == self.colorbar.ax and abs(event.step) >0:
            self.contrast = self.contrast + event.step*0.05
            self.make_white_black()
        if event.button == 'down' and event.inaxes == self.colorbar.ax and abs(event.step) > 0:
            self.contrast = abs(self.contrast + event.step*0.05)
            self.make_white_black()

    @ifImage
    def change_scale(self, extra):
        self.scale()
        self.guess_white_black()
        self.update_canvas()

    def set_extents(self,extents):
        self.imshow.canvas.ax.set_ylim(extents[0])
        self.imshow.canvas.ax.set_xlim(extents[1])

    def set_scale(self,colors):
        self.white = colors[0]
        self.black = colors[1]

    @ifImage
    def scale(self):
        '''
        Update the image accordingly to which option the user chooses for scaling,
        log or linear
        '''
        if self.lincheck.isChecked():
            self.imageedit = self.image
        if self.logcheck.isChecked():
            self.imageedit = self.image.copy()
            self.imageedit[np.where(self.imageedit <=0)]=0.001
            self.imageedit = np.log(self.imageedit)

    @ifImage
    def cmapupdate(self, extra):
        '''
        Simply redraw the canvas if the colormap is changed
        '''
        self.ctext = str(self.cmapbox.currentText())
        self.z = getattr(matplotlib.pyplot.cm, self.ctext)
        self.imdata.set_cmap(self.z)
        self.imshow.canvas.draw()

    def make_threed_list(self,array):
        tarray = array.tolist()
        for i in range(len(tarray)):
            tarray[i] = np.array(tarray[i])
        return tarray

    def loadinfo(self, image=None):
        '''
        Load in a file if not in embeded mode. Function updates labels accordingly
        '''
        self.filelab.setText("<font color=blue>"+self.path+"</font>")
        if image:
            head = None
        else:    
            image, head = astroIo.getdata(self.path,header=True)

        # Catch nans and set to zero for now
        image[image != image] = 0
        #Set funloaded to 1 to turn on interactions with UI elements
        self.funloaded = 1

        #This section loads the threed data if there is any. sets the frame as the first element,
        #similar behaivor happens from the embed side function
        self.plugin_clicked(plugin='three_d', hidden=True)
        threeDWidget = self.plugins_dock_dict['three_d'].widget()
        threeDWidget.addImage(image)
        # Add a header object for each image in possible image cube
        if len(image.shape) == 3:
            [threeDWidget.addHeader(head) for x in range(image.shape[0])]
        else:
            threeDWidget.addHeader(head)
        # Do work depending on shape of image
        if len(image.shape) == 3:
            self.image = image[0]
            self.threeDaction.trigger()
        else:
            self.image = image
        self.head = head
        self.setup_image_info()

    def renderinfo(self):
        #This signal gets emited to update a three d control window that may
        #happen to be open
        self.emit(SIGNAL('update_3d'))
        self.setup_image_info()

    def setup_image_info(self):
        self.previewsize = self.previewsetting
        self.rebinfactor = 200/self.previewsize/2
        self.imageedit = self.image
        #set all the initial scalling for the
        self.guess_white_black()
        #set associated information
        self.minlab.setText(str(self.image.min()))
        self.maxlab.setText(str(self.image.max()))
        self.xdim.setText(str(self.image.shape[1]))
        self.ydim.setText(str(self.image.shape[0]))
        self.check_preview()
        self.homeImage = 1
        if self.head:
            #try:
            self.wcs = astroWcs.WCS(self.head)
            #except:
            #    self.wcs = None
        self.drawim()
        self.lincheck.setChecked(1)

    def nav_home(self):
        self.homeImage = 1
        self.lincheck.setChecked(True)
        self.image = self.imagecube[0]
        self.imageedit = self.image
        self.three_d_props = Three_D_class(self)
        self.emit(SIGNAL('update_3d'))
        self.guess_white_black()
        self.drawim()

    def drawim(self):
        '''
        This fucntion actually handles the drawing of the imshow mpl canvas.
        It pulls the required elements from the ui on each redraw
        whenever possible try to use update canvas, as it is faster
        '''
        self.emit(SIGNAL('update_main_canvas'))
        #self.max_m_min = self.imageedit.max()-self.imageedit.min()
        #ylims,xlims This is to preserve the zooming when redrawing the image for some reason
        xlims=self.imshow.canvas.ax.get_xlim()
        ylims=self.imshow.canvas.ax.get_ylim()
        #Clear and update the axis on each redraw, this is nessisary to avoid a memory leak
        self.imshow.canvas.fig.clf()
        self.imshow.canvas.ax = self.imshow.canvas.fig.add_subplot(111)
        self.imshow.canvas.format_labels()
        #The next two lines are a bit hacky but are required to properly turn the color map from the listbox to an object so that the map
        #can be updated accordingly
        self.ctext = str(self.cmapbox.currentText())
        self.z = getattr(matplotlib.pyplot.cm, self.ctext)
        #updated the canvas and draw
        self.imdata = self.imshow.canvas.ax.imshow(self.imageedit,vmax=self.white,vmin=self.black,cmap=self.z,interpolation=None,alpha=1,origin=self.orig)
        self.cbbounds  = np.linspace(self.imageedit.min(),self.imageedit.max(),1000)
        self.colorbar = self.imshow.canvas.fig.colorbar(self.imdata,ax = self.imshow.canvas.ax,boundaries=self.cbbounds)
        self.colorbar.ax.tick_params(labelsize=8)
        self.imshow.canvas.fig.subplots_adjust(left=0.05,right=1,top=0.95,bottom=0.05)
        self.imshow.canvas.ax.set_anchor('C')
        self.imshow.canvas.draw()
        self.make_gray_const()
        #This next bit checks if the limits should be restored after a redraw, the cases are at the start
        #of the program or when a new image is loaded
        if self.homeImage == 0:
            self.imshow.canvas.ax.set_ylim(ylims)
            self.imshow.canvas.ax.set_xlim(xlims)
            self.imshow.canvas.draw()
        self.homeImage = 0


if __name__=="__main__":
    from optparse import OptionParser
    usage = "usage: %prog [options] filename"
    parser = OptionParser()
    parser.add_option("-p","--port",dest='port',help='Port to start zmq listening',\
                      metavar='PORT')
    (options, args) = parser.parse_args()
    #This is a section to run the
    import sys
    app = QApplication(sys.argv)
    if len(args) > 0:
        filez = args[0]
    else:
        filez = None
    plot = NTV(file=filez,port=options.port)
    plot.show()
    sys.exit(app.exec_())

'''
TO DO:
implement more dialog information such as s/n calc, ap and an positions, fwhm
get wiki and doc writer
update readme
need to update some comments in the code for the new features.
stop three D window from closing
add circles to view in display window
upload all plugins to github
update all manifests w/ full information
update plugin list
move rest of code to plugins (remote/embed)
look into zmq from remote connection
maybe make a meeting plugin
fix autoscale for small things (low priority)
update plugman for minimum version and plugin type
make everything try for pyside
fix save scale for mixed 3d
'''
