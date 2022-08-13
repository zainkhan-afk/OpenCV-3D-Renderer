import cv2
import numpy as np

class Draw:
	def __init__(self, width, height, window_name = "Canvas"):
		self.width = width
		self.height = height
		self.canvas = 255*np.ones((height, width, 3)).astype("uint8")
		self.window_name = window_name

	def clear(self):
		self.canvas = 255*np.ones((self.height, self.width, 3)).astype("uint8")

	def draw(self, pts, obj, draw_points = False):
		if draw_points:
			for pt in pts:
				cv2.circle(self.canvas, pt, 2, (0, 255, 0), -1)

		if obj.name == "CUBE":
			for i in range(3):
				cv2.line(self.canvas, pts[i, :], pts[i+1, :], ((0, 0, 0)), 1)
				cv2.line(self.canvas, pts[i, :], pts[i+4, :], ((0, 0, 0)), 1)
				cv2.line(self.canvas, pts[i+4, :], pts[i+4+1, :], ((0, 0, 0)), 1)
				if i == 2:
					cv2.line(self.canvas, pts[i+1, :], pts[0, :], ((0, 0, 0)), 1)
					cv2.line(self.canvas, pts[i+1, :], pts[7, :], ((0, 0, 0)), 1)
					cv2.line(self.canvas, pts[i+4+1, :], pts[4, :], ((0, 0, 0)), 1)

		if obj.name == "SPHERE":
			for i in range(360//obj.resolution):
				offset = i*360//obj.resolution
				offset_next = (i+1)*360//obj.resolution
				for j in range(360//obj.resolution - 1):
					cv2.line(self.canvas, pts[offset+j,:], pts[offset+j+1, :], ((0, 0, 0)), 1)
					if i<360//obj.resolution-1:
						cv2.line(self.canvas, pts[offset+j,:], pts[offset_next+j, :], ((0, 0, 0)), 1)
				cv2.line(self.canvas, pts[offset+j+1,:], pts[offset+0, :], ((0, 0, 0)), 1)

		if obj.name == "TORUS":
			for i in range(360//obj.resolution):
				offset = i*360//obj.resolution
				offset_next = (i+1)*360//obj.resolution
				for j in range(360//obj.resolution - 1):
					cv2.line(self.canvas, pts[offset+j,:], pts[offset+j+1, :], ((0, 0, 0)), 1)

					if i<360//obj.resolution-1:
						cv2.line(self.canvas, pts[offset+j,:], pts[offset_next+j, :], ((0, 0, 0)), 1)

					else:
						cv2.line(self.canvas, pts[offset+j,:], pts[0+j, :], ((0, 0, 0)), 1)

				cv2.line(self.canvas, pts[offset+j+1,:], pts[offset+0, :], ((0, 0, 0)), 1)


	def show(self):
		cv2.imshow(self.window_name, self.canvas)
		return cv2.waitKey(30)