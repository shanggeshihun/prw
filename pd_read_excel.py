# -*- coding: utf-8 -*-
import pandas as pd
data=pd.read_excel(r'c:/users/administrator/desktop/prw/test.xlsx',sheetname='Sheet1')
print(data)
print(data.iloc[:,1:2])