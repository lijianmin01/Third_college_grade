# -*- coding: utf-8 -*-
# 基于python-opencv的图像读取、可视化
# 注意：这里用到了基于opencv、plt两种方式的显示化

# 导入opencv包
import cv2
import matplotlib.pyplot as plt
 
#imagepath='flowers.png'
imagepath='flowers1.bmp'
image = cv2.imread(imagepath)
print(type(image)) #结果为<class 'numpy.ndarray'>
print(image.shape) #结果为(2304, 4096, 3)
 
cv2.imshow('1A-bgrImage',image)
cv2.waitKey()
cv2.destroyAllWindows()

imgflip = cv2.flip(image,0) # 0-上下翻转，1-左右翻转，-1-同时
cv2.imshow('1B-bgrImage flipped',imgflip)
cv2.waitKey()
cv2.destroyAllWindows()

plt.figure(figsize = (20,5))
plt.subplot(121)
plt.imshow(image)
 
# BGR to RGB
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('2-rgbImage',image_rgb)
cv2.waitKey()
cv2.destroyAllWindows()

plt.subplot(122)
plt.imshow(image_rgb)
plt.xticks([])
plt.yticks([])

plt.savefig('10_opencv.pdf')