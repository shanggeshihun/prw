# -*- coding: utf-8 -*-
"""
矩阵乘法
"""
import numpy as np
#np.dot 二维即矩阵乘法，一维即计算内积
array1=np.array([[1, 2, 3], [4, 5, 6]])
array2=np.array([[1, 2], [3, 4], [5, 6]])
arr_dot=np.dot(array1,array2)
arr_neiji=array1*array1
print(arr_dot)
print(arr_neiji)