s="""
2018-12-04 00:00:46,726 [http-nio-8167-exec-436] 1112743 DEBUG [com.sijibao.bams.modules.sys.interceptor.LogInterceptor] - LOGID:1543852800798 计时结束：12:00:46.726  耗时：0:0:45.928  URI: /bams/a/pres/certify/vehicleCertify/list  最大内存: 7166m  已分配内存: 4199m  已分配内存中的剩余空间: 3419m  最大可用内存: 6386m
2018-12-04 00:00:46,726 [http-nio-81
"""
#lst=re.findall(r'LOGIND:(\d+)\s+计时结束：(.*?)\s+耗时：(.*?)\s+URI:\s+(.*?)\s+',s)
# -*- coding: utf-8 -*-
import re
import pandas as pd 

def readInChunks(fileObj, chunkSize=1024*1024*20):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 4kB.
    chunkSize=20M
    """
    while 1:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data

f=open(r'C:\Users\dell\Desktop\bams_2018-12-04.log\bams_2018-12-04.log','r',encoding='utf-8')
i=0
logid=[]
count_over=[]
waste=[]
url=[]
max_memory=[]
already_memory=[]
already_rest_memory=[]
max_avali=[]
for chuck in readInChunks(f):
    lst=re.findall('LOGID:\s*(\d+)\s*计时结束：\s*(.*?)\s*耗时：(.*?)\s*URI:\s*(.*?)\s*最大内存:\s*(.*?)\s*已分配内存:\s(.*?)\s*已分配内存中的剩余空间:\s(.*?)\s*最大可用内存:\s*(.*?)\s+',chuck)
    for log_dic in lst:
        logid.append(log_dic[0])
        count_over.append(log_dic[1])
        waste.append(log_dic[2])
        url.append(log_dic[3])
        max_memory.append(log_dic[4])
        already_memory.append(log_dic[5])
        already_rest_memory.append(log_dic[6])
        max_avali.append(log_dic[7])
        i+=1
        print(log_dic)
        print(i)
print(logid)
print(count_over)
c={'logid':logid,
   'count_over':count_over,
   'waste':waste,
   'url':url,
   'max_memory':max_memory,
   'already_memory':already_memory,
   'already_rest_memory':already_rest_memory,
   'max_avali':max_avali
   }
df=pd.DataFrame(c)
df=df[['logid','count_over','waste','url','max_memory','already_memory','already_rest_memory','max_avali']]
writer=pd.ExcelWriter(r'C:\Users\dell\Desktop\pd_1.xlsx')
df.to_excel(writer,'Sheet1')
f.close()