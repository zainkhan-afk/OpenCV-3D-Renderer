from cube import Cube
from sphere import Sphere
from torus import Torus
from scene import Scene
from camera import Camera

import numpy as np

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height)

cube = Cube(x = 3, y = 2, z = -2)
sphere = Sphere(x = 0, y = 0, z = 3)
torus = Torus(x = -3, y = -2, z = 0)
camera = Camera(x = 0, y = 0, z = 20, cx = scene_width//2, cy = scene_height//2, fx = 1000, fy = 1000)

scene.add_camera(camera)
scene.add_object(cube)
scene.add_object(sphere)
scene.add_object(torus)


ang = 0
camera_x = 0
camera_y = 0
camera_z = 7
while True:
	k = scene.render_scene()
	camera.rotate(0, ang, 0)
	# camera.translate(camera_x, camera_y, camera_z)
	ang += 0.025
	if k == ord("q"):
		break

	# if k == ord("w"):
	# 	camera_z -= 0.5

	# if k == ord("s"):
	# 	camera_z += 0.5

	# if k == ord("a"):
	# 	camera_x -= 0.5

	# if k == ord("d"):
	# 	camera_x += 0.5