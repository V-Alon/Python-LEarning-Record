import numpy as np
import matplotlib.pyplot as plt
#读取图片
n1=plt.imread('baidu.png')
print(n1,type(n1))#三维数组，最高维度表示图像的高后面是宽，最低维颜色
plt.imshow(n1)
#编写一个灰度公式
n2=np.array([0.299,0.587,0.114])
#将n1和n2点乘
x=np.dot(n1,n2)
#传入数组解释灰度
plt.imshow(x,cmap='gray')
#显示图形
plt.show()

