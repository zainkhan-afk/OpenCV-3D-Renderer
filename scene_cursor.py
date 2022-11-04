from shape import Shape
from line import Line
import numpy as np
from utils import *

class SceneCursor(Shape):
	def __init__(self, x, y, z, camera):
		Shape.__init__(self, x, y, z, 0, 0, 0)

		self.name = "SceneCursor"
		self.camera = camera

		self.origin = np.array([[0, 0, 0]])

		x_line = Line(x = 0, y = 0, z = 0, x_rot = 0, y_rot = 0, z_rot = 0)
		y_line = Line(x = 0, y = 0, z = 0, x_rot = 0, y_rot = 0, z_rot = 0)
		z_line = Line(x = 0, y = 0, z = 0, x_rot = 0, y_rot = 0, z_rot = 0)
		self.lines = {"X":x_line, "Y":z_line, "Z":z_line}

	def update_matrices(self):
		W_M_camera = self.camera.get_transformation_matrix()
		camera_M_cursor = np.array([
									[1, 0, 0, 0],
									[0, 1, 0, 0],
									[0, 0, 1, 1],
									[0, 0, 0, 1]
									])
		W_M_cursor = W_M_camera@camera_M_cursor
		self.set_transformation_matrix(W_M_cursor)

		W_M_x = self.lines["X"].get_transformation_matrix()
		W_M_y = self.lines["Y"].get_transformation_matrix()
		W_M_z = self.lines["Z"].get_transformation_matrix()

		cursor_M_W = get_inverse_transformation(W_M_cursor)
		cursor_M_x = cursor_M_W@W_M_x
		cursor_M_y = cursor_M_W@W_M_y
		cursor_M_z = cursor_M_W@W_M_z

		self.lines["X"].set_transformation_matrix(cursor_M_x)
		self.lines["Y"].set_transformation_matrix(cursor_M_y)
		self.lines["Z"].set_transformation_matrix(cursor_M_z)