# 原始卫星图像的可视化、部分内容的修改以及可视化

# 0.导入必要的模块
import imageio
import numpy as np
import matplotlib.pyplot as plt


# 1.读取原始卫星图像、并可视化
pic = imageio.imread('satimg.jpg')
plt.figure(figsize = (15,15))
plt.imshow(pic)
plt.xlabel(f'width {pic.shape[1]} pixels')
plt.ylabel(f'hieght {pic.shape[0]} pixels')
plt.title(f'Shape of the original satellite image {pic.shape}')
plt.show()


# 2. 分别处理不同通道，屏蔽掉相应通道取值过低的位置，并可视化
#    Detecting High Pixel of Each Channel

# (1)Only Red Pixel value , higher than 180
pic = imageio.imread('satimg.jpg')

red_mask = pic[:, :, 0] < 180
pic[red_mask] = 0

imageio.imsave('satimg_R.jpg',pic)

plt.figure(figsize=(15,15))
plt.imshow(pic)
plt.show()

# (2)Only Green Pixel value , higher than 180
pic = imageio.imread('satimg.jpg')
green_mask = pic[:, :, 1] < 180
pic[green_mask] = 0
imageio.imsave('satimg_G.jpg',pic)
plt.figure(figsize=(15,15))
plt.imshow(pic)
plt.show()

# (3)Only Blue Pixel value , higher than 180
pic = imageio.imread('satimg.jpg')
blue_mask = pic[:, :, 2] < 180
pic[blue_mask] = 0
imageio.imsave('satimg_B.jpg',pic)
plt.figure(figsize=(15,15))
plt.imshow(pic)

# 3.Composite mask using logical"and"
pic = imageio.imread('satimg.jpg')
final_mask = np.logical_and(red_mask, green_mask, blue_mask)
pic[final_mask] = 40
imageio.imsave('satimg_RGB.jpg',pic)
plt.figure(figsize=(15,15))
plt.imshow(pic)
