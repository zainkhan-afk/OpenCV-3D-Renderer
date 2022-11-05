from ..shapes.shape import Shape
import numpy as np

class Sphere(Shape):
	def __init__(self, x = 0, y = 0, z = 0, 
					   x_rot = 0, y_rot = 0, 
					   z_rot = 0, radius = 1,
					   resolution = 20, color = (0, 0, 0), thickness = 1):
		Shape.__init__(self, x, y, z, x_rot, y_rot, z_rot)
		self.radius = radius
		self.name = "SPHERE"
		self.resolution = resolution

		self.color = color
		self.thickness = thickness

		self.shape_points = []

		for i in range(0, 360, self.resolution):
			for j in range(0, 360, self.resolution):
				x = self.radius*np.cos(i*np.pi/180)*np.sin(j*np.pi/180)
				y = self.radius*np.sin(i*np.pi/180)*np.sin(j*np.pi/180)
				z = self.radius*np.cos(j*np.pi/180)
				self.shape_points.append([x, y, z])

		self.shape_points = np.array(self.shape_points)


		self.shape_points_homogeneous = np.append(self.shape_points, np.ones((len(self.shape_points), 1)), axis=1)