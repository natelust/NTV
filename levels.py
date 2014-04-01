try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
import numpy as np
import time


class line_item(QGraphicsLineItem):
    def __init__(self,main,start):
        QGraphicsLineItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.main = main
        self.start = start
        self.wd = self.main.widget_size.width()

    def checkvalue(self,x):
        if self.main.blackline != self:
            if x < (self.main.blackline.scenePos().x()+\
                    self.main.blackline.start)-self.start:
                x = (self.main.blackline.scenePos().x()+\
                    self.main.blackline.start)-self.start
        if self.main.whiteline != self:
            if x > (self.main.whiteline.scenePos().x()+\
                    self.main.whiteline.start)-self.start:
                x = (self.main.whiteline.scenePos().x()+\
                     self.main.whiteline.start)-self.start
        if x > self.wd-self.start:
            x = self.wd-self.start
        if x < (0-self.start):
            x = 0 - self.start
        return x

    def itemChange(self,change,value):
        if change == QGraphicsItem.ItemPositionChange:
            x = self.checkvalue(value.toPoint().x())
            return QPointF(x,0)
        return QGraphicsLineItem.itemChange(self,change,value)

    def mouseReleaseEvent(self,event):
        self.main.update_main()


class myView(QGraphicsView):
    def __init__(self,rect):
        QGraphicsView.__init__(self)
        self.rect = rect
    def resizeEvent(self,event):
        self.fitInView(self.rect)



class levels(QWidget):
    def __init__(self,main,parent=None):
        QWidget.__init__(self,parent=parent)
        self.main = main
        self.vbox   = QVBoxLayout()
        self.widget_size = QRectF(0,0,600,600)
        self.hist_view = myView(self.widget_size)
        self.hist_scene = QGraphicsScene()
        self.hist_scene.setBackgroundBrush(QColor(210,231,236))
        self.hist_scene.setSceneRect(self.widget_size)
        self.hist_view.setScene(self.hist_scene)
        self.hist_view.setMaximumHeight(300)
        self.hist_view.setMinimumWidth(300)

        self.vbox.addWidget(self.hist_view)
        self.setLayout(self.vbox)
        self.resize(400,400)
        self.show()
        self.draw_hist()
        self.draw_lines()
        self.hist_view.fitInView(self.widget_size)
        QObject.connect(main,SIGNAL('update_main_canvas'),self.render_scene)

    def render_scene(self):
        self.hist_scene.clear()
        self.draw_hist()
        self.draw_lines()


    def draw_hist(self):
        heights,bins = np.histogram(self.main.imageedit.flat,bins=100)
        width = self.widget_size.width()/100.
        heights = heights.astype('float')
        heights[heights != 0] = np.log10(heights[heights !=0 ])
        heights /= heights.max()
        for i in range(len(bins)-1):
            self.hist_scene.addRect(i*width,self.widget_size.height(),width,\
                                    -1*heights[i]*self.widget_size.height(),
                                    brush=QBrush(QColor(23,108,179)),
                                    pen=QPen(QColor(23,108,179)))
        self.hist_scene.update()

    def get_pos(self,line):
        x = line.scenePos().x()+line.start
        scaled_pos = x/self.widget_size.width()
        scaled_pos *= (self.main.imageedit.max()-self.main.imageedit.min())
        scaled_pos += self.main.imageedit.min()
        if line == self.whiteline:
            self.main.white = scaled_pos
        if line == self.blackline:
            self.main.black = scaled_pos


    def draw_lines(self):
        where_black = (self.main.black-self.main.imageedit.min())/\
                      (self.main.imageedit.max()-self.main.imageedit.min())
        where_black *= (self.widget_size.width())
        self.blk = QLineF(QPointF(where_black,-1*self.widget_size.height()),\
                   QPointF(where_black,self.widget_size.height()))
        self.blackline = line_item(self,where_black)
        self.blackline.setLine(self.blk)
        self.blackline.setPen(QPen(QColor(0,0,0),self.widget_size.width()/100.))
        self.hist_scene.addItem(self.blackline)


        where_white = (self.main.white-self.main.imageedit.min())/\
                      (self.main.imageedit.max()-self.main.imageedit.min())
        where_white *= self.widget_size.width()
        self.wht = QLineF(QPointF(where_white,-1*self.widget_size.height()),\
                   QPointF(where_white,self.widget_size.height()))
        self.whiteline = line_item(self,where_white)
        self.whiteline.setLine(self.wht)
        self.whiteline.setPen(QPen(QColor('gray'),self.widget_size.width()/100.))
        self.hist_scene.addItem(self.whiteline)

    def update_main(self):
        self.get_pos(self.blackline)
        self.get_pos(self.whiteline)
        self.main.update_canvas()





