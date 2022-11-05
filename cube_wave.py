from cvrenderer.shapes.cube import Cube
from cvrenderer.scene import Scene
from cvrenderer.camera import Camera

import numpy as np

scene_width = 700
scene_height = 700

num_cubes = 12

scene = Scene(width = scene_width, height = scene_height)


camera = Camera(x = 5, y = 0, z = 50,
				x_rot = np.pi/5, y_rot = np.pi/2, z_rot = 0, 
				cx = scene_width//2, cy = scene_height//2, 
				fx = 1000, fy = 1000)

cube_dict = {}

for x in range(-num_cubes//2, num_cubes//2+1):
	temp = {}
	for z in range(-num_cubes//2, num_cubes//2+1):
		cube = Cube(x = x, y = 0, z = z, h = 2, w = 1, l = 1)
		scene.add_object(cube)
		temp[z] = cube
	cube_dict[x] = temp


scene.add_camera(camera)

ang = 0
while True:
	k = scene.render_scene()
	for x in range(-num_cubes//2, num_cubes//2+1):
		for z in range(-num_cubes//2, num_cubes//2+1):
			dist = np.sqrt(x**2 + z**2)
			new_h = 1.5+((np.sin(ang + dist)+1)/2)*5
			cube_dict[x][z].set_scale(h = new_h, w = 1, l = 1)
	ang += 0.1
	if k == ord("q"):
		break