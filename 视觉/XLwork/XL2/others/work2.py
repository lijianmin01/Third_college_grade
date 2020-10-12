import cv2

"""
图像灰度级指图像中的色度分量亮度的最大值与最小值之差的级别。
"""


# 生成灰度图像
def create_gray_img():
    img = cv2.imread('klcc_a.png')

    #cv2.imshow('原图像', img)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('灰度图像', img_gray)


    cv2.imwrite('klcc_a_gray.png',img_gray)

    pass


def main():
    img = cv2.imread(r'T:\imgs\XL2\klcc_a_gray.png')

    # 固定灰度级数
    img128 = cv2.garyStage(img,128)
    cv2.imshow('input_image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 确定灰度级数
    pass
if __name__ == '__main__':
    main()
