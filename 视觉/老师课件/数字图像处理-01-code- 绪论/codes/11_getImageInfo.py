# -*- coding: utf-8 -*-
"""
用照片讲故事
"""
import exifread
myFile="QQ图片20200916055457.jpg"

f=open(myFile,'rb')
tags = exifread.process_file(f)
f.close()
print(tags['Image ImageWidth'])  # 获取图片宽度信息
print(tags['Image Orientation']) # 照片拍摄方向
#print(tags['GPSLatitude'])      # 获取拍摄者位置纬度  
#print(tags['GPS GPSLongitude'])  # 获取拍摄者位置经度
print(tags['Image DateTime'])    # 照片拍摄时间