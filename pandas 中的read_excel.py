# -*- coding: utf-8 -*-
#pandas 中的read_excel
import pandas as pd
df=pd.read_excel(r'c:/users/administrator/desktop/prw/log.xls',sheetname=0)
#sheetname从0开始
print(df.dtypes)
#提取出每个"回执名单"多次出现的最后一行数据
new_df=df.drop_duplicates(subset='回执名单',keep='last')
print(df,'\n',new_df)
#out没有创建时自动新建
out=pd.ExcelWriter(r'c:/users/administrator/desktop/prw/output_log.xls')
new_df.to_excel(out)
out.save()


# 字段名重命名
volumn_merge_final.rename(columns={'order_pay_x':'order_pay'}, inplace = True)