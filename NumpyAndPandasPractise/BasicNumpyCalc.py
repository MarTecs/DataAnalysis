# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: Numpy基础运算

import numpy as np

## 首先创建Numpy的两个矩阵
array_NewArray = np.arange(10)                          ### 将会生成0-9的数字填充在Numpy的矩阵中
array_NewArray2 = np.array([1,2,3,4,5,6,7,8,9,10])


## 两个矩阵进行计算并进行打印
print(array_NewArray, array_NewArray2)
print(array_NewArray * np.sin(array_NewArray2))
print(array_NewArray * np.tan(array_NewArray2))
print(array_NewArray * array_NewArray2)

print(array_NewArray < 10)          ### 将会对矩阵中的每个数字进行判断，然后组成一个bool类型的矩阵进行返回

## 新建两个矩阵
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])

print(array1 * array2)

### 返回矩阵间乘法的结果
print(np.dot(array1 , array2))
#####等价于下面的表达
print(array1.dot(array2))


## 新生成一个Array
array3 = np.random.random((2,4))        ### 第1个random因为是Numpy的模块之一，后面是给定一个维度
print(array3)
print(np.max(array3, axis=1))       ###求出生成的矩阵中每1行的最大值，
print(np.max(array3, axis=0))       ###求出生成的矩阵中每1列的最大值
print(np.max(array3))
print(np.min(array3))
print(np.sum(array3))



