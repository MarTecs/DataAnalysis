# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 讲解Numpy的属性


import numpy as np

## 命名一个矩阵
a = [[1,2,3],[4,5,6]]   ## A list of Python
array = np.array(a)     ## 将Python中的列表转换为矩阵


print(type(a))
print(type(array))

print("number of dim：", array.ndim)     ## 输出Array的Dimension
print("shape：", array.shape)            ## 输出Array的Shape    也就是几行几列
print("size：", array.size)              ## 输出Array的size     也就是元素的个数