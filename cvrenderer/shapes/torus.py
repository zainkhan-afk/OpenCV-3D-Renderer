from ..shapes.shape import Shape
import numpy as np

class Torus(Shape):
	def __init__(self, x = 0, y = 0, z = 0, 
					   x_rot = 0, y_rot = 0, 
					   z_rot = 0, radius1 = 1,
					   radius2 = 0.5, resolution = 20, color = (0, 0, 0), thickness = 1):
		Shape.__init__(self, x, y, z, x_rot, y_rot, z_rot)
		self.radius1 = radius1
		self.radius2 = radius2
		self.name = "TORUS"
		self.resolution = resolution

		self.color = color
		self.thickness = thickness

		self.shape_points = []

		for i in range(0, 360, self.resolution):
			R = np.array([
							[np.cos(i*np.pi/180), -np.sin(i*np.pi/180), 0],
							[np.sin(i*np.pi/180),  np.cos(i*np.pi/180), 0],
							[				   0,					 0, 1]
				])
			for j in range(0, 360, self.resolution):
				x = self.radius1 + self.radius2*np.cos(j*np.pi/180)
				y = 0
				z = self.radius2*np.sin(j*np.pi/180)
				temp = np.array([[x, y, z]])
				temp = R@temp.T
				x, y, z = temp[0, 0], temp[1, 0], temp[2, 0]
				self.shape_points.append([x, y, z])

		self.shape_points = np.array(self.shape_points)


		self.shape_points_homogeneous = np.append(self.shape_points, np.ones((len(self.shape_points), 1)), axis=1)