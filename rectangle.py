from shape import Shape
import numpy as np

class Rectangle(Shape):
	def __init__(self, x = 0, y = 0, z = 0, 
					   w = 1, l = 1, x_rot = 0, 
					   y_rot = 0, z_rot = 0):
		Shape.__init__(self, x, y, z, x_rot, y_rot, z_rot)

		self.w = w
		self.l = l
		self.name = "RECTANGLE"

		self.shape_points = np.array([
										[ -self.w/2, -self.l/2, 0],
										[ self.w/2,  -self.l/2, 0],
										[ self.w/2,  self.l/2,  0],
										[-self.w/2,  self.l/2,  0],
									])

		self.shape_points_homogeneous = np.append(self.shape_points, np.ones((len(self.shape_points), 1)), axis=1)

	def set_scale(self, w, h, l):
		self.w = w
		self.l = l

		self.shape_points = np.array([
										[ -self.w/2, 0, -self.l/2],
										[ self.w/2, 0,  -self.l/2],
										[ self.w/2, 0,  self.l/2],
										[-self.w/2, 0,  self.l/2],
									])

		self.shape_points_homogeneous = np.append(self.shape_points, np.ones((len(self.shape_points), 1)), axis=1)
