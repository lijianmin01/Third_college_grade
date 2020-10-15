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

    print(a)
    print(b)
    print(a1)
    print(b1)

    len_1 = len(a)

    img_sq_1 = np.ones((len_1,3),dtype='int')
    img_sq_2 = np.ones((len_1,2), dtype='int')

    img_sq_1[:,0] = a[:]
    img_sq_1[:,1] = b[:]

    img_sq_2[:,0] = a1[:]
    img_sq_2[:,1] = b1[:]

    print(img_sq_1)
    print(img_sq_2)

    return img_sq_1,img_sq_2

# 将列表变成整形
def float_int(np):
    for i in range(len(np)):
        for j in range(len(np[i])):
            np[i][j] = int(np[i][j])

    return np

if __name__ == '__main__':
    a, b = [], []
    # 第二张图片
    a1, b1 = [], []

    img1 = cv2.imread(r'T:\imgs\XL4\klcc_a.png')
    img2 = cv2.imread(r"T:\imgs\XL4\klcc_b.png")

    img1_copy = img1[:]
    img2_copy = img2[:]

    # 获取同点对
    # img_sq_1, img_sq_2 = get_same_point()

    # 因为之前对图像做出了修改，所以要恢复原图像
    img1 = cv2.imread(r'T:\imgs\XL4\klcc_a.png')
    img2 = cv2.imread(r"T:\imgs\XL4\klcc_b.png")

    # test 用例
    img_sq_1 = [[153,316,1],[344,352,1],[355,403,1],[537,380,1]]
    img_sq_2 = [[ 72,343],[273,369],[285,421],[463,391]]
    # 转换成矩阵形式
    img_sq_1 = np.mat(img_sq_1)
    img_sq_2 = np.mat(img_sq_2)


    """
    img_sq_1:
    [[153 316   1]
     [344 352   1]
     [355 403   1]
     [537 380   1]]
    img_sq_2:
    [[ 72 343]
     [273 369]
     [285 421]
     [463 391]]
    
    """

    # 求A
    U = img_sq_2[:]
    X = img_sq_1[:]
    A = np.dot(X.T,X)
    A = A.I
    A = np.dot(A,X.T)
    A = np.dot(A,U)

    # print(A)
    """
    [[ 1.00022874e+00 -4.14776097e-02]
     [ 1.07400244e-01  9.99067849e-01]
     [-1.13038867e+02  3.29912376e+01]]
    """

    # img1_coordinate 记录 X 图像的原始坐标
    # img2_coordinate 记录 U 图像的原始坐标
    # M 表示走坐标  N 表示横坐标
    M1 , N1 = img1.shape[0], img1.shape[1]
    M2, N2 = img2.shape[0], img2.shape[1]

    img1_coordinate = []
    img2_coordinate = []

    for x in range(M1):
        for y in range(N1):
            img1_coordinate.append([x,y])

    for x in range(M2):
        for y in range(N2):
            img2_coordinate.append([x,y])

    # img1_coordinate_change 记录 X 图像的改变后的坐标
    # img2_coordinate_change 记录 U 图像的改变后的坐标
    img1_coordinate = np.array(img1_coordinate)
    img2_coordinate = np.array(img2_coordinate)

    img1_coordinate_change = img1_coordinate.copy()
    img2_coordinate_change = img2_coordinate.copy()
    print("改变之前坐标")
    print(np.mat(img1_coordinate_change))


    # 根据变换矩阵，来进行坐标转换
    # 变换矩阵X1
    X1 = []
    for x in range(M1):
        for y in range(N1):
            X1.append([x,y,1])
    # 将其转换为矩阵
    X1 = np.mat(X1)
    # print(X1)
    """
    [[  0   0   1]
     [  0   1   1]
     [  0   2   1]
     ...
     [485 645   1]
     [485 646   1]
     [485 647   1]]
    """
    # 记录变换后的坐标U1
    U1 = np.dot(X1,A)
    # print(U1)
    """
    [[-113.03886664   32.99123757]
     [-112.93146639   33.99030542]
     [-112.82406615   34.98937327]
     ...
     [ 441.34522701  657.27335977]
     [ 441.45262726  658.27242762]
     [ 441.5600275   659.27149547]]
    """

    # 寻找变换矩阵中是否存在负数
    U1_min = np.min(U1,axis=0).tolist()
    x_min,y_min = U1_min[0][0],U1_min[0][1]
    # print(x_min,y_min)
    # # -113.03886663513177 12.874596885406799

    # print("img2改变之前的坐标")
    # print(np.mat(img2_coordinate))
    U1 = np.array(U1)
    if x_min<0:
        cnt = x_min*(-1)
        for index in range(len(img1_coordinate_change)):
            img1_coordinate_change[index][0]=U1[index][0]+cnt
        cnt = x_min * (-1)
        for index in range(len(img2_coordinate_change)):
            img2_coordinate_change[index][0]+=cnt

    if y_min<0:
        cnt = y_min*(-1)
        for index in range(len(img1_coordinate_change)):
            img1_coordinate_change[index][1]=U1[index][1]+cnt
        for index in range(len(img2_coordinate_change)):
            img2_coordinate_change[index][1]+=cnt

    # print("img2改变之后的坐标")
    # print(np.mat(img2_coordinate_change))

    # print("变换之后的坐标")
    # print(np.mat(U1))
    # print("改变之后坐标")
    # print(np.mat(img1_coordinate_change))
    # print("原来的坐标")
    # print(np.mat(img1_coordinate))

    # 寻找最大的横纵坐标
    x,y = 0,0

    img1_max = np.max(img1_coordinate_change,axis=0)
    img2_max = np.max(img2_coordinate_change, axis=0)
    print(img1_max)
    print(img2_max)

    if(img1_max[0]>img2_max[0]):
        x = img1_max[0]
    else:
        x = img2_max[0]

    if (img1_max[1] > img2_max[1]):
        y = img1_max[1]
    else:
        y = img2_max[1]

    # 开始构建一个大的图像
    img3 = np.zeros([ 1000,1000,3], np.uint8)



    for index in range(len(img2_coordinate)):
        try:
            img3[int(img2_coordinate_change[index][1]),int(img2_coordinate_change[index][0])]=img2[int(img2_coordinate[index][1]),int(img2_coordinate[index][0])]
        except:
            continue

    # for index in range(len(img1_coordinate_change)):
    #     try:
    #         img3[int(img1_coordinate_change[index][1]),int(img1_coordinate_change[index][0])]=img1[int(img1_coordinate[index][1]),int(img1_coordinate[index][0])]
    #     except:
    #         continue


    cv2.imshow("3",img3)
    cv2.waitKey(0)


