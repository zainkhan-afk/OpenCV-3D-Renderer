import numpy as np

class Shape:
	def __init__(self, x = 0, y = 0, z = 0, x_rot = 0, y_rot = 0, z_rot = 0):
		self.x = x
		self.y = y
		self.z = z

		self.x_rot = x_rot
		self.y_rot = y_rot
		self.z_rot = z_rot

	def rotate(self, x_rot, y_rot, z_rot):
		self.x_rot = x_rot
		self.y_rot = y_rot
		self.z_rot = z_rot

	def translate(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def get_transformation_matrix(self):
		R_x = np.array([
			[1, 			0, 				0],
			[0, np.cos(self.x_rot), -np.sin(self.x_rot)],
			[0, np.sin(self.x_rot), 	np.cos(self.x_rot)]
							])
		R_y = np.array([
			[np.cos(self.y_rot),  0, 	np.sin(self.y_rot)],
			[0,  			 1, 				0],
			[-np.sin(self.y_rot), 0, 	np.cos(self.y_rot)]
							])
		R_z = np.array([
			[np.cos(self.z_rot), -np.sin(self.z_rot), 0],
			[np.sin(self.z_rot),  np.cos(self.z_rot), 0],
			[0,   		 0, 				1]
							])
		R = R_x@R_y@R_z
		T = np.array([
			[self.x],
			[self.y],
			[self.z]
			])
		M = np.append(R, T, axis = 1)
		M = np.append(M, np.array([[0, 0, 0, 1]]), axis = 0)

		return M