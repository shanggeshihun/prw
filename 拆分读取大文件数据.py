# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:15:22 2019

@author: Administrator
"""

import pandas as pd
"""
chunksize是设定为None的，这个时候read_csv会把整个文件的数据读取到DataFrame中;
当chunksize被设置成数值的时候，read_csv就会迭代读取数据;
每次读取10条数据
"""

data=pd.read_csv(r"C:\Users\Administrator\Desktop\ex.csv",chunksize=10,header=None)
#type(chunk)==DataFrame
for chunk in data:
    print(chunk)
    print(type(chunk))
