from cube import Cube
from sphere import Sphere
from torus import Torus
from scene import Scene
from read_obj import ReadObj
from camera import Camera

import numpy as np

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height)

ant = ReadObj("ANT_BLK.OBJ", scale = 5)
camera = Camera(x = 0, y = 0, z = 20, cx = scene_width//2, cy = scene_height//2, fx = 1000, fy = 1000)

scene.add_camera(camera)
scene.add_object(ant)


ang = 0
camera_x = 0
camera_y = 0
camera_z = 7
while True:
	k = scene.render_scene()
	camera.rotate(0, ang, 0)
	ang += 0.025
	if k == ord("q"):
		break