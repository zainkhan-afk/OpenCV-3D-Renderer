import numpy as np

def get_inverse_transformation(T):
	R = T[0:3, 0:3]
	trans = T[:-1, -1][:, np.newaxis]

	new_R = np.linalg.inv(R)
	new_trans = -new_R@trans

	T = np.append(new_R, new_trans, axis = 1)
	T = np.append(T, np.array([[0, 0, 0, 1]]), axis = 0)

	return T

def get_rotation_matrix(x_rot, y_rot, z_rot):
	R_x = np.array([
			[1, 			     0,					  0],
			[0, np.cos(x_rot), -np.sin(x_rot)],
			[0, np.sin(x_rot),  np.cos(x_rot)]
							])
	R_y = np.array([
		[np.cos(y_rot),  0, 	np.sin(y_rot)],
		[0,  			 1, 				0],
		[-np.sin(y_rot), 0, 	np.cos(y_rot)]
						])
	R_z = np.array([
		[np.cos(z_rot), -np.sin(z_rot), 0],
		[np.sin(z_rot),  np.cos(z_rot), 0],
		[                 0,   		           0, 1]
						])
	R = R_x@R_y@R_z

	return R


if __name__ == "__main__":
	T1 = np.array([
					[0, 0, 1, 5],
					[0, 3, 0, 3],
					[-1, 0, 0, 2],
					[0, 0, 0, 1]
				])
	print(T1)
	T2 = get_inverse_transformation(T1)
	print(T2)
	print(T2@T1)