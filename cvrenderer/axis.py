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