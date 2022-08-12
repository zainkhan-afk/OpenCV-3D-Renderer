from cube import Cube
from scene import Scene
from camera import Camera

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height)

cube1 = Cube(x = 3, y = 2, z = -2)
cube2 = Cube(x = -3, y = 3, z = -1)
cube3 = Cube(x = 0, y = 0, z = 1)
camera = Camera(x = 0, y = 0, z = 20, cx = scene_width//2, cy = scene_height//2, fx = 1000, fy = 1000)

scene.add_camera(camera)
scene.add_object(cube1)
scene.add_object(cube2)
scene.add_object(cube3)


ang = 0
camera_x = 0
camera_y = 0
camera_z = 7
while True:
	k = scene.render_scene()
	camera.rotate(0, ang, 0)
	# camera.translate(camera_x, camera_y, camera_z)
	ang += 0.1
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