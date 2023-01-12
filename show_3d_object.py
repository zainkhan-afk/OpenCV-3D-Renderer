from cvrenderer.shapes.read_obj import ReadObj
from cvrenderer.camera import Camera
from cvrenderer.scene import Scene

import numpy as np

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height)

ant = ReadObj("ANT_BLK.OBJ", x_rot=-np.pi/2,scale = 5)
camera = Camera(x = 0, y = 0, z = 20,
				cx = scene_width//2, cy = scene_height//2, 
				width = scene_width, height = scene_height,
				x_rot = 0, z_rot = 0,
				fov_x = 60, fov_y = 60)

scene.add_camera(camera)
scene.add_object(ant)


ang = 0
camera_x = 0
camera_y = 0
camera_z = 7
while True:
	k = scene.render_scene()
	camera.rotate(0, 0, ang)
	ang += 0.025
	if k == ord("q"):
		break