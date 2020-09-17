#Program to draw an eclipse on a black image

import numpy as np 
from skimage import io, draw 

# 1.create an empty image,and Draw a ellipse
img = np.zeros((200, 200), dtype=np.uint8)
x, y = draw.ellipse(50, 50, 10, 20)
img[x, y] = 1
io.imshow(img)
io.show()

# 2.create an image,and Draw a circle
img = np.zeros((200, 200), dtype=np.uint8)
x, y = draw.circle(150, 150, 10)
img[x, y] = 1
io.imshow(img)
io.show()

# 3.Make an empty(blank) image,and draw a polygon
img = np.zeros((200, 200), dtype=np.uint8)
r = np.array([10, 25, 80, 50])
c = np.array([10, 60, 40, 10])
x, y = draw.polygon(r, c)
img[x, y] = 1
io.imshow(img)
io.show()

