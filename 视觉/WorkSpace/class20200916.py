from skimage import data, io, filters, feature, segmentation
from skimage import color, exposure, measure, morphology, draw
from matplotlib import pyplot as plt
from skimage import transform as tf

image = data.chelsea()
io.imshow(image)
io.show()

# 灰度转换
gray = color.rgb2gray(image)
fig,axes = plt.subplots(1,2,figsize=(8,4))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title("Input RGB")
ax[1].imshow(gray, cmap=plt.cm.gray)
ax[1].set_title("gray")
 
fig.tight_layout()
plt.show()

