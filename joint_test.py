from cvrenderer.utils import *
import numpy as np
from cvrenderer.shapes.line import Line
from cvrenderer.shapes.joint import Joint
from cvrenderer.scene import Scene
from cvrenderer.camera import Camera

object_1 = Line(x = 0, y = 0, z = 0.5, length = 1, thickness=2, color=(255, 0, 0))
object_2 = Line(x = 0, y = 0, z = -0.5, length = 1, thickness=2, color=(0, 255, 0))

# self.fl_j2 = Joint(x = self.body_w/2, y = self.body_l/2+self.l1, z = self.body_initial_height, axis = [0, 1, 0], parent = self.fl_hip, child = self.fl_knee)

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height, save_as_video = False)


camera = Camera(x = 0, y = 0, z = 20,
				cx = scene_width//2, cy = scene_height//2, 
				width = scene_width, height = scene_height,
				x_rot = 0, z_rot = 0,
				fov_x = 60, fov_y = 60)

scene.add_object(object_1)
scene.add_object(object_2)
# scene.add_axis(scaler=1)

scene.add_camera(camera)

ang = 0
while True:
	k = scene.render_scene()
	ang += 0.025
	if k == ord("q"):
		break

scene.destroy_scene()