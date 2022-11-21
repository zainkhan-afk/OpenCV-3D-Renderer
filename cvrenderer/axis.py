from .shapes.line import Line
import numpy as np
from .utils import *

class Axis:
	def __init__(self, size = 25, scaler = 1):
		self.size = size
		self.scaler = scaler
		self.name = "SceneCursor"

		self.lines = []

		x = Line(y_rot = np.pi/2, length = self.size*self.scaler, color = (0, 0, 255))
		y = Line(x_rot = np.pi/2, length = self.size*self.scaler, color = (0, 255, 0))

		self.lines.append(x)
		self.lines.append(y)

		for i in range(-self.size//2+1, self.size//2+1):
			if i == 0:
				continue
			l = Line(y = i*self.scaler, y_rot = np.pi/2, length = self.size*self.scaler, color = (0, 0, 0))
			self.lines.append(l)
			l = Line(x = i*self.scaler, x_rot = np.pi/2, length = self.size*self.scaler, color = (0, 0, 0))
			self.lines.append(l)

	def translate_axis(self, delta_x = 0, delta_y = 0):
		if delta_x != 0:
			for i in range(1, len(self.lines), 2):
				l = self.lines[i]
				l.translate(x = l.x+delta_x, y = 0, z = 0)

				if l.x>self.size//2*self.scaler:
					l.translate(x=-self.size//2*self.scaler, y = 0, z = 0)

				if l.x<-self.size//2*self.scaler:
					l.translate(x=self.size//2*self.scaler, y = 0, z = 0)

		if delta_y != 0:
			for i in range(0, len(self.lines), 2):
				l = self.lines[i]
				l.translate(y = l.y+delta_y, x = 0, z = 0)

				if l.y>self.size//2*self.scaler:
					l.translate(y=-self.size//2*self.scaler, x = 0, z = 0)

				if l.y<-self.size//2*self.scaler:
					l.translate(y=self.size//2*self.scaler, x = 0, z = 0)