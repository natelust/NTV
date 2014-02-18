from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import time

from .details import Ui_Dialog

#These next three functions are used to fit a two dimentional Gaussian to a user defined object
#The accuracy of this fit should only be trusted to the tenths place, but it provides a good guess.
#This code was used from the scipy cookbook.
def gaussian(height, center_x, center_y, width_x, width_y):
    width_x = np.float(width_x)
    width_y = np.float(width_y)
    return lambda x,y: height*np.exp(-(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def moments(data):
    total = data.sum()
    X, Y = np.indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = np.sqrt(np.abs((np.arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = np.sqrt(np.abs((np.arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    return height, x, y, width_x, width_y

def fitgaussian(data):
    from scipy import optimize
    params = moments(data)
    errorfunction = lambda p: np.ravel(gaussian(*p)(*np.indices(data.shape)) - data)
    p, success = optimize.leastsq(errorfunction, params)
    return p



#This class implements the dialog box to display information on a particular object that a user
#defines by clicking on it.
class details_view(QDialog,Ui_Dialog):
    '''
    This class is mainly for internal use only. It is used to implement the pop up dialog window
    That displays information about the object that a user selects.
    '''
    def __init__(self,main,listno,frame,frameedit,realx,realy,apsize,clipmax,clipmin,color,dbbox,parent=None):
        super(details_view,self).__init__(parent)
        self.setupUi(self)
        #set the inputs to class members and initialize some variables needed in plotting
        self.listno = listno
        self.frame = frame
        self.framey,self.framex = self.frame.shape
        #This next part is used to check and see if the cutsize needs changed
        if self.framey > self.framex:
            self.flimit = self.framey/2.
        else:
            self.flimit = self.framex/2.
        self.clipmax = clipmax
        self.clipmin = clipmin
        self.color = color
        self.frameedit = frameedit
        self.dbbox    = dbbox
        self.cutsize = apsize*4
        self.apsize = apsize
        self.radin    = apsize*2
        self.radout   = apsize*3
        self.thread3 = None
        self.limit_check()
        #sets the variable that will be used to pick lines and make decisions
        self.artist = None
        #Create a temporary view to centroid with, will be overridden when the true center is found
        view = frame[realy-self.cutsize:realy+self.cutsize,realx-self.cutsize:realx+self.cutsize]
        maxy,maxx = np.where(view==view.max())
        maxy = realy-self.cutsize+maxy[0]
        maxx = realx-self.cutsize+maxx[0]
        view = frame[maxy-self.cutsize:maxy+self.cutsize,maxx-self.cutsize:maxx+self.cutsize]-np.median(frame[maxy-self.cutsize:maxy+self.cutsize,maxx-self.cutsize:maxx+self.cutsize])
        #Finding center and correcting for the cut size
        #The try statemet to to catch any problems when choosing a site that has no star
        try:
            self.y,self.x = fitgaussian(view)[[1,2]]
            #this is a fail safe for if fitgaussian fails
            if np.abs(self.y) > 2*self.cutsize or np.abs(self.x) > 2*self.cutsize:
                self.y = self.cutsize
                self.x = self.cutsize
        except:
            self.y = self.cutsize
            self.x = self.cutsize
        self.totalx = maxx - self.cutsize + self.x
        self.totaly = maxy - self.cutsize + self.y
        self.xval.setText(str(np.round(self.totalx,2)))
        self.yval.setText(str(np.round(self.totaly,2)))
        self.radprof.canvas.fig.canvas.mpl_connect('pick_event',self.on_pic)
        self.radprof.canvas.fig.canvas.mpl_connect('button_release_event',self.button_release_callback)
        self.radprof.canvas.fig.canvas.mpl_connect('motion_notify_event',self.motion_notify_callback)
        QObject.connect(self,SIGNAL('paint'),self.radprof.repaint)
        QObject.connect(self,SIGNAL('resize()'),self.radprof.repaint)
        QObject.connect(self,SIGNAL('closing'),main.del_detail_list_item)
        QObject.connect(self.okbutton,SIGNAL('clicked()'),self.close)
        #self.draw_canvas()
        #This thread is a hack to get the canvas to redraw properly on the first draw. futures redraws are handled by the draw_cancas itself.
        self.temp = myThread2(parent=self)
        self.temp.start()
        self.horcut.canvas.ax.plot(self.frame[maxy,:],'.')
        self.vertcut.canvas.ax.plot(self.frame[:,maxx],'.')
        self.show()
    def closeEvent(self, event):
        if self.dbbox == 0:
            self.emit(SIGNAL('closing'),self.listno)

    def limit_check(self):
        '''
        This function is used to check to make sure that the cutsize and radius and apsize is appropriate
        for the size of the frame
        '''
        if self.cutsize >= self.flimit:
            self.cutsize = self.flimit-1
        if self.radout >= self.flimit:
            self.radout = 3*self.flimit/4.
        if self.radin >= self.radout:
            self.radin = self.flimit/2.
        if self.apsize >= self.flimit:
            self.apsize = self.flimit/4.
    def dummy2(self):
        '''
        This function is just used to double check to make sure that the window redraw gets delayed
        in order to have it drawn properly
        '''
        self.radprof.canvas.ax.cla()
        self.radprof.canvas.format_labels()
        self.vis.canvas.ax.cla()
        self.vis.canvas.format_labels()
        self.draw_canvas()
    def dummy(self):
        '''
        This is the function that facillitates the posponed drawing of the plot via the separate thread.
        '''
        self.radprof.canvas.fig.canvas.mpl_connect('draw_event',self.draw_callback)
        self.radprof.canvas.ax.cla()
        self.radprof.canvas.format_labels()
        self.vis.canvas.ax.cla()
        self.vis.canvas.format_labels()
        self.draw_canvas()

    def draw_canvas(self):
        #Creating the new view based on the correct positions. This is the view the radial profile will be
        #generated from
        self.view = self.frame[self.totaly-self.cutsize:self.totaly+self.cutsize,self.totalx-self.cutsize:self.totalx+self.cutsize]
        #View 2 is view of the minimap. This is required to be separate since there may be either a maping of
        #log or linear scale
        self.view2 = self.frameedit[self.totaly-self.cutsize:self.totaly+self.cutsize,self.totalx-self.cutsize:self.totalx+self.cutsize]
        #Sow the view2 and set associated text
        self.vis.canvas.ax.imshow(self.view2,vmax=self.clipmax,vmin=self.clipmin,cmap=self.color)
        self.yin,self.xin= np.indices((self.view.shape))
        #create a distance array and create the radial profile, display this information to screen based on given
        #aperature size and anulus
        self.dist = ((self.cutsize-self.xin)**2+(self.cutsize-self.yin)**2)**0.5
        self.radprof.canvas.ax.plot(self.dist.flatten(),self.view.flatten(),'k.')
        #sum up the photons in anulus
        self.photons = np.sum(self.view[np.where(self.dist<self.apsize)])
        #get median backkground lvl
        self.bphotons = np.median(self.view[np.where(np.bitwise_and(self.dist>self.radin,self.dist<self.radout))])
        #update text and background
        self.background.setText(str(self.bphotons))
        self.photons -= len(np.where(self.dist<self.apsize))*self.bphotons
        self.counts.setText(str(self.photons))
        #Draw the interactive lines
        self.ap = self.radprof.canvas.ax.axvline(self.apsize,color="g",label="Aperture",picker=5,animated=True)
        self.rad1 = self.radprof.canvas.ax.axvline(self.radin,color="r",label="Annulus",picker=5,animated=True)
        self.rad2 = self.radprof.canvas.ax.axvline(self.radout,color="r",picker=5,animated=True)
        self.leg = self.radprof.canvas.ax.legend()
        #format and draw the canvas
        self.radprof.canvas.format_labels()
        self.radprof.canvas.draw()
        self.vis.canvas.draw()
        self.radprof.canvas.format_labels()
        #emit a paint signal to make sure the window is redrawn properly
        self.emit(SIGNAL('paint'))
    def resizeEvent(self,ev):
        if self.thread3 != None:
            self.thread3.quit()
        self.thread3 = myThread3(parent=self)
        self.thread3.start()
    def on_pic(self,event):
        '''
        This function is called when one of the vertical lines is selected, set the line selected
        to the line to be edited.
        '''
        self.artist = event

    def draw_callback(self,event):
        #grab the current state of the canvas, inorder to quickly blit the background
        self.bg = self.radprof.canvas.fig.canvas.copy_from_bbox(self.radprof.canvas.ax.bbox)
        #redraw each of the member elements during dragging.
        self.radprof.canvas.ax.draw_artist(self.ap)
        self.radprof.canvas.ax.draw_artist(self.rad1)
        self.radprof.canvas.ax.draw_artist(self.rad2)
        self.radprof.canvas.ax.draw_artist(self.leg)
        self.radprof.canvas.fig.canvas.blit(self.radprof.canvas.ax.bbox)
        #emit a paint signal to make sure the window is redrawn properly
        self.emit(SIGNAL('paint'))


    def button_release_callback(self,event):
        '''
        called when a button is released
        '''
        if self.artist != None:
            #Set the artist to none, so that mouse motion events will be turned off.
            self.artist = None
            # get the current radii for the ap and annulus inorder to redraw the figure
            self.apsize = self.ap.get_data()[0][0]
            self.radin = self.rad1.get_data()[0][0]
            self.radout = self.rad2.get_data()[0][0]
            #rescale the view size based on the current aperature size
            self.cutsize = 4*int(self.apsize)
            #check that the annulus rings are in proper orientation, ie inside the cutview, and r1 < r2
            if self.rad1.get_data()[0][0] < self.apsize or self.rad1.get_data()[0][0] > 1.5*self.cutsize:
                self.radin = 2*self.apsize
            if self.rad2.get_data()[0][0] < self.radin or self.rad2.get_data()[0][0] > 1.5*self.cutsize:
                self.radout = self.radin+self.apsize
            #clear and format the axis to prevent memory overflow
            self.radprof.canvas.ax.cla()
            self.radprof.canvas.format_labels()
            #check to make sure that new limits are w/n the image size
            self.limit_check()
            #redraw the canvas
            self.draw_canvas()

    def motion_notify_callback(self,event):
        '''
        This function gets called as the mouse moves when a line artist has been selected, it
        updates the the lines as they get dragged around
        '''
        #check to make sure there is a line selected
        if self.artist != None:
            #get the current x and y mouse positions
            x,y = event.xdata,event.ydata
            #make sure the mouse is in the canvas
            if x != None:
                #make sure you dont move past zero, as negitive radius is meaningless
                if x >0:
                    #update the position of selected artist and blit the figure. not really a full
                    #redraw
                    self.artist.artist.set_xdata([x,x])
                    self.radprof.canvas.fig.canvas.restore_region(self.bg)
                    self.radprof.canvas.ax.draw_artist(self.ap)
                    self.radprof.canvas.ax.draw_artist(self.rad1)
                    self.radprof.canvas.ax.draw_artist(self.rad2)
                    self.radprof.canvas.ax.draw_artist(self.leg)
                    self.radprof.canvas.fig.canvas.blit(self.radprof.canvas.ax.bbox)

class myThread2(QThread,details_view):
    '''
    This class is for internal use only, It simply delays the drawing of the radial profile till after the details view
    instance has been created. This solves a problem where the axes were getting blacked out and a repaint was in need to
    be forced.
    '''
    def __init__(self,parent):
        QThread.__init__(self)
        QObject.connect(self,SIGNAL('redraw'),parent.dummy)
    def run(self):
        time.sleep(0.3)
        self.emit(SIGNAL('redraw'))
        self.sleep(2)
        self.exec_()

class myThread3(QThread,details_view):
    '''
    This class is for internal use only, It simply delays the drawing of the radial profile till after the details view
    instance has been created. This solves a problem where the axes were getting blacked out and a repaint was in need to
    be forced.
    '''
    def __init__(self,parent):
        QThread.__init__(self)
        QObject.connect(self,SIGNAL('redraw'),parent.dummy2)
    def run(self):
        time.sleep(0.01)
        self.emit(SIGNAL('redraw'))
        self.sleep(2)
        self.exec_()
