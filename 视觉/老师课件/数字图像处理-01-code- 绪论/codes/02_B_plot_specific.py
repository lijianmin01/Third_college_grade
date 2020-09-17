"""
===============
Specific images
===============

"""
import matplotlib.pyplot as plt
import matplotlib

from skimage import data

matplotlib.rcParams['font.size'] = 18

######################################################################
#
# Stereo images
# =============


fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel() #将axes轴对象数组元素拉成1维

images = data.stereo_motorcycle()
ax[0].imshow(images[0])
ax[1].imshow(images[1])

#会自动调整子图参数，使之填充整个图像区域，更为紧凑
fig.tight_layout()
plt.show()

######################################################################
#
# Faces and non-faces dataset
# ===========================
#
# A sample of 20 over 200 images is displayed.


fig, axes = plt.subplots(4, 5, figsize=(20, 20))
ax = axes.ravel()
images = data.lfw_subset()
for i in range(20):
    ax[i].imshow(images[90+i], cmap=plt.cm.gray)
    ax[i].axis('off')
fig.tight_layout()
plt.show()
