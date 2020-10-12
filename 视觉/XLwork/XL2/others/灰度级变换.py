from skimage import io,exposure
import numpy as np

# 图像灰度级指图像中的色度分量亮度的最大值与最小值之差的级别。





def main():
    img = io.imread('klcc_a_gray.png')
    io.imshow(img)
    io.show()
    img1 = exposure.rescale_intensity(img,(0,64))
    io.imshow(img1)
    io.show()
    # exposure.rescale_intensity(img, (0, 64))
    # io.imshow(img)
    # io.show()
    # exposure.rescale_intensity(img, (0, 32))
    # io.imshow(img)
    # io.show()
    # exposure.rescale_intensity(img, (0, 1))
    # io.imshow(img)
    # io.show()
if __name__ == '__main__':
    main()