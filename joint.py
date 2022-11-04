from shape import Shape
from utils import *

class Joint(Shape):
	def __init__(self, x, y, z, axis, parent, child):
		Shape.__init__(self, x, y, z, 0, 0, 0)
		self.name = "JOINT"
		self.x = x
		self.y = y
		self.z = z
		self.axis = axis

		self.parent = parent
		self.child = child

	def set_joint_position(self, position):
		# x_rot = position*self.axis[0]
		# y_rot = position*self.axis[1]
		# z_rot = position*self.axis[2]
		# self.rotate(x_rot, y_rot, z_rot)
		self.update_matrices(position)

	def update_matrices(self, position):
		self.parent.calculate_transformation_matrix()
		self.calculate_transformation_matrix()
		self.child.calculate_transformation_matrix()
		W_M_parent = self.parent.get_transformation_matrix()
		W_M_joint = self.get_transformation_matrix()
		W_M_child = self.child.get_transformation_matrix()

		x_rot = position*self.axis[0]
		y_rot = position*self.axis[1]
		z_rot = position*self.axis[2]

		R = get_rotation_matrix(x_rot, y_rot, z_rot)
		T = np.array([
			[0],
			[0],
			[0]
			])
		M = np.append(R, T, axis = 1)
		M = np.append(M, np.array([[0, 0, 0, 1]]), axis = 0)

		parent_M_W = get_inverse_transformation(W_M_parent)
		joint_M_W = get_inverse_transformation(W_M_joint)

		print()
		print(W_M_parent)
		print(W_M_joint)

		parent_M_joint = parent_M_W@W_M_joint
		join_M_child = joint_M_W@W_M_child
		join_M_child = M@join_M_child

		self.set_transformation_matrix(parent_M_joint)
		self.child.set_transformation_matrix(join_M_child)