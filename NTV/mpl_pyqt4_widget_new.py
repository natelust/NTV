#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

import numpy as N

class MyMplCanvas(FigureCanvas):
	def __init__(self, parent=None, width = 10, height = 12, dpi = 100, sharex = None, sharey = None):
		self.fig = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
		self.ax = self.fig.add_subplot(111, sharex = sharex, sharey = sharey)
		self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
		self.xtitle="x-Axis"
		self.ytitle="y-Axis"
		self.PlotTitle = "Some Plot"
		self.grid_status = True
		self.xaxis_style = 'linear'
		self.yaxis_style = 'linear'
		self.format_labels()
		self.ax.hold(True)
		FigureCanvas.__init__(self, self.fig)
		#self.fc = FigureCanvas(self.fig)
		FigureCanvas.setSizePolicy(self,
			QSizePolicy.Expanding,
			QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def format_labels(self):
		#self.ax.set_title(self.PlotTitle)
		#self.ax.title.set_fontsize(10)
		#self.ax.set_xlabel(self.xtitle, fontsize = 9)
		#self.ax.set_ylabel(self.ytitle, fontsize = 9)
		#labels_x = self.ax.get_xticklabels()
		#labels_y = self.ax.get_yticklabels()
		
		#for xlabel in labels_x:
		#	xlabel.set_fontsize(8)
		#for ylabel in labels_y:
	#		ylabel.set_fontsize(8)
	#		ylabel.set_color('b')
		self.ax.axis('off')
		#self.ax.axis['top'].set_visible(False)
		#self.ax.axis['bottom'].set_visible(False)
		#self.ax.axis['left'].set_visible(False)
	#	pass
	def sizeHint(self):
		w, h = self.get_width_height()
		return QSize(w, h)

	def minimumSizeHint(self):
		return QSize(10, 10)

	def sizeHint(self):
		w, h = self.get_width_height()
		return QSize(w, h)

	def minimumSizeHint(self):
		return QSize(10, 10)


class MPL_Widget1(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MyMplCanvas()
        #self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        #self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)

