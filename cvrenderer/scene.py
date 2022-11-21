from .renderer import Renderer
from .axis import Axis

class Scene(Renderer):
	def __init__(self, width, height, save_as_video = False):
		Renderer.__init__(self, width, height, save_as_video)
		self.objects = []
		self.axis = None
		self.stick_figures = []
		self.save_as_video = save_as_video

	def add_camera(self, camera):
		self.camera = camera

	def add_object(self, obj):
		self.objects.append(obj)

	def get_object_at(self, i):
		return self.objects[i]

	def render_scene(self):
		k = self.render(self.camera, self.objects)
		return k

	def add_axis(self, size=25, scaler=1):
		self.axis = Axis(size, scaler)
		self.objects = self.axis.lines + self.objects

	def move_axis(self, delta_x = 0, delta_y = 0):
		self.axis.translate_axis(delta_x, delta_y)

	def add_stick_figure(self, stick_figures):
		self.stick_figures.append(stick_figures)
		for figure in self.stick_figures:
			self.objects = self.objects + figure.shapes