#基于scikit-image 实现图像的读取、显示、转存、信息可视化

from skimage import io, color 
from skimage import data

# 1.Read image
img = io.imread('image2.png')
print('\n1--shape of the orginal image:',img.shape)
print('img type: ',type(img), ', number of pixles = ',img.size)  
io.imshow(img)
io.show()


# 2.Write an image to a file 
io.imsave('new_image2.bmp', img)


# 3.Convert the image to grayscale
gray_image = color.rgb2gray(img)
print('\n2--shape of the converted gray image:',gray_image.shape)
io.imshow(gray_image)
io.show()

# 4.Convert the image from RGB to HSV
hsv_image = color.rgb2hsv(img)
print('\n3--shape of the converted hsv image:',hsv_image.shape)
io.imshow(hsv_image)
io.imsave('new_image2_hsv.jpg',hsv_image)
io.show()


# 5.Get the camera image 
img_camera = data.camera()
print('\n4--shape of the cameraman image:',img_camera.shape)
print('max=%.5f, min=%.5f, mean=%.5f '% (img_camera.max(), img_camera.min(), img_camera.mean()) ) 
io.imshow(img_camera)
