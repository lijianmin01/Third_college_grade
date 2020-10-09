import cv2
import numpy as np
from scipy import ndimage
import math




def on_EVENT_LBUTTONDOWN(event, x, y,flags, param):
    # 点击三次，获得三个位置的坐标，销毁窗口
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        # cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)

# 获取每次点击的坐标
def get_three_position():
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    cv2.waitKey(0)

    print(a)
    print(b)

# 旋转图片
def spin_img():
    # 找到眼睛倾斜角度和两眼的距离
    # 左眼坐标
    p1 = np.array([b[0],a[0]])
    # 右眼坐标
    p2 = np.array([b[1],a[1]])
    # 嘴中心坐标
    p3 = np.array([b[2],a[2]])

    # 根据公式计算成角度
    dp = p1 - p2
    angle = np.arctan(dp[0] / dp[1])

    # 旋转图片
    # 旋转图片
    rot_img = ndimage.rotate(img, angle=+angle * 180 / np.pi)
    # 旋转后图像的中点
    rot_image_center = np.array((np.array(rot_img.shape[:2]) - 1) / 2,
                                dtype=np.int)
    cv2.imshow('旋转图片',rot_img)
    cv2.waitKey(0)

    # 在旋转后的图片中找到眼睛的坐标
    # 原两眼距离的中点
    org_eye_center = np.array((p1 + p2) / 2, dtype=np.int)
    # 原图像的中点
    org_image_center = np.array((np.array(img.shape[:2]) - 1) / 2, dtype=np.int)
    # 以图片中心进行旋转，在旋转后的图片中找到眼睛的中点
    R = np.array([[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]])
    rot_eye_center = np.dot(R, org_eye_center[::-1]- org_image_center[::-1])[::-1] + rot_image_center
    rot_eye_center = np.array(rot_eye_center, dtype=int)

    print(rot_eye_center)
    # 模仿者100 * 100 裁剪图像

    # 两眼的距离
    l_dis = int(math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))

    # 嘴巴距离眼睛中心的距离一半
    l_e_m = int(math.sqrt((p3[0]-org_eye_center[0])**2+(p3[1]-org_eye_center[1])**2)/2)

    # 裁剪图像
    deal_with_img = rot_img[int(rot_eye_center[0]-l_e_m):int(rot_eye_center[0]+3*l_e_m),int(rot_eye_center[1]-l_dis):int(rot_eye_center[1]+l_dis)]
    cv2.imshow('裁剪完成图片', deal_with_img)
    cv2.waitKey(0)

    # 双线性
    pc1 = cv2.resize(deal_with_img,(100, 100), interpolation=cv2.INTER_LINEAR)
    # 双三次插值
    pc2 = cv2.resize(deal_with_img,(100, 100), interpolation=cv2.INTER_CUBIC)

    imghstack = np.hstack((pc1,pc2))

    cv2.imshow('左 双线性插值  右 双三次插值',imghstack)
    cv2.waitKey(0)



    cv2.imwrite('pc1.png',pc1)
    cv2.imwrite('pc2.png', pc2)

def main():
    get_three_position()
    spin_img()
    pass

if __name__ == '__main__':
    # 记录每次的坐标
    a, b = [], []

    # 使用的图像
    img = cv2.imread(r'T:\imgs\XL3\hb.jpg')
    main()