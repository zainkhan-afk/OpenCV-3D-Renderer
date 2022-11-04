from shape import Shape
from line import Line
from rectangle import Rectangle
from scene import Scene
from joint import Joint
import numpy as np

class Quadruped(Shape):
	def __init__(self, x = 0, y = 0, z = 0,
					   x_rot = 0, y_rot = 0, 
					   z_rot = 0):
		Shape.__init__(self, x, y, z, x_rot, y_rot, z_rot)

		self.name = "QUADRUPED"

		self.body = Rectangle(x=0, y=0, z=3, w=2, l=1)
		
		self.fr_hip  = Line(x = 0, y = -2, z = 0)
		self.fr_knee = Line(x = 0, y = -2, z = 0)
		self.fr_calf = Line(x = 0, y = -2, z = 0)
