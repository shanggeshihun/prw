# -*- coding: utf-8 -*-
#Python pandas读取excel文件时候如果读取指定的col
import pandas as pd
df=pd.DataFrame({'A':[1,2,3],'B':['foo','bar','baz']})
#没有创建pd.ExcelWriter也写入成功了
df.to_excel(r'c:/users/administrator/desktop/prw/tt.xlsx')
print(pd.read_excel(r'c:/users/administrator/desktop/prw/tt.xlsx'))
#给列重命名
print(pd.read_excel(r'c:/users/administrator/desktop/prw/tt.xlsx',names=['B','A']))