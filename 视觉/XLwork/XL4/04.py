import cv2
import numpy as np

# 第一张图片
def on_EVENT_LBUTTONDOWN1(event, x, y,flags, param):
    # 点击三次，获得三个位置的坐标，销毁窗口
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(y)
        b.append(x)
        cv2.circle(img1, (x, y), 1, ( 0, 0,255), thickness=4)
        cv2.putText(img1, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image1", img1)

# 第二张图片
def on_EVENT_LBUTTONDOWN2(event, x, y,flags, param):
    # 点击三次，获得三个位置的坐标，销毁窗口
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a1.append(y)
        b1.append(x)
        cv2.circle(img2, (x, y), 1, (255, 0, 0), thickness=4)
        cv2.putText(img2, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image2", img2)

# 获取同名点对
def get_same_point():
    # 第一张图片
    cv2.namedWindow("image1")
    cv2.setMouseCallback("image1", on_EVENT_LBUTTONDOWN1)
    cv2.imshow("image1", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 第二张图片
    cv2.namedWindow("image2")
    cv2.setMouseCallback("image2", on_EVENT_LBUTTONDOWN2)
    cv2.imshow("image2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    len_1 = len(a)

    img_sq_1 = np.ones((len_1,3),dtype='int')
    img_sq_2 = np.ones((len_1,2), dtype='int')

    img_sq_1[:,0] = a[:]
    img_sq_1[:,1] = b[:]

    img_sq_2[:,0] = a1[:]
    img_sq_2[:,1] = b1[:]


    return img_sq_1,img_sq_2



if __name__ == '__main__':
    a, b = [], []
    # 第二张图片
    a1, b1 = [], []

    img1 = cv2.imread(r'T:\imgs\XL4\klcc_a.png')
    img2 = cv2.imread(r"T:\imgs\XL4\klcc_b.png")



    # 获取同点对
    X, U = get_same_point()

    # 重新获取原图像
    # img1 = cv2.imread(r'T:\imgs\XL4\klcc_a.png')
    # img2 = cv2.imread(r"T:\imgs\XL4\klcc_b.png")

    # 图像配准求A
    A = np.dot(X.T,X)
    A = np.mat(A)
    A = A.I
    A = np.dot(A,X.T)
    A = np.dot(A,U)

    # 记录原来的图像的卫士
    img1_zb = []
    for x in range(img1.shape[0]):
        for y in range(img1.shape[1]):
            img1_zb.append([x,y,1])

    img2_zb = []
    for x in range(img2.shape[0]):
        for y in range(img2.shape[1]):
            img2_zb.append([x, y])

    # 将图像1的位置变成矩阵
    img1_zb = np.mat(img1_zb)

    # 求图像一变换之后的矩阵
    img1_change_zb = np.dot(img1_zb,A)
    print(img1_change_zb)
    img1_change_zb = np.array(img1_change_zb)

    M1,N1 = img2.shape[0],img2.shape[1]
    index = 0
    for x in range(img2.shape[0]):
        for y in range(img2.shape[1]):
            if not (0<= int(img1_change_zb[index][0])<M1 and 0<= int(img1_change_zb[index][1])<N1):
                img1[x,y]=255
                img2[x,y]=255
            else:
                img2[x,y]=img2[int(img1_change_zb[index][0]),int(img1_change_zb[index][1])]
            index+=1

    img3 = np.hstack((img1,img2))

    cv2.imshow("3",img3)
    cv2.waitKey(0)

    # # 图像叠加效果
    # img4 = cv2.add(img1,img2)
    # cv2.imshow("4", img4)
    # cv2.waitKey(0)
