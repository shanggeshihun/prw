# -*- coding: utf-8 -*-
#写文件和读文件唯一的区别是调用open函数时，传入标识符w或者wb表示写文本文件或者写二进制文件
f=open(r'c:/users/administrator/desktop/prw/test_w.txt','w')
f.write('hello world')
f.close()
#w如果没有这个文件就创建一个，如果有就会先把原有的内容清空在写入新的东西；a表示不清空而是追加
f=open(r'c:/users/administrator/desktop/prw/test_w.txt','w')
f.write('hi world')
f.close()

f=open(r'c:/users/administrator/desktop/prw/test_w.txt','a')
f.write('add hello world')
f.close()

#with语句保险
with open(r'c:/users/administrator/desktop/prw/test_w.txt','a') as f:
    f.write('with write')

#python文件对象提供了两个写方法 write  writelines()、writelines()针对列表的操作，换行符不会自动加入
    f.writelines(['1','2','3'])
    f.write('\n')
    f.writelines(['4\n','5\n','6\n'])

with open(r'c:/users/administrator/desktop/prw/test_w.txt','r',encoding='gbk',errors='ignore') as f:
    
