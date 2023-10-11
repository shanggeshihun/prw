# -*- coding: utf-8 -*-
#Python读取并写入csv文件
import csv
#读取csv文件方法1
csvFile=open(r'c:/users/administrator/desktop/prw/csvData.csv','r')
reader=csv.reader(csvFile)#返回的是迭代类型
data=[]
for item in reader:
    print(item)
    data.append(item)
print(data)
csvFile.close()

#读取csv文件方法2
with open(r'c:/users/administrator/desktop/prw/csvData.csv','r') as csvFile:
    reader2=csv.reader(csvFile)
    for item2 in reader2:
        print(item2)

#从列表写入csv文件
#设置newline，否则两行之间会空一行
data=['wo','shi','shui']
csvFile2=open(r'c:/users/administrator/desktop/prw/csvDataW.csv','w',newline='')
writer=csv.writer(csvFile2)
m=len(data)
for i in range(m):
    writer.writerow(data[i])
csvFile2.close()

#从字典写入csv文件
dic={'张三':123,'李四':456,'王五':789}
csvFile3=open(r'c:/users/administrator/desktop/prw/csvDataW1.csv','w',newline='')
writer=csv.writer(csvFile3)
for key in dic:
    writer.writerow([key,dic[key]])
csvFile3.close()