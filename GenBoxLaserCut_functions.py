# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals
from FreeCAD import Base
import Draft, Part
import numpy as np
from PySide import QtGui, QtCore




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



width = 180
depth = 80
height = 40
material_thickness = 3
height=height+material_thickness*2
#nombre de segment 
numberW=13.0
numberD=7.0
numberH=5.0


reply = QtGui.QInputDialog.getText(None, "Init","enter the width of the box")
if reply[1]:
        # user clicked OK
        width = int(reply[0])
else:
        # user clicked Cancel
        replyText = reply[0] # which will be "" if they clicked Cancel
reply = QtGui.QInputDialog.getText(None, "Init","enter the depth of the box")
if reply[1]:
        # user clicked OK
        depth = int(reply[0])
else:
        # user clicked Cancel
        replyText = reply[0] # which will be "" if they clicked Cancel
reply = QtGui.QInputDialog.getText(None, "Init","enter the height of the box")
if reply[1]:
        # user clicked OK
        height = int(reply[0])
else:
        # user clicked Cancel
        replyText = reply[0] # which will be "" if they clicked Cancel
unit = "mm"





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
