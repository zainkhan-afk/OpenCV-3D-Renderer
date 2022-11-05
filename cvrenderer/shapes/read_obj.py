from cvrenderer.shapes.shape import Shape
import numpy as np

class ReadObj(Shape):
	def __init__(self, filename, x = 0, 
					   y = 0, z = 0, x_rot = 0, 
					   y_rot = 0, z_rot = 0, scale = 1, color = (0, 0, 0), thickness = 1):
		Shape.__init__(self, x, y, z, x_rot, y_rot, z_rot)

		self.scale = scale
		self.name = "3D File"
		self.filename = filename

		self.color = color
		self.thickness = thickness

		f = open(self.filename, "r")
		all_dala = f.readlines()
		f.close()

		self.shape_points = []
		for line in all_dala:
			line = line.replace("\n", "")
			line = line.split(" ")

			if line[0] == "v":
				self.shape_points.append([float(line[1]), float(line[2]), float(line[3])])

			if len(self.shape_points) > 0 and line[0] != "v":
				break

		self.shape_points = np.array(self.shape_points)
		
		MIN = self.shape_points.min()
		MAX = self.shape_points.max()

		self.shape_points = (MAX - self.shape_points)/(MAX - MIN)*self.scale
		
		# self.shape_points[:,0] = self.shape_points[:,0] + self.shape_points[:,0].min()
		# print(self.shape_points[:,0].min(), self.shape_points[:,1].min(), self.shape_points[:,2].min())
		# print(self.shape_points[:,0].max(), self.shape_points[:,1].max(), self.shape_points[:,2].max())
		# self.shape_points = np.array([
		# 								[-self.scale/2, -self.scale/2, -self.scale/2],
		# 								[ self.scale/2, -self.scale/2, -self.scale/2],
		# 								[ self.scale/2,  self.scale/2, -self.scale/2],
		# 								[-self.scale/2,  self.scale/2, -self.scale/2],

		# 								[-self.scale/2, -self.scale/2,  self.scale/2],
		# 								[ self.scale/2, -self.scale/2,  self.scale/2],
		# 								[ self.scale/2,  self.scale/2,  self.scale/2],
		# 								[-self.scale/2,  self.scale/2,  self.scale/2]
		# 							])

		self.shape_points_homogeneous = np.append(self.shape_points, np.ones((len(self.shape_points), 1)), axis=1)
