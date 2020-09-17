# 图像的可视化、基本属性的获取、部分内容分的修改以及可视化

# 0.导入必要的模块
import imageio
import matplotlib.pyplot as plt


# 1.原始图像的读取
pic = imageio.imread('demo_2.jpg')

# 2. 原始图像基本属性的可视化
print('1--Type of the image : ' , type(pic))
print('2--Shape of the image : {}'.format(pic.shape))
print('3--Image Hight = {}'.format(pic.shape[0]))
print('4--Image Width = {}'.format(pic.shape[1]))
print('5--Dimension of Image = {}'.format(pic.ndim))
print('6--Image size = {}'.format(pic.size))
print('7--Maximum RGB value in this image = {}'.format(pic.max()))
print('8--Minimum RGB value in this image = {}'.format(pic.min()))
print('9-- pixel value at [100,50]: ', pic[ 100, 50 ])
print('10--Value of only R channel = {}'.format(pic[ 100, 50, 0]))
print('11--Value of only G channel = {}'.format(pic[ 100, 50, 1]))
print('12--Value of only B channel = {}'.format(pic[ 100, 50, 2]))

# 3.原始彩色图像、以及RGB三个通道的可视化
plt.figure(figsize = (15,15))
plt.imshow(pic)
plt.title('1--original color image')
plt.ylabel('Height = {}'.format(pic.shape[0]))
plt.xlabel('Width = {}'.format(pic.shape[1]))


plt.figure(figsize = (15,15))
plt.title('R channel')
plt.ylabel('Height {}'.format(pic.shape[0]))
plt.xlabel('Width {}'.format(pic.shape[1]))
plt.imshow(pic[ : , : , 0])
plt.show()
    
plt.figure(figsize = (15,15))
plt.title('G channel')
plt.ylabel('Height {}'.format(pic.shape[0]))
plt.xlabel('Width {}'.format(pic.shape[1]))
plt.imshow(pic[ : , : , 1])
plt.show()

plt.figure(figsize = (15,15))
plt.title('B channel')
plt.ylabel('Height {}'.format(pic.shape[0]))
plt.xlabel('Width {}'.format(pic.shape[1]))
plt.imshow(pic[ : , : , 2])
plt.show()



# 4.改变图像中特定区域的颜色值，可视化
#   R channel: Row- 50 to 150
#   G channel: Row- 200 to 300
#   B channel: Row- 350 to 450

# 4-1.红
pic = imageio.imread('demo_2.jpg')
pic[50:150 , : , 0] = 255 # full intensity to those pixel's R channel
plt.figure( figsize = (15,15))
plt.imshow(pic)
plt.show()


# 4-2. 红+绿
pic[200:300 , : , 1] = 255 # full intensity to those pixel's G channel
plt.figure( figsize = (15,15))
plt.imshow(pic)
plt.show()

# 4-3. 红+绿+蓝
pic[350:450 , : , 2] = 255 # full intensity to those pixel's B channel
plt.figure( figsize = (15,15))
plt.imshow(pic)
plt.show()

# 5. 在上述工作基础上，同时改变某个区内三个颜色分量，使其灰度化效果
# set value 200 of all channels to those pixels which turns them to white

pic[ 50:450 , 400:600 , [0,1,2] ] = 200 
plt.figure( figsize = (15,15))
plt.imshow(pic)
plt.show()




