
# 0.导入必要的类、模块
import imageio
import matplotlib.pyplot as plt
import random

# 1.原始彩色图像的读取及可视化
pic = imageio.imread('demo_1.jpg')
plt.figure(figsize = (10,10))
plt.imshow(pic)
plt.title(f'1--original image with shape {pic.shape} ')
plt.show()


# 2.找到原始图像中过低像素值的位置
low_pixel = pic < 20

# to ensure of it let's check if all values in low_pixel are True or not
if low_pixel.any() == True:
    print('0--low pixel shape:',low_pixel.shape)
print('1--pic shape: ',pic.shape)
print('2--low pixel shape: ', low_pixel.shape)  


# 3. 将过低的像素值设置为某个随机抽取的值：randomly choose a value 
# (1)load the orginal image
pic = imageio.imread('demo_1.jpg')

# (2)set value randomly range from 25 to 225 - these value also randomly choosen
pic[low_pixel] = random.randint(25,225)

# (3)display the image
plt.figure( figsize = (10,10))
plt.imshow(pic)
plt.show()
