from cvrenderer.shapes.cube import Cube
from cvrenderer.shapes.sphere import Sphere

from cvrenderer.scene import Scene
from cvrenderer.camera import Camera

import numpy as np

scene_width = 700
scene_height = 700

num_cubes = 12

scene = Scene(width = scene_width, height = scene_height)


camera = Camera(x = 0, y = 0, z = 20,
				x_rot = np.pi/6, z_rot = 4*np.pi/3,
				cx = scene_width//2, cy = scene_height//2, 
				fx = 1000, fy = 1000)
cube = Cube()
sphere = Sphere(y = 2)

scene.add_object(cube)
scene.add_object(sphere)
scene.add_axis(scaler=1)

scene.add_camera(camera)

ang = 0
while True:
	scene.move_axis(delta_x = 0.01, delta_y = -0.01)
	sphere.rotate(ang, ang, 0)
	cube.rotate(ang, ang/10, ang/5)
	cube.translate(0, 0, np.sin(ang))
	k = scene.render_scene()
	ang += 0.025
	if k == ord("q"):
		break