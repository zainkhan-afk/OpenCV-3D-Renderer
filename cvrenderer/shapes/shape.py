import numpy as np
from utils import *

class Shape:
	def __init__(self, x = 0, y = 0, z = 0, x_rot = 0, y_rot = 0, z_rot = 0):
		self.x = x
		self.y = y
		self.z = z

		self.x_rot = x_rot
		self.y_rot = y_rot
		self.z_rot = z_rot

		self.rotate(self.x_rot, self.y_rot, self.z_rot)
		self.translate(self.x, self.y, self.z)

		self.calculate_transformation_matrix()

	def rotate(self, x_rot, y_rot, z_rot):
		self.x_rot = x_rot
		self.y_rot = y_rot
		self.z_rot = z_rot
		self.R = get_rotation_matrix(x_rot, y_rot, z_rot)

	def translate(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.T = np.array([
			[self.x],
			[self.y],
			[self.z]
			])

	def calculate_transformation_matrix(self):
		self.M = np.append(self.R, self.T, axis = 1)
		self.M = np.append(self.M, np.array([[0, 0, 0, 1]]), axis = 0)

	def get_transformation_matrix(self):
		return self.M

	def set_transformation_matrix(self, M):
		self.R = M[0:3, 0:3]
		self.T = M[:-1, -1][:, np.newaxis]
		self.M = M

	def get_points(self):
		self.calculate_transformation_matrix()
		pts = self.M@self.shape_points_homogeneous.T
		return pts