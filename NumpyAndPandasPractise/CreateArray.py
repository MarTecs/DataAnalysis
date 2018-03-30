# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: Array的创建

import numpy as np


array = np.array([1,2,3,4,5,6], dtype=np.int64)
## 前面指定Python中的列表，后面指定Numpys所采用的的数据类型，如果没有指定，默认就是int64,有小数的话默认就是float64

print(array.ndim)           ## 打印Numpy中这个数据结构的维度
print(array.size)           ## 打印Numpy中这个数据结构的数字个数
print(array.dtype)          ## 打印Numpy中这个数据结构所采用的的数据类型


## 使用Numpy生成全部为0的矩阵
array_zero = np.zeros( (3,4), dtype=np.float32  )           ## 这里需要我们指定一个数据维度，数据类型可以选择指定
print(array_zero)
print(array_zero.dtype)


## 使用Numpy生成全部为1的矩阵
array_one = np.ones( (5,5) )
print(array_one)


## 使用Numpy生成近乎没有的矩阵，说是什么都没有其实近乎为0
array_approximateZero = np.empty( (2,2) )

print(array_approximateZero)

## 顺序生成一个矩阵

array_Order = np.arange(80, 90, 2)          ### 类似于Python自己的range() ，第一个是开始值，第二个是结束值，但是不包括，最后一个是步长
print(array_Order)

## 生成一个指定行列的随机矩阵

array_OrderArray = np.arange(20).reshape(4,5)       ### 首先随机生成20以内的数字然后外形分割成4行5列的一个矩阵
print(array_OrderArray)


## 等间断生成一个数组
array_lineSpace = np.linspace(0, 9, 4)      ## 将分成4个数字，也就是3段，每段间距为3，最开始0，结束为9
print(array_lineSpace)