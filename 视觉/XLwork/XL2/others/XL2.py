from skimage import io,transform,data,color
import matplotlib.pyplot as plt
import numpy as np


# plt  显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 2. 固定灰度级数，降低该图像的空间分辨率，体会不同空间分辨率下图像的视觉效果；
## 因为该图像的灰度等级是256的 ， 分别把图像的空间分辨率 缩小 为原来的 1,8,16,32,128,256倍 观察效果

# 将图像缩小k倍,并显示出来
def narrwo_k_img(img,k):
    height, width = img.shape[0], img.shape[1]
    img_cnt = transform.resize(img, [int(height / k), int(width / k)])
    # io.imshow(img_cnt)
    # io.show()
    return img_cnt


def narrow_img():
    img = data.camera()
    img = color.gray2rgb(img)
    # 将图像的空间分辨率缩小k倍
    k_list=[1,8,16,32,128,256]
    labels = ['原图像','8倍','16倍','32倍','128倍','256倍']
    img_list = []
    for k in k_list:
        img_list.append(narrwo_k_img(img,k))
    plt.figure()
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(img_list[i])
        io.imsave(str(i)+".jpg",img_list[i])
        plt.title(labels[i])

    plt.show()

# 3. 固定空间分辨率，降低灰度分辨率，体会不同灰度分辨率下的图像视觉效果。





def main():
    narrow_img()
    #reduce_gray_resolution()

    pass

if __name__ == '__main__':
    main()