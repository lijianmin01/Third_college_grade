# 将原始图像内容进行部分屏蔽

import imageio
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    # 1.读取原始图像
    pic = imageio.imread('demo_1.jpg')
    
    # 2.获取图像的行数、列数、颜色通道数
    total_row , total_col , layers = pic.shape
    
    # 3.基于Ogrid函数构造向量：
    #   Ogrid is a compact method of creating a multidimensional-ndarray 
    #   operations in single lines.
    x , y = np.ogrid[:total_row , :total_col]

    # 4.get the center values of the image
    cen_x , cen_y = total_row/2 , total_col/2
    
    
    # 5.生成与图像行数、列数一致的距离矩阵
    distance_from_the_center = np.sqrt((x-cen_x)**2 + (y-cen_y)**2)

    # 6.设置圆形mask的半径
    radius = (total_row/2)

    # 7.Using logical operator '>' 生成逻辑矩阵(圆形mask)
    
    circular_pic = distance_from_the_center > radius

    
    # 8.圆形区域以外的其它位置设置为0
    pic[circular_pic] = 0
    
    # 9.可视化mask之后的图像内容
    plt.figure(figsize = (10,10))
    plt.imshow(pic) 
    plt.savefig('05_masked image.pdf')
    plt.show()
