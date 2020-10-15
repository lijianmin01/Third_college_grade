import cv2
import numpy as np

# 全局变量
# 第几张图片   0  第一张   1 第二张
img_flag = 0

# 第一张图片
def on_EVENT_LBUTTONDOWN1(event, x, y,flags, param):
    # 点击三次，获得三个位置的坐标，销毁窗口
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img1, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img1, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image1", img1)

# 第二张图片
def on_EVENT_LBUTTONDOWN2(event, x, y,flags, param):
    # 点击三次，获得三个位置的坐标，销毁窗口
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a1.append(x)
        b1.append(y)
        cv2.circle(img2, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img2, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image2", img2)

# 获取同名点对
def get_same_point(img_flag):
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

    # print(a)
    # print(b)
    # print(a1)
    # print(b1)

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

if __name__ == '__main__':
    # 分表保存第一张图片与第二张图片的同名点对
    # 记录同名点对
    # 第一张图片
    a,b = [], []
    # 第二张图片
    a1, b1 = [], []



    img1 = cv2.imread(r'T:\imgs\XL4\klcc_a.png')
    img2 = cv2.imread(r"T:\imgs\XL4\klcc_b.png")

    img1_copy = img1[:]
    img2_copy = img2[:]

    # img_sq_1, img_sq_2 = get_same_point(img_flag)

    # 获取同点对
    # img_sq_1,img_sq_2 = get_same_point(img_flag)

    """
    [[318 250   1]
     [153 318   1]
     [344 351   1]]
    [[243 270]
     [ 74 342]
     [272 369]]
    """

    # 为了避免重复获取同点对，所以直接获取，后期删了
    X = np.mat([[318,250,1],[153,318,1],[344,351,1]])
    U = np.mat([[243,270],[ 74,342],[272,369]])

    # 前A
    A = np.dot(X.I,U)
    print(A)

    # 因为当时画图的时候，图像已经被修改，所以，恢复原图像
    img1 = img1_copy[:]
    img2 = img2_copy[:]

    M1,N1 = img1.shape[0],img1.shape[1]
    M2, N2 = img2.shape[0], img2.shape[1]

    img1_cnt = img1[:]
    img2_cnt = img2[:]

    # 建立一个大型图片
    # 确定变换后的图片坐标

    # 变换后图片的坐标 X
    save_img2 = []
    for x in range(M1):
        for y in range(N1):
            cnt_sq = np.array([x, y, 1]).dot(A)
            cnt_sq = [int(cnt_sq.tolist()[0][0]),int(cnt_sq.tolist()[0][1])]
            save_img2.append(cnt_sq)


    # 参考图片  U
    save_img1 = []
    for x in range(M2):
        for y in range(N2):
            save_img1.append([x,y])

    save_img1 = np.array(save_img1)

    # 找变换后的图片的最小坐标
    save_img2=np.array(save_img2)
    min_h = np.min(save_img2,axis=0)

    # 用来记录坐标改变后的坐标
    save_img1_1 = save_img1[:]
    save_img2_2 = save_img2[:]

    # 当最小坐标出现负数的时候，进行调整
    for min_index in range(len(min_h)):
        if min_h[min_index]<0:
            cnt = min_h[min_index] * (-1)
            # 原图像
            for save_img1_index in range(len(save_img1)):
                save_img1_1[save_img1_index][min_index]+=cnt
            for save_img2_index in range(len(save_img2)):
                save_img2_2[save_img2_index][min_index]+=cnt


    # print(save_img1)
    # print(save_img2)

    # 调整完后，求图像的最大横纵坐标
    # 最大坐标
    max_h_1 = np.max(save_img1, axis=0)
    max_h_2 = np.max(save_img2, axis=0)
    max_x_y = []
    for i in range(len(max_h_1)):
        if max_h_1[i]>max_h_2[i]:
            max_x_y.append(max_h_1[i])
        else:
            max_x_y.append(max_h_2[i])

    # print(max_x_y)
    #
    # # # 构造大图片
    img3 = np.zeros([1000,1000, 3], np.uint8)


    print(np.size(img1,0)) # 行数
    print(np.size(img1,1)) # 列数

    print(len(save_img1))
    print(len(save_img2))

    if(len(save_img1_1)==len(save_img1)):
        print("666")


    for index in range(len(save_img2)):
        try:
            img3[save_img2_2[index][0],save_img2_2[index][1]]=img2[save_img2[index][0],save_img2[index][1]]
        except:
            img3[save_img2_2[index][0], save_img2_2[index][1]]=255

    for index in range(len(save_img1)):
        try:
            img3[save_img1_1[index][0],save_img1_1[index][1]]=img1[save_img1[index][0],save_img1[index][1]]
        except:
            img3[save_img1_1[index][0], save_img1_1[index][1]]=255

    cv2.imshow("3", img3)
    cv2.waitKey(0)





