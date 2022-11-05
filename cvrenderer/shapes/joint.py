from cvrenderer.shapes.shape import Shape
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

		self.prev_position = 0
		self.current_position = 0

		self.prev_R = np.array([[1,0,0], [0,1,0], [0,0,1]])

		W_M_parent = self.parent.get_transformation_matrix()
		W_M_joint = self.get_transformation_matrix()
		W_M_child = self.child.get_transformation_matrix()

		parent_M_W = get_inverse_transformation(W_M_parent)
		joint_M_W = get_inverse_transformation(W_M_joint)

		self.parent_M_joint = parent_M_W@W_M_joint
		self.joint_M_child = joint_M_W@W_M_child

	def set_joint_position(self, position):
		self.prev_position = self.current_position
		self.current_position = position
		self.update_matrices()

	def update_matrices(self):
		W_M_parent = self.parent.get_transformation_matrix()

		W_M_joint = W_M_parent@self.parent_M_joint
		self.set_transformation_matrix(W_M_joint)

		W_M_child = W_M_joint@self.joint_M_child
		self.child.set_transformation_matrix(W_M_child)

		x_rot = (self.current_position )*self.axis[0]
		y_rot = (self.current_position )*self.axis[1]
		z_rot = (self.current_position )*self.axis[2]

		R = get_rotation_matrix(x_rot, y_rot, z_rot)
		T = np.array([
			[0],
			[0],
			[0]
			])
		

		M = np.append(R, T, axis = 1)
		M = np.append(M, np.array([[0, 0, 0, 1]]), axis = 0)

		joint_M_W = get_inverse_transformation(W_M_joint)
		join_M_child = joint_M_W@W_M_child

		join_M_child = M@join_M_child

		W_M_child = W_M_joint@join_M_child

		self.child.set_transformation_matrix(W_M_child)