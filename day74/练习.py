#coding=utf-8
import numpy as np

UK_path='UK_video_data.csv'
US_path='US_video_data.csv'

#加载国家数据
us_data=np.loadtxt(US_path,delimiter=',',dtype=int)
uk_data=np.loadtxt(UK_path,delimiter=',',dtype=int)

#添加归家信息
#构造全为零的数据
zero_data=np.zeros((us_data.shape[0],1)).astype(int)
ones_data=np.ones((us_data.shape[0],1)).astype(int)

#分别添加一列全为0,1的数组
us_data=np.hstack([us_data,zero_data])#us为0标识
uk_data=np.hstack([uk_data,ones_data])#uk为1标识

#拼接两组数据
final_data=np.vstack([us_data,uk_data])
print(final_data)
