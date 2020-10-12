import cv2
import os
import numpy as np
from PIL import Image as ImagePIL
from skimage import io,color

import matplotlib.pyplot as plt


# plt  显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 2. 固定灰度级数，降低该图像的空间分辨率，体会不同空间分辨率下图像的视觉效果；
def change_the_spatial_resolution():
    img = ImagePIL.open(r'aman_gray.png')

    # 因为该图片的灰度级数是一定的，只需要改变空间分辨率即可
    # 分辨分辨率 k
    k_list = [90,70,50,30,10,2]
    # 新建文件夹，用来保存降低该图像空间分辨率的图像
    img_path ='img1/'
    # 如果没有该路径，则创建该路径
    if not os.path.exists(img_path):
        os.makedirs(img_path)

    # 压缩图像，并改变图像的分辨率
    for k in k_list:
        img.save(img_path+str(k)+".jpg",dpi=(k,k))

    # 打开图像，并显示出来
    imgs_list = [img]
    for k in k_list:
        img_cnt = io.imread((img_path+str(k)+'.jpg'))
        imgs_list.append(img_cnt)


    plt.figure()
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(imgs_list[i],cmap="gray")
        plt.title(str(i + 1))

    plt.show()

# 3. 固定空间分辨率，降低灰度分辨率，体会不同灰度分辨率下的图像视觉效果。
def change_the_grayscale_resolution():
    img = io.imread(r'aman_gray.png')

    imgs_list = []
    # 降低图像灰度分辨率 k
    k_list = [2,8,16,64,128,256]
    for k in k_list:
        img_cnt = reduce_Grayvalue(img,k)
        # io.imshow(img_cnt)
        # io.show()
        imgs_list.append(img_cnt)

    plt.figure()
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(imgs_list[i],cmap="gray")
        plt.title(str(i+1))

    plt.show()

#降低灰度级
def reduce_Grayvalue(img,level):
    img = cv2.copyTo(img, None)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            si = img[x, y]
            ni = int(level * si / 255 + 0.5) * (255 / level)
            img[x, y] = ni
    return img



if __name__ == '__main__':
    change_the_spatial_resolution()
    change_the_grayscale_resolution()
    pass