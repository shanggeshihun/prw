#f=open(r'c:/users/administrator/desktop/test.txt','r')#r表示文本文件，rb是二进制文件，如果文件不存在即IOError
#f.close()
#为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

with open(r'c:/users/administrator/desktop/prw/test.txt','r') as f:
    print(f.read())
#read()读取整个文件，read(size)读取size个字节
with open(r'c:/users/administrator/desktop/prw/test.txt','r') as f:
    print(f.read(1))

#readlines() 读取整个文件，自动将文件内容分析成一个行的列表
with open(r'c:/users/administrator/desktop/prw/test.txt','r') as f:
    print(f.readlines(),type(f.readlines()))
    
#readline()每次只读取一行，通常比readlines()慢的多，仅当没有足够内存可以一次读取整个文件时，才应该使用readline()

#注意read(),readlines(),readline()把每行末尾的'\n'也读出来了，需要我们手动去掉
with open(r'c:/users/administrator/desktop/prw/test.txt','r') as f:
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip('\n')
print(lst)

