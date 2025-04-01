import pandas as pd
import matplotlib.pyplot as plt
#读取Excel文件
df=pd.read_excel('JD手机销售数据.xlsx')
# print(df)
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
#设置画布大小
plt.figure(figsize=(10,6))
labels=df['商品名称']
y=df['北京出库销量']
# print(labels)
# print(y)
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
#设置xy轴
plt.axis('equal')
plt.title('2077北京各品牌手机出库占比图')
plt.show()