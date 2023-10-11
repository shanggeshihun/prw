# -*- coding: utf-8 -*-
#pandas.read_excel详解
import pandas as pd
import numpy as np
filefullpath=r'c:/users/administrator/desktop/prw/1.xls'
df=pd.read_excel(filefullpath,skiprow=[0])
#df=pd.read_excel(filefullpath,sheetname=[0,2],skiprows=[0])
#sheetname指定为读取几个sheet，sheet数目从0开始
#如果sheetname=[0,2],那代表读取第0页和第2页的sheet
#skiprows=[0]代表读取跳过的行数第0行，不写代表不跳过标题
#df=pd.read_excel(filefullpath,sheetname=None,skiprows=[0])
print(df)

df1=pd.read_excel(filefullpath,sheetname=[0,1],skiprow=[0])
print(df1,'\n',df1[0],'\n',df1[1])
print(type(df1),'\n',type(df1[0]))
df11=df1[1]
print(df11.iloc[:,1])