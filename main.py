from cube import Cube
from sphere import Sphere
from torus import Torus
from line import Line
from rectangle import Rectangle
from scene import Scene
from joint import Joint
from read_obj import ReadObj
from camera import Camera

import numpy as np

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height)


# cube = Cube(x=1,y=0,z=0,w=0.5, h=0.5,l=0.5)
rect = Rectangle(x=0, y=0, z=3, w=1.5, l=3)
line1 = Line(x = 0, y = 0, z = 2.25, length = 1.5)
line2 = Line(x = 0, y = 0, z = 0.75, length = 1.5)
j = Joint(x = 0, y = 0, z = 0, axis = [0, 1, 0], parent = line1, child = line2)

camera = Camera(x = 0, y = 0, z = 20, cx = scene_width//2, cy = scene_height//2, fx = 1000, fy = 1000, x_rot = np.pi/2, z_rot = np.pi/2)

scene.add_camera(camera)

scene.add_object(line1)
scene.add_object(line2)
# scene.add_object(cube)
scene.add_object(rect)


ang = 0
camera_x = 0
camera_y = 0
camera_z = 7
while True:
	j.set_joint_position(ang)
	k = scene.render_scene()
	camera.rotate(np.pi/2, 0, ang/10)
	# line1.rotate(ang, ang, 0)
	# sphere.translate(0, np.sin(ang), 0)
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