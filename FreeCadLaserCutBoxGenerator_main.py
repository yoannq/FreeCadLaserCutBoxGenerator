# -*- coding: utf-8 -*-

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>. 1
'''
__author__ = "yoann quere"
__license__ = "GPL"
__version__ = "3"
__email__ = "ioanker295@gmail.com"
__status__ = "beta"


from FreeCAD import Base
import Draft, Part
import numpy as np
from PySide import QtCore, QtGui
import sys

def generate_points_for_xaxis(x,y,point_mat,material_thickness,number,step,male=True):
	if male:
		sign=1
	else :
		sign=-1
	for i in range(np.int(number)):
		point_mat.append([x,y])
		x=x+step
		point_mat.append([x,y])

		if i%2 == 1:
			y=y+sign*material_thickness
		else :
			y=y-1*sign*material_thickness
	return point_mat
def generate_points_for_yaxis(x,y,point_mat,material_thickness,number,step,male=True):
	if male:
		sign=1
	else :
		sign=-1
	for i in range(np.int(number)):

		point_mat.append([x,y])
		y=y+step
		point_mat.append([x,y])
		if i%2 == 1:
			x=x-1*sign*material_thickness
		else :
			x=x+sign*material_thickness
	return point_mat



class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
		Dialog.resize(519, 451)
		self.layoutWidget = QtGui.QWidget(Dialog)
		self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 442))
		self.layoutWidget.setObjectName("layoutWidget")
		self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_8 = QtGui.QLabel(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(16)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.verticalLayout.addWidget(self.label_8)
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setSpacing(20)
		self.gridLayout.setObjectName("gridLayout")
		self.thicknesspinBox = QtGui.QSpinBox(self.layoutWidget)
		self.thicknesspinBox.setMinimum(1)
		self.thicknesspinBox.setMaximum(15)
		self.thicknesspinBox.setProperty("value", 3)
		self.thicknesspinBox.setObjectName("thicknesspinBox")
		self.gridLayout.addWidget(self.thicknesspinBox, 9, 2, 1, 1)
		self.thicknessSlider = QtGui.QSlider(self.layoutWidget)
		self.thicknessSlider.setInputMethodHints(QtCore.Qt.ImhNone)
		self.thicknessSlider.setMinimum(1)
		self.thicknessSlider.setMaximum(15)
		self.thicknessSlider.setProperty("value", 3)
		self.thicknessSlider.setOrientation(QtCore.Qt.Horizontal)
		self.thicknessSlider.setInvertedAppearance(False)
		self.thicknessSlider.setInvertedControls(False)
		self.thicknessSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.thicknessSlider.setObjectName("thicknessSlider")
		self.gridLayout.addWidget(self.thicknessSlider, 9, 1, 1, 1)
		self.label_2 = QtGui.QLabel(self.layoutWidget)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
		self.label_3 = QtGui.QLabel(self.layoutWidget)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
		self.widthSlider = QtGui.QSlider(self.layoutWidget)
		self.widthSlider.setMinimum(10)
		self.widthSlider.setMaximum(1000)
		self.widthSlider.setSliderPosition(30)
		self.widthSlider.setOrientation(QtCore.Qt.Horizontal)
		self.widthSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.widthSlider.setObjectName("widthSlider")
		self.gridLayout.addWidget(self.widthSlider, 0, 1, 1, 1)
		self.heightspinBox = QtGui.QSpinBox(self.layoutWidget)
		self.heightspinBox.setMinimum(10)
		self.heightspinBox.setMaximum(1000)
		self.heightspinBox.setProperty("value", 30)
		self.heightspinBox.setObjectName("heightspinBox")
		self.gridLayout.addWidget(self.heightspinBox, 3, 2, 1, 1)
		self.depthspinBox = QtGui.QSpinBox(self.layoutWidget)
		self.depthspinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
		self.depthspinBox.setMinimum(10)
		self.depthspinBox.setMaximum(1000)
		self.depthspinBox.setProperty("value", 35)
		self.depthspinBox.setObjectName("depthspinBox")
		self.gridLayout.addWidget(self.depthspinBox, 6, 2, 1, 1)
		self.depthSlider = QtGui.QSlider(self.layoutWidget)
		self.depthSlider.setMinimum(10)
		self.depthSlider.setMaximum(1000)
		self.depthSlider.setProperty("value", 35)
		self.depthSlider.setOrientation(QtCore.Qt.Horizontal)
		self.depthSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.depthSlider.setObjectName("depthSlider")
		self.gridLayout.addWidget(self.depthSlider, 6, 1, 1, 1)
		self.widthspinBox = QtGui.QSpinBox(self.layoutWidget)
		self.widthspinBox.setReadOnly(False)
		self.widthspinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
		self.widthspinBox.setMinimum(10)
		self.widthspinBox.setMaximum(1000)
		self.widthspinBox.setProperty("value", 30)
		self.widthspinBox.setObjectName("widthspinBox")
		self.gridLayout.addWidget(self.widthspinBox, 0, 2, 1, 1)
		self.label_7 = QtGui.QLabel(self.layoutWidget)
		self.label_7.setObjectName("label_7")
		self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
		self.heightSlider = QtGui.QSlider(self.layoutWidget)
		self.heightSlider.setMinimum(10)
		self.heightSlider.setMaximum(1000)
		self.heightSlider.setSliderPosition(30)
		self.heightSlider.setOrientation(QtCore.Qt.Horizontal)
		self.heightSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.heightSlider.setObjectName("heightSlider")
		self.gridLayout.addWidget(self.heightSlider, 3, 1, 1, 1)
		self.label = QtGui.QLabel(self.layoutWidget)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.line = QtGui.QFrame(self.layoutWidget)
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName("line")
		self.gridLayout.addWidget(self.line, 8, 0, 1, 1)
		self.line_3 = QtGui.QFrame(self.layoutWidget)
		self.line_3.setFrameShape(QtGui.QFrame.HLine)
		self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.gridLayout.addWidget(self.line_3, 8, 2, 1, 1)
		self.line_2 = QtGui.QFrame(self.layoutWidget)
		self.line_2.setFrameShape(QtGui.QFrame.HLine)
		self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.gridLayout.addWidget(self.line_2, 8, 1, 1, 1)
		self.heightTab = QtGui.QSpinBox(self.layoutWidget)
		self.heightTab.setFrame(True)
		self.heightTab.setReadOnly(True)
		self.heightTab.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
		self.heightTab.setMinimum(3)
		self.heightTab.setSingleStep(2)
		self.heightTab.setProperty("value", 3)
		self.heightTab.setObjectName("heightTab")
		self.gridLayout.addWidget(self.heightTab, 4, 2, 1, 1)
		self.depthTab = QtGui.QSpinBox(self.layoutWidget)
		self.depthTab.setEnabled(True)
		self.depthTab.setReadOnly(True)
		self.depthTab.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
		self.depthTab.setMinimum(3)
		self.depthTab.setSingleStep(2)
		self.depthTab.setProperty("value", 3)
		self.depthTab.setObjectName("depthTab")
		self.gridLayout.addWidget(self.depthTab, 7, 2, 1, 1)
		self.widthTab = QtGui.QSpinBox(self.layoutWidget)
		self.widthTab.setReadOnly(True)
		self.widthTab.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
		self.widthTab.setMinimum(3)
		self.widthTab.setSingleStep(2)
		self.widthTab.setProperty("value", 3)
		self.widthTab.setObjectName("widthTab")
		self.gridLayout.addWidget(self.widthTab, 1, 2, 1, 1)
		self.line_4 = QtGui.QFrame(self.layoutWidget)
		self.line_4.setFrameShape(QtGui.QFrame.HLine)
		self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.gridLayout.addWidget(self.line_4, 5, 0, 1, 1)
		self.line_5 = QtGui.QFrame(self.layoutWidget)
		self.line_5.setFrameShape(QtGui.QFrame.HLine)
		self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.gridLayout.addWidget(self.line_5, 5, 1, 1, 1)
		self.line_6 = QtGui.QFrame(self.layoutWidget)
		self.line_6.setFrameShape(QtGui.QFrame.HLine)
		self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.gridLayout.addWidget(self.line_6, 5, 2, 1, 1)
		self.line_7 = QtGui.QFrame(self.layoutWidget)
		self.line_7.setFrameShape(QtGui.QFrame.HLine)
		self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.gridLayout.addWidget(self.line_7, 2, 0, 1, 1)
		self.line_8 = QtGui.QFrame(self.layoutWidget)
		self.line_8.setFrameShape(QtGui.QFrame.HLine)
		self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.gridLayout.addWidget(self.line_8, 2, 1, 1, 1)
		self.line_9 = QtGui.QFrame(self.layoutWidget)
		self.line_9.setFrameShape(QtGui.QFrame.HLine)
		self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.gridLayout.addWidget(self.line_9, 2, 2, 1, 1)
		self.label_6 = QtGui.QLabel(self.layoutWidget)
		self.label_6.setObjectName("label_6")
		self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
		self.label_5 = QtGui.QLabel(self.layoutWidget)
		self.label_5.setObjectName("label_5")
		self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
		self.label_4 = QtGui.QLabel(self.layoutWidget)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
		self.widthTabSlider = QtGui.QSlider(self.layoutWidget)
		self.widthTabSlider.setMinimum(3)
		self.widthTabSlider.setSingleStep(2)
		self.widthTabSlider.setOrientation(QtCore.Qt.Horizontal)
		self.widthTabSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.widthTabSlider.setObjectName("widthTabSlider")
		self.gridLayout.addWidget(self.widthTabSlider, 1, 1, 1, 1)
		self.heightTabSlider = QtGui.QSlider(self.layoutWidget)
		self.heightTabSlider.setMinimum(3)
		self.heightTabSlider.setSingleStep(2)
		self.heightTabSlider.setOrientation(QtCore.Qt.Horizontal)
		self.heightTabSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.heightTabSlider.setObjectName("heightTabSlider")
		self.gridLayout.addWidget(self.heightTabSlider, 4, 1, 1, 1)
		self.depthTabSlider = QtGui.QSlider(self.layoutWidget)
		self.depthTabSlider.setMinimum(3)
		self.depthTabSlider.setSingleStep(2)
		self.depthTabSlider.setOrientation(QtCore.Qt.Horizontal)
		self.depthTabSlider.setTickPosition(QtGui.QSlider.TicksAbove)
		self.depthTabSlider.setObjectName("depthTabSlider")
		self.gridLayout.addWidget(self.depthTabSlider, 7, 1, 1, 1)
		self.verticalLayout.addLayout(self.gridLayout)
		self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.okclicked)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.cancelclicked)
		#		self.widthSlider.valueChanged[int].connect(self.valueChanged(self.widthSlider.value))



		## permet de coupler les sliders aux spinbox et vice et versa
		self.widthSlider.valueChanged[int].connect(self.widthspinBox.setValue)
		self.heightSlider.valueChanged[int].connect(self.heightspinBox.setValue)
		self.depthSlider.valueChanged[int].connect(self.depthspinBox.setValue)
		self.thicknessSlider.valueChanged[int].connect(self.thicknesspinBox.setValue)
		self.widthspinBox.valueChanged[int].connect(self.widthSlider.setValue)
		self.heightspinBox.valueChanged[int].connect(self.heightSlider.setValue)
		self.depthspinBox.valueChanged[int].connect(self.depthSlider.setValue)
		self.thicknesspinBox.valueChanged[int].connect(self.thicknessSlider.setValue)

		self.widthTabSlider.valueChanged[int].connect(self.widthTab.setValue) 	
		self.heightTabSlider.valueChanged[int].connect(self.heightTab.setValue) 	
		self.depthTabSlider.valueChanged[int].connect(self.depthTab.setValue) 	
		
		QtCore.QMetaObject.connectSlotsByName(Dialog)




	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.label_8.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p align=\"center\">FreeCad Laser cut box generator</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("Dialog", "Height", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("Dialog", "Depth", None, QtGui.QApplication.UnicodeUTF8))
		self.label_7.setText(QtGui.QApplication.translate("Dialog", "Material thickness", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Width", None, QtGui.QApplication.UnicodeUTF8))
		self.label_6.setText(QtGui.QApplication.translate("Dialog", "Depth Tab number", None, QtGui.QApplication.UnicodeUTF8))
		self.label_5.setText(QtGui.QApplication.translate("Dialog", "Height Tab number", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate("Dialog", "Width Tab number", None, QtGui.QApplication.UnicodeUTF8))


	def okclicked(self):
		print "okclicked"
		d.hide()	
		width =int(self.widthspinBox.value())
		depth =int(self.depthspinBox.value())
		height =int(self.heightspinBox.value())
		material_thickness = int(self.thicknesspinBox.value())
		numberW = float(self.widthTab.value())
		if (numberW%2)==0:
			numberW = numberW+1.0	
			
		numberD = float(self.depthTab.value())
		if (numberD%2)==0:
			numberD = numberD+1.0	
			
		numberH = float(self.heightTab.value())
		if (numberH%2)==0:
			numberH = numberH+1.0	
		
		height=height+material_thickness*2
		#nombre de segment 
		step_width= width/(numberW)
		step_depth= depth/(numberD)
		step_height = height/(numberH)
		
		
		# capot et base
		liste_de_point=[]
		A=[0,0]
		B=[width,0]
		C=[width,depth]
		D=[0,depth]
		x,y=A[0],A[1]
		liste_de_point = generate_points_for_xaxis(x,y,liste_de_point,material_thickness,numberW,step_width,male=True)
		x,y=B[0],B[1]
		liste_de_point = generate_points_for_yaxis(x,y,liste_de_point,material_thickness,numberD,step_depth,male=True)
		x,y=C[0],C[1]
		liste_de_point = generate_points_for_xaxis(x,y,liste_de_point,material_thickness,numberW,-1*step_width,male=False)
		x,y=D[0],D[1]
		liste_de_point = generate_points_for_yaxis(x,y,liste_de_point,material_thickness,numberD,-1*step_depth,male=False)
		
		wire=[]
		for point in liste_de_point:
			X,Y,Z = point[0], point[1],0  
			wire.append(FreeCAD.Vector(float(X),float(Y),float(Z)))
		
		objet=Draft.makeWire(wire,closed=False,face=False,support=None)   # create the wire open
		#Draft.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)
		objet.Label="part001"
		objet2 = FreeCAD.ActiveDocument.getObjectsByLabel("part001")
		objet_copy=Draft.makeCopy(objet)
		objet_copy.Placement=Placement = App.Placement(App.Vector(0,(height+depth),0),App.Rotation(App.Vector(0,0,1),0))
		
		
		# cote1
		liste_de_point=[]
		A=[0,0]
		B=[width,0]
		C=[width,height]
		D=[0,height]
		
		
		x,y=A[0],A[1]
		liste_de_point = generate_points_for_xaxis(x,y,liste_de_point,material_thickness,numberW,step_width,male=False)
		
		x,y=B[0],B[1]
		liste_de_point = generate_points_for_yaxis(x,y,liste_de_point,material_thickness,numberH,step_height,male=True)
		
		x,y=C[0],C[1]
		liste_de_point = generate_points_for_xaxis(x,y,liste_de_point,material_thickness,numberW,-1*step_width,male=True)
		
		x,y=D[0],D[1]
		liste_de_point = generate_points_for_yaxis(x,y,liste_de_point,material_thickness,numberH,-1*step_height,male=False)
		
		wire=[]
		for point in liste_de_point:
			X,Y,Z = point[0], point[1],0  
			wire.append(FreeCAD.Vector(float(X),float(Y),float(Z)))
		
		objet=Draft.makeWire(wire,closed=False,placement=None,face=False,support=None)   # create the wire open
		#Draft.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)
		objet.Label="part003"
		objet.Placement=Placement = App.Placement(App.Vector(0,-height,0),App.Rotation(App.Vector(0,0,1),0))
		objet_copy=Draft.makeCopy(objet)
		objet_copy.Placement=Placement = App.Placement(App.Vector(0,(depth),0),App.Rotation(App.Vector(0,0,1),0))
		
		
		
		# cote2
		liste_de_point=[]
		A=[0,0]
		B=[height,0]
		C=[height,depth]
		D=[0,depth]
		
		
		
		# cote majore de 3mm
		liste_de_point.append([A[0],A[1]])
		x,y=A[0],A[1]-material_thickness
		liste_de_point = generate_points_for_xaxis(x,y,liste_de_point,material_thickness,numberH,step_height,male=False)
		
		x,y=B[0],B[1]
		liste_de_point = generate_points_for_yaxis(x,y,liste_de_point,material_thickness,numberD,step_depth,male=False)
		
		x,y=C[0],C[1]+material_thickness
		liste_de_point = generate_points_for_xaxis(x,y,liste_de_point,material_thickness,numberH,-1*step_height,male=True)
		
		x,y=D[0],D[1]
		liste_de_point = generate_points_for_yaxis(x,y,liste_de_point,material_thickness,numberD,-1*step_depth,male=True)
		
		wire=[]
		for point in liste_de_point:
			X,Y,Z = point[0], point[1],0  
			wire.append(FreeCAD.Vector(float(X),float(Y),float(Z)))
		
		objet=Draft.makeWire(wire,closed=False,placement=None,face=False,support=None)   # create the wire open
		#Draft.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)
		objet.Label="part005"
		objet.Placement=Placement = App.Placement(App.Vector(-height,0,0),App.Rotation(App.Vector(0,0,1),0))
		objet_copy=Draft.makeCopy(objet)
		objet_copy.Placement=Placement = App.Placement(App.Vector(width,0,0),App.Rotation(App.Vector(0,0,1),0))

	
	def cancelclicked(self):
		print "cancelclicked"
		d.hide()	


d = QtGui.QWidget()
d.ui = Ui_Dialog()
d.ui.setupUi(d)
d.show()	