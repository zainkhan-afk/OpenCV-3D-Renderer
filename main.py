from cube import Cube
from scene import Scene
from camera import Camera

scene_width = 700
scene_height = 700

scene = Scene(width = scene_width, height = scene_height)

cube1 = Cube(x = 3, y = 2, z = -2)
cube2 = Cube(x = -3, y = 3, z = -1)
cube3 = Cube(x = 0, y = 0, z = 1)
camera = Camera(x = 0, y = 0, z = 7, cx = scene_width//2, cy = scene_height//2)

scene.add_camera(camera)
scene.add_object(cube1)
scene.add_object(cube2)
scene.add_object(cube3)


ang = 0
while True:
	k = scene.render_scene()
	camera.rotate(0, ang, 0)
	# cube1.rotate(0, ang, 0)
	ang += 0.1
	if k == ord("q"):
		break