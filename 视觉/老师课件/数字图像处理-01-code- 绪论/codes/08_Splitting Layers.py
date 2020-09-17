# 目标：读取彩色图像，可视化三个不同的颜色通道

# 0.导入必要的模块
import imageio
import numpy as np
import matplotlib.pyplot as plt

# 1.读取当前文件夹下一幅彩色图像
pic = imageio.imread('demo_2.jpg')

# 2.创建一个指定大小的窗口对象，将其划分为1行*3列布局的3个轴对象
fig, ax = plt.subplots(nrows = 1, ncols=3, figsize=(30,10))

# 3.设置可视化内容
for c, ax in zip(range(3), ax):
    
    # (1)create zero matrix，'dtype' by default: 'numpy.float64'
    split_img = np.zeros(pic.shape, dtype="uint8") 
    
    # (2)保持其余两个通道为0，assing each channel 
    split_img[ :, :, c] = pic[ :, :, c]
    
    # (3)display each channel
    ax.imshow(split_img)
    ax.set_xticks([])
    ax.set_yticks([])

# 4.保存效果图、可视化    
plt.savefig('08_three channels.png')
plt.savefig('08_three channels.pdf')
plt.show()