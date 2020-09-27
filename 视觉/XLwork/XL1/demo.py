import os
from skimage import io
import fnmatch


# 在给定的文件夹中，获取不同格式的图像文件列表；
def get_imgs_list(path):
    png_list = []
    jpg_list = []
    bmp_list = []
    gif_list = []
    tif_list = []
    # 依次匹配对应的文件
    png_list = [file for file in os.listdir(path) if fnmatch.fnmatch(file, '*.png')]
    jpg_list = [file for file in os.listdir(path) if fnmatch.fnmatch(file, '*.jpg')]
    bmp_list = [file for file in os.listdir(path) if fnmatch.fnmatch(file, '*.bmp')]
    gif_list = [file for file in os.listdir(path) if fnmatch.fnmatch(file, '*.gif')]
    tif_list = [file for file in os.listdir(path) if fnmatch.fnmatch(file, '*.tif')]

    # imgs_list
    imgs_list = {}
    if(len(png_list)!=0):
        imgs_list['png']=png_list
    if (len(jpg_list)!=0):
        imgs_list['jpg']=jpg_list
    if (len(bmp_list)!=0):
        imgs_list['bmp']=bmp_list
    if (len(gif_list)!=0):
        imgs_list['gif']=gif_list
    if (len(tif_list)!=0):
        imgs_list['tif']=tif_list

    return imgs_list

#  顺次读取文件列表中每个文件名对应的图像文件，
#  获取该图像的行数、列数、颜色通道数，显示该图像，
#  并转存成其它格式的图像文件。
def read_save_img(list,path):
    for key in list.keys():
        print(str(key)+'类型的图像信息如下：')
        for img_name in list[key]:
            show_img(path+'/'+img_name)

    pass

# 显示图片,并打印该图像的行数、列数、颜色通道数
def show_img(path):
    img = io.imread(path)
    print("{}==>行数：{} ，列数：{}，颜色通道数：{}".format(os.path.basename(path),img.shape[1],img.shape[0],img.shape[2]))
    io.imshow(img)
    io.show()
    # 将图片统一保存为png格式
    io.imsave('./save_imgs/'+os.path.basename(path)[:-4]+'.png',img)

def main():
    path = r'./imgs'
    img_lists=get_imgs_list(path)
    # 打印文件列表
    for k in img_lists.keys():
        print(str(k)+"图像文件列表")
        print(img_lists[k])
    # 创建保存转存成其它格式的图像文件
    if not os.path.exists('./save_imgs'):
        os.mkdir('./save_imgs')
    read_save_img(img_lists,path)

    pass

if __name__ == '__main__':
    main()