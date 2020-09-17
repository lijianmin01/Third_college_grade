# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:25:47 2019

@author: dell
"""

import cv2

# 1.获取本地摄像头 --folder_path 截取图片的存储目录
def get_img_from_camera_local(folder_path):
  cap = cv2.VideoCapture(0)
  i = 1
  while True:
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    print(str(i))
    
    #cv2.imwrite(folder_path + str(i) + '.jpg', frame) # 存储为图像
    if cv2.waitKey(1) == ord('e'):
        break
    i += 1
    
  cap.release()
  cv2.destroyAllWindows()
  
# 2.测试
if __name__ == '__main__':
  folder_path = 'E:\\'
  get_img_from_camera_local(folder_path)