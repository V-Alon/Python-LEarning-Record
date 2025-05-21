import numpy as np
'''

max

'''
# 创建一个一维数组
arr1d = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
max_index_1d = np.argmax(arr1d)
print("一维数组最大值的索引：", max_index_1d)  # 输出：5

# 创建一个二维数组
arr2d = np.array([[7, 2, 9],
                  [4, 6, 3],
                  [8, 1, 5]])

# 不指定axis时，将数组展平为一维数组后查找索引
max_index_flat = np.argmax(arr2d)
print("二维数组展平后的最大值索引：", max_index_flat)  # 输出：2

# 沿着行的方向（axis=0）查找每列的最大值索引
max_indices_axis0 = np.argmax(arr2d, axis=0)
print("每列最大值的索引：", max_indices_axis0)  # 输出：[2 1 0]

# 沿着列的方向（axis=1）查找每行的最大值索引
max_indices_axis1 = np.argmax(arr2d, axis=1)
print("每行最大值的索引：", max_indices_axis1)  # 输出：[2 1 0]





'''

min

'''
import numpy as np




# 创建一个一维数组
arr1d = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
min_index_1d = np.argmin(arr1d)
print("一维数组最小值的索引：", min_index_1d)  # 输出：1




# 创建一个二维数组
arr2d = np.array([[7, 2, 9],
                  [4, 6, 3],
                  [8, 1, 5]])



# 不指定axis时，将数组展平为一维数组后查找索引
min_index_flat = np.argmin(arr2d)
print("二维数组展平后的最小值索引：", min_index_flat)  # 输出：7



# 沿着行的方向（axis=0）查找每列的最小值索引
min_indices_axis0 = np.argmin(arr2d, axis=0)
print("每列最小值的索引：", min_indices_axis0)  # 输出：[1 2 1]



# 沿着列的方向（axis=1）查找每行的最小值索引
min_indices_axis1 = np.argmin(arr2d, axis=1)
print("每行最小值的索引：", min_indices_axis1)  # 输出：[1 2 1]