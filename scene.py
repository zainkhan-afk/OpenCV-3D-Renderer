from renderer import Renderer

class Scene(Renderer):
	def __init__(self, width, height):
		Renderer.__init__(self, width, height)
		self.objects = []

	def add_camera(self, camera):
		self.camera = camera

	def add_object(self, obj):
		self.objects.append(obj)

	def get_object_at(self, i):
		return self.objects[i]

	def render_scene(self):
		k = self.render(self.camera, self.objects)
		return k