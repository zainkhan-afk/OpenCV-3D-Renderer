import numpy as np


class Camera:
	def __init__(self, x, y, z, cx, cy, width, height, fov_x = 100, fov_y = 100, x_rot = 0, y_rot = 0, z_rot = 0):
		self.x = x
		self.y = y
		self.z = z

		self.x_rot = x_rot + np.pi/2
		self.y_rot = y_rot
		self.z_rot = z_rot - np.pi/2

		self.fov_x = fov_x/180*np.pi
		self.fov_y = fov_y/180*np.pi

		self.fx = width/np.tan(self.fov_x/2)
		self.fy = height/np.tan(self.fov_y/2)

		self.cx = cx
		self.cy = cy

	def rotate(self, x_rot, y_rot, z_rot):
		self.x_rot = x_rot + np.pi/2
		self.y_rot = y_rot
		self.z_rot = z_rot - np.pi/2

	def translate(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def get_intrinsic_matrix(self):
		M = np.array([
			[self.fx, 		 0, self.cx],
			[		0, self.fy, self.cy],
			[		0,  	 0,  	  1],
			])

		return M


	def get_exrinsic_matrix(self):
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

		return M