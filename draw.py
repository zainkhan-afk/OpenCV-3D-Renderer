import cv2
import numpy as np

class Draw:
	def __init__(self, width, height, window_name = "Canvas"):
		self.width = width
		self.height = height
		self.canvas = np.zeros((height, width, 3)).astype("uint8")
		self.window_name = window_name

	def clear(self):
		self.canvas = np.zeros((self.height, self.width, 3)).astype("uint8")

	def draw(self, pts):
		for pt in pts:
			cv2.circle(self.canvas, pt, 2, (0, 255, 0), -1)

		for i in range(3):
			cv2.line(self.canvas, pts[i, :], pts[i+1, :], (255, 0, 0), 1)
			cv2.line(self.canvas, pts[i, :], pts[i+4, :], (255, 0, 0), 1)
			cv2.line(self.canvas, pts[i+4, :], pts[i+4+1, :], (255, 0, 0), 1)
			if i == 2:
				cv2.line(self.canvas, pts[i+1, :], pts[0, :], (255, 0, 0), 1)
				cv2.line(self.canvas, pts[i+1, :], pts[7, :], (255, 0, 0), 1)
				cv2.line(self.canvas, pts[i+4+1, :], pts[4, :], (255, 0, 0), 1)


	def show(self):
		cv2.imshow(self.window_name, self.canvas)
		return cv2.waitKey(30)