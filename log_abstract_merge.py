s="""
2018-12-04 00:00:46,726 [http-nio-8167-exec-436] 1112743 DEBUG [com.sijibao.bams.modules.sys.interceptor.LogInterceptor] - LOGID:1543852800798 计时结束：12:00:46.726  耗时：0:0:45.928  URI: /bams/a/pres/certify/vehicleCertify/list  最大内存: 7166m  已分配内存: 4199m  已分配内存中的剩余空间: 3419m  最大可用内存: 6386m
2018-12-04 00:00:46,726 [http-nio-81
"""
#lst=re.findall(r'LOGIND:(\d+)\s+计时结束：(.*?)\s+耗时：(.*?)\s+URI:\s+(.*?)\s+',s)
# -*- coding: utf-8 -*-
import re
import pandas as pd 

def readInChunks(fileObj, chunkSize=20971520):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 4kB.
    """
    while 1:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

f=open(r'C:\Users\dell\Desktop\bams_2018-12-04.log\bams_2018-12-04.log','r',encoding='utf-8')
i=0
logid_1=[]
count_over=[]
waste=[]
url=[]
max_memory=[]
already_memory=[]
already_rest_memory=[]
max_avali=[]

logid_2=[]
count_start=[]
for chuck in readInChunks(f):
    lst_1=re.findall('LOGID:\s*(\d+)\s*计时结束：\s*(.*?)\s*耗时：(.*?)\s*URI:\s*(.*?)\s*最大内存:\s*(.*?)\s*已分配内存:\s(.*?)\s*已分配内存中的剩余空间:\s(.*?)\s*最大可用内存:\s*(.*?)\s+',chuck)
    lst_2=re.findall('LOGID:\s*(\d+)\s*开始计时:\s*(.*?)\s*URI:\s*(.*?)\s*\d+',chuck)
    
    for log_dic_1 in lst_1:
        logid_1.append(log_dic_1[0])
        count_over.append(log_dic_1[1])
        waste.append(log_dic_1[2])
        url.append(log_dic_1[3])
        max_memory.append(log_dic_1[4])
        already_memory.append(log_dic_1[5])
        already_rest_memory.append(log_dic_1[6])
        max_avali.append(log_dic_1[7])
        i+=1
        print(log_dic_1)
        print(i)
        
    for log_dic_2 in lst_2:
        logid_2.append(log_dic_2[0])
        count_start.append(log_dic_2[1])

print(logid_1)
print(count_over)
print(logid_2)

c_1={'logid_1':logid_1,
   'count_over':count_over,
   'waste':waste,
   'url':url,
   'max_memory':max_memory,
   'already_memory':already_memory,
   'already_rest_memory':already_rest_memory,
   'max_avali':max_avali
   }
c_2={'logid_2':logid_2,
   'count_start':count_start}

df_1=pd.DataFrame(c_1)
df_2=pd.DataFrame(c_2)

df_1=df_1[['logid_1','count_over','waste','url','max_memory','already_memory','already_rest_memory','max_avali']]

df_2=df_2[['logid_2','count_start']]

df_merge=df_1.merge(df_2,left_on ='logid_1',right_on = 'logid_2',how = 'inner')

writer_1=pd.ExcelWriter(r'C:\Users\dell\Desktop\df_1.xlsx')
writer_2=pd.ExcelWriter(r'C:\Users\dell\Desktop\df_2.xlsx')
writer=pd.ExcelWriter(r'C:\Users\dell\Desktop\pd_merge.xlsx')

df_1.to_excel(writer_1,'Sheet1')
df_2.to_excel(writer_2,'Sheet1')
df_merge.to_excel(writer,'Sheet1')
f.close()