#!usr/bin/env python

import sys;
import os;
import time;

#Import the OpenGL instances
from OpenGL.GL import *;
from OpenGL.GLU import *;
from OpenGL.GLUT import *;

#FILENAME: ThermafieldGraphicsMod.py

#Copy this file to: /usr/lib/pymodules/python2.7

#Introduce the global variables

render_x_coor_global = [];
render_y_coor_global = [];
render_data_dx_global = [];
render_data_dy_global = [];	

def openGLRenderingPlotting():
#The actual plotting function

	counter = 0;
	
	#Set the BG colour
	glClearColor(1.0,1.0,1.0,1.0);
	
	#Clearing the screen buffer
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0,0.0,0.0); #plotting colour

	glBegin(GL_LINES);

	#Plot the lines representing the displacements
	while (counter < globalNodeMeshCounter_global - 10):

		dx_coor = (render_x_coor_global[counter]-2.5)/5.0;
		dy_coor = (render_y_coor_global[counter]-2.5)/5.0;
		
		ddx_coor = dx_coor + render_data_dx_global[counter];
		ddy_coor = dy_coor + render_data_dy_global[counter];

		print "NOPEEE {0} {1} {2} {3}".format(dx_coor, dy_coor, ddx_coor, ddy_coor);

		glVertex2f(dx_coor, dy_coor);
		glVertex2f(ddx_coor, ddy_coor);
		
		counter += 1;
	
	glEnd();

	glFlush();

	time.sleep(5);

	glutLeaveMainLoop();
	
def openGLRendering(render_x_coor, render_y_coor, render_z_coor, render_data_dx, render_data_dy, render_data_dz, globalNodeMeshCounter):
	#This function will plot the displacement of the structure as a series of arrows with the help of openGL
	#Create temporary global variable for use in the rendering function
	
	global render_x_coor_global, render_y_coor_global, render_data_dx_global, render_data_dy_global, globalNodeMeshCounter_global;	

	counter = 0;
	
	while (counter < globalNodeMeshCounter - 10):

		render_x_coor_global.append(float(render_x_coor[counter]));
		render_y_coor_global.append(float(render_y_coor[counter]));
		render_data_dx_global.append(float(render_data_dx[counter]));
		render_data_dy_global.append(float(render_data_dy[counter]));
		
		counter += 1;

	globalNodeMeshCounter_global = globalNodeMeshCounter;

	glutInit(sys.argv);
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowSize(500,500);
	glutInitWindowPosition(50,50);
	glutCreateWindow("Displacement values for the experimental model");
	glutDisplayFunc(openGLRenderingPlotting);
	
	counter = 0;

	glutMainLoop();	
