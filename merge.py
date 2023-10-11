import pandas as pd
import numpy as np
#左右连接字段不相同，则均保留
df1=pd.DataFrame({'A1':[1,2,3,5,6,8],'B':np.random.randint(1,10,6)})
df2=pd.DataFrame({'A2':[4,2,7,5,9,28],'B':np.random.randint(1,10,6)})
merge=pd.merge(df1,df2,left_on='A1',right_on='A2',how='left')

#左右连接字段相同，则只保留左边
df3=pd.DataFrame({'A':[1,2,3,5,6,8],'B':np.random.randint(1,10,6)})
df4=pd.DataFrame({'A':[4,2,7,5,9,28],'B':np.random.randint(1,10,6)})
merge34=pd.merge(df3,df4,left_on='A',right_on='A',how='left')
print(merge34)