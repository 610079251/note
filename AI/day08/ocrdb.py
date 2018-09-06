import numpy as np
import cv2 as cv
with open('../../data/ocrdb.dat', 'r') as f:
	for line in f.readlines():
		items = line.split('\t')
		char, image = items[1], items[6:-1]
		image = np.array(image, dtype=np.uint8)
		image *= 255
		image = image.reshape(16, 8)
		image = cv.resize(image, None, fx=10, fy=10)
		cv.imshow(char, image)
		if cv.waitKey(100) == 27:
			break