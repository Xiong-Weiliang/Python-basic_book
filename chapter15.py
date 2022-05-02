# TODO Chapter15 文件操作与管理
# 以及如何读写文本文件和二进制文件。最后还详细介绍了OS和OS.path 模块。
''' 在Python 语言中对文件的读写是通过文件对象(file object)实现的。Python 的文件对象也称为类似文件对象
file-like object）或流（ stream）.Python 提供一种类似于文件操作的API如read() or write()实现对底层资源的访问。
'''
# 文件对象可以通过open()函数获得。open(file, mode ='r', buffering=- 1, encoding=None , errors=None , newline=None , closefd=True , opener=None)
'''参数： 文件，读写模式，缓冲区参数，文件编码，错误处理，是否关闭文件时的描述文件，加工操作（文件描述符）
提示：文件描述符是一个整数值，它对应到当前程序已经打开的一个文件。例如标准输入文件描述符是0 ，标准输出文件描述符是l ，标准错误文件描述符是2 ，
打开其他文件的文件描述符依次是3 、4 、5 等数字。示例如下：'''
# f=open('test.txt','w+')    # 在无文件下会增加该文件
# f.write('World the first')
# f=open('test.txt','r+')   #会覆盖文件内容(仅仅覆盖的是对应位置的)
# f.write('Second')
# f=open('test.txt','a+')   #会末尾增加文件内容
# f.write('third')
# 调用文件对象的close（）方法关闭为文件，close（）方法应该放在异常处理的finally的代码块中
# 但笔者更推荐使用with as代码块进行自动资源管理。
# f_name='test.txt'
# with open(f_name,'r') as f:
#     content=f.read()
#     print(content)
# with as 的基本思想是with所求值的对象必须有一个enter()方法，一个exit()方法。紧跟with后面的语句被求值后，返回对象的enter()方法被调用，
# 这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的exit()方法。
'''文本文件读写方法：
read (size=-1) 读取字符串，size 限制最多读取的字符数，size=-1 时没有限制，
readline (size=1):读取到换行符或文件尾并返回单行字符串，如果己经到文件尾。
readlines (hint= 1 ）： 读取文件数据到一个字符串列表中，hint为行数，-1时无限制
write(s）：将字符串s 写入文件，并返回写入的字符数。
writelines(lines）：向文件中写入一个列表，不添加行分隔符，因此通常为每一行末尾提供行分隔符。
flush(): 刷新写缓冲区，数据会写入到文件。
'''
# f_name = 'test.txt'   # test.txt 文件采用utf-8编码,需要指定
# with open(f_name,'r',encoding='utf-8') as f:
#     lines=f.readlines()         #读取方法与写入方法相对应
#     print(lines)
#     copy_f_name='copy.txt'
#     with open(copy_f_name,'w',encoding='utf-8') as copy_f:
#         copy_f.writelines(lines)
#         print("copy success")
#  Python 对文件的操作是通过文件对象实现的，文件对象属于Python 的io 模块
#  Python程序管理文件或目录，如删除文件、修改文件名、创建目录、删除目录和遍历目录等，可以通过Python的OS模块实现
'''
• os.rename(src,dst）： 修改文件名，src是源文件,dst是目标文件.
remove() 文件移除
rmdir 删除目录
walk() 遍历 自顶向下遍历目录树， 返回值是一个三元组（目录路径，目录名列表，文件名列表〉。
listdir(dir)  列出指定目录中的文件和子目录
curdir 获得当前目录
pardir 获得当前父目录
'''
import os
f_name = 'test.txt'
copy_f_name = 'copy.txt'
with open(f_name,'r')as f:
    b=f.read()
    with open(copy_f_name,'w') as copy_f:
        copy_f.write(b)
try:
    os.rename(copy_f_name,'Copy_2.txt')
except OSError('copy,txt'):
    print(os.listdir(os.curdir))    # 获得当前目录，
    print(os.listdir(os.pardir))    # 获得当前父目录
try:
    os.mkdir('subdir')
except OSError:
    os.rmdir('subdir')
for item in os.walk('.'):   #  返回当前目录树下所有目录和文件
    print(item)
# Python 提供的OS.path 模块提供对路径、目录和文件等进行管理的函数。
#对于文件和目录的操作往往需要路径， Python 提供的OS. p ath 模块提供对路径、目录和文件进行管理的函数
'''
os.path.abspath(path): 返回path 的绝对路径。
basename(path): 返回path路径的基础名部分,如果path指向的是一个文件，则返回文件名；如果path 指向的是一个目录，则返回最后目录名。
dirname(path): 返回path路径中目录部分。
exists(path): 判断path文件是否存在。
isfile(path）： 如果path 是文件，则返回True 。
isdir(path）：如果path 是目录，则返回True 。
getatime(path）：返回最后一次的访问时间，
getmtime(path）： 返回最后修改时间，
path.getctime(path） ： 返回创建时间，
getsize(path） ：返回文件大小，以字节为单位
'''
