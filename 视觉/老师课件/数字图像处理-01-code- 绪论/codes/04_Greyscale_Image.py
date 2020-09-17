# 基于numpy库及pyplot模块的图像数据处理及可视化
# 0.导入必要的模块
#-*- coding:utf-8 -*-
import imageio
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   #用来正常显示负号

# 1.读取原始的彩色图像
pic = imageio.imread('demo_2.jpg')

# 2.注意lamada表达式的意义
#   基于方式1将原始彩色图像转化为灰度图像、并显示：灰度值=0.299R+0.587G+0.114B
gray1 = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
gray = gray1(pic)  

plt.figure( figsize = (10,10))
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
plt.title('方式1')
plt.show()

# 3.基于方式2将原始彩色图像转化为灰度图像、并显示：灰度值=0.21R+0.72G+0.07B
gray2 = lambda rgb : np.dot(rgb[... , :3] , [0.21 , 0.72, 0.07]) 
gray = gray2(pic)  

plt.figure( figsize = (10,10))
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
plt.title('方式2')
plt.show()


# 4.图像有关特性的了解
'''
Let's take a quick overview some the changed properties now the color image.
Like we observe some properties of color image, same statements are applying 
now for gray scaled image.
'''
# 行数*列数*通道数
print('0--Shape of the original color image : ' , pic.shape)
print('1--Type of the gray image : ' , type(gray))
print('2--Shape of the image : {}'.format(gray.shape))
print('3--Image Hight = {}'.format(gray.shape[0]))
print('4--Image Width = {}'.format(gray.shape[1]))
print('5--Dimension of Image = {}'.format(gray.ndim))
print('6--Image size = {}'.format(gray.size))
print('7--Maximum RGB value in this image = {}'.format(gray.max()))
print('8--Minimum RGB value in this image = {}'.format(gray.min()))
print('9--Random indexes [X,Y] : {}'.format(gray[100, 50]))
