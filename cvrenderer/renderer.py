from .draw import Draw
from .utils import *

class Renderer(Draw):
	def __init__(self, width, height, save_as_video = False):
		Draw.__init__(self, width, height, save_as_video)

	def render(self, camera, objects):
		self.clear()
		for obj in objects:
			M1 = camera.get_intrinsic_matrix()
			M2 = camera.get_exrinsic_matrix()
			
			# TODO: Make the camera rotations relative to the camera frame, not the world origin.
			# R = M2[0:3, 0:3]
			# trans = M2[:-1, -1][:, np.newaxis]
			# trans = np.append(trans, np.array([[1]]), axis = 0)
			# new_R = np.linalg.inv(R)
			# new_trans = -new_R@trans
			# M2 = np.append(R, new_trans, axis = 1)

			pts = obj.get_points()


			transformed_pts = M1@M2@pts

			transformed_pts = transformed_pts/transformed_pts[-1, :]
			transformed_pts = transformed_pts[:2, :].T.astype("int")

			self.draw(transformed_pts, obj, draw_points = False)

		k = self.show()
		return k