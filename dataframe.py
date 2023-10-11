#空值替换
import pandas as pd
import numpy as np
dfnan=pd.DataFrame({'a':[1,np.NAN,np.NAN,2,5],'b':[6,7,9,np.NAN,10]})
dfnan['new']=dfnan['a']
dfnan['new'][pd.isnull(dfnan['a'])]=dfnan['b']
# 等价：查找null值
print(pd.isnull(dfnan['a']))
print(dfnan['a'].isnull())
print(dfnan)


# 空值所在行索引
lg_null_index=lg_df_temp.index[np.where(np.isnan(lg_df_temp))[0]].drop_duplicates()

