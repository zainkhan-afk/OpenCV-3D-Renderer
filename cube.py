from shape import Shape
import numpy as np

class Cube(Shape):
	def __init__(self, x = 0, y = 0, z = 0, x_rot = 0, y_rot = 0, z_rot = 0, scale = 1):
		Shape.__init__(self, x, y, z, x_rot, y_rot, z_rot)

		self.scale = scale

		self.cube_points = np.array([
										[-self.scale, -self.scale, -self.scale],
										[ self.scale, -self.scale, -self.scale],
										[ self.scale,  self.scale, -self.scale],
										[-self.scale,  self.scale, -self.scale],

										[-self.scale, -self.scale,  self.scale],
										[ self.scale, -self.scale,  self.scale],
										[ self.scale,  self.scale,  self.scale],
										[-self.scale,  self.scale,  self.scale]
									])

		self.cube_points_homogeneous = np.append(self.cube_points, np.ones((len(self.cube_points), 1)), axis=1)


	def get_points(self):
		M = self.get_transformation_matrix()
		pts = M@self.cube_points_homogeneous.T
		return pts