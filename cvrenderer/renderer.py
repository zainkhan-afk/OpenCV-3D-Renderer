from .draw import Draw

class Renderer(Draw):
	def __init__(self, width, height, save_as_video = False):
		Draw.__init__(self, width, height, save_as_video)

	def render(self, camera, objects):
		self.clear()
		for obj in objects:
			M1 = camera.get_intrinsic_matrix()
			M2 = camera.get_exrinsic_matrix()
			pts = obj.get_points()

			transformed_pts = M1@M2@pts

			transformed_pts = transformed_pts/transformed_pts[-1, :]
			transformed_pts = transformed_pts[:2, :].T.astype("int")

			self.draw(transformed_pts, obj, draw_points = False)

		k = self.show()
		return k