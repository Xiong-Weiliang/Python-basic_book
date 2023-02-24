# TODO Chapter1-2:
# 使用import this输入运行进行puthon之禅的查看。一段文本代码。
import this
# 特点：简单易学，面向对象，解释性，免费开源，胶水语言，丰富的库，强制缩进的规范代码，函数编程，提供了函数式编程的支持，如函数类型、Lambda 表达式、高阶函数和匿名函数等。动态类型。
# 应用：高级语言，无法进行硬件访问(类似于Java)，应用于应用开发，web应用，自动化，科学计算和数据可视化，网络爬虫urllib，Selenium BeautifulSoup 等，还有网络爬虫框架scrapy。
# 人工智能和大数据Hadoop，Spark，游戏开发Pygame 、Pyglet 和 Cocos2d
# website：对于一个初学者必须要熟悉如下几个Python 相关网址：
# • Python 标准库： https://docs.python.org/3/1ibrary/index.htmI
# • Python HOWTO: https://docs.python.org/3/howto/index.html
# • Python 教程： https://docs.python.org/3/tutorial/index.html
# • PEP 规范①： https://www.python.org/dev/peps/  （技术文档规范）
# Window下的默认字符集是 GBK, 但是 Linux 和 masOS的是UTF-8, 导致可能会出现乱码.
# 运行程序可以使用python XXX.py

# TODO Chapter 3
# Python运行方式：交互式，文本式两种。
# 交互式时，可以直接在Anaconda里面输入python即可。 用 windows porompt命令可能不行，除非另外安装了IDLE。
# 注意与C++不同，python不需要主函数
# print('Hello world')  #注意单引号和双引号都可以，但是如果字符串内部有引号，可以外部双引号，内部双引号
# str='Hello, Doctor Klaus'
# print(str);     #句尾分号有没有没差别，但是用分号的话一行可以多条语句;
'''
print('Hello world')    #print函数有五个输入值，对象，分隔符，结束字符，输出参数，是否刷新缓冲区（刷新直接当前位置输出）
'''    #三重单引号或者双引号注释
# 快捷键 F5 copy；shift+F10 run；Ctrl+/ 批量行注释；

# TODO Chapter 4
# 介绍python 中一些最基础的语法，其中包括标识符、关键字、常量、变量、表达式、语句、注释、模块和包等内容。
# 1.标识符就是变量、常量、函数、属性、类、模块和包等由程序员指定的名字。
# python共计33个关键词，False,None,True 大写，其余全部小写。注意Python无法定义常量值.
# coding=utf-8 用于设定编码格式，必须放在前两行才有效。 注意尽管是以注释出现, 但是不是注释, 会有实际的影响.
# !/usr/bin/python 注释是用于在安装了多个python解释器时候做选择版本使用的.
# a=b=c=d=142  #支持链式赋值
# f=0
# 查看运行的变量名的方法： 右上角项目名点开，编辑配置，使用python控制台运行。
# 在if、for 和while 代码块的语句中，代码块不是通过大括号来界定的，而是通过缩进,e.g.
# if a>=154:
#     print('big')    #一个缩进级别一般是一个制表符（Tab）或4个空格，
# else:
#     print('small')
# print('判定结束')
# Python 中一个模块就是一个文件，模块是保存代码的最小单位，也就是.py文件为模块，模块中可以声明，以及互相调用。
# 实际上模块命名空间， 也称名字空间、名称空间等，它表示着一个标识符（ identifi e仆的可见范围
z=18
import module1
# from module1 import z
print(module1.z)   # 这中使用点的方法只导入目前模块没有的值特定的  #调用时必须严格按照其规范指定全局的唯一路径，否则直接报错。
# 在导入时优先保存之前的变量, 而不是新导入的包中的数据覆盖掉.
# 注意.pkg后缀的包只有专业版可以使用，社区版不能新建。用于新建的模块命名之间冲突，从而提供一个别名。
# pkg就是新建的“软件包”，可以放多个.py文件防止冲突.

# TODO Chapter 5
# 命名法：类名称使用大驼峰方法，变量名使用小写加下划线隔开，
# 注释有三种：单行，多行，文本注释。注释可以生成API帮助文档,使用pydoc提取这些信息, 也可以生成HTML文件.
# 一行代码中最多 79个字符， 对于文档注释和多行注释时一行最多72个字符, 包含URL 地址可以不受这个限制
# 备注：API（Application Programming Interface,应用程序编程接口）：是一些预先定义的函数，
#    目的是提供应用程序与开发人员基于某软件或硬件的以访问一组例程的能力，而又无需访问源码，或理解内部工作机制的细节。
#    API帮助文档就是对这些函数写的文档，帮助开发人员了解函数的使用方法和功能。
# 有些特殊的注释， 就是在代码中加一些标识，便于IDE 工具快速定位代码， TODO 注释就是其中的一种，注意必须得先要有#和空格，随后使用TODO触发
# import re 每一句道路语句只能道路一个模块，但from re import 1,2,3,可以接上多个元素
# 导入语句总是放在文件顶部，位于模块注释和文档注释之后，模块全局变量和常量之前。导入语句应该按照从通用到特殊的顺序分组， 顺序建议为： 标准库→ 第三方库→ 自己模块
# 有可能标准库中的模块有自己的顺序。
# 过长的语句可以直接在括号中断开，而无需使用换行符’\‘,有时候也直接人为加入括号去除换行符
#  方法就是通过对象 (类的实例化) 调用的函数.
# TODO Chapter 6
'''Python有6种标准数据类型：数字、字符串、列表、元组、集合和字典，而列表、元组、集合和字典可以保存多项数据， 它们每一个都是一种数据结构， 本书中把它们统称为“数据结构”类型。
Python 数字类型有4种： 整数类型、浮点类型、复数类型和布尔类型。
Python 3 不再区分整数和长整数，所有需要的整数都可以是长整数。int, 此外 Python 只支持双精度浮点类型，1e2=100（前面的1不可省略）
默认十进制，以ob 或者0B 开头，八进制和十六进制为 0o(0O)与0X(0x)
Python 中复数类型为complex ，例如1 + 2j 表示的是实部为l 、虚部为2 的复数。
Python 中布尔类型为bool, bool 是int 的子类，它只有两个值： True 和False 。通过函数bool()转化为bool类型。
  数据类型的转换：除complex之外，其他的三种数字类型（整数、浮点和布尔〉都可以互相进行转换，转换分为隐式类型转换和显式类型转换。 type()用于查看其类型。 隐式函数的转换为直接运算。显式转换函数分别是int（）、float（）和bool （） 函数
  字符串：python内部的字符串是有顺序的，从左到右， 索引从0 开始依次递增。Python 中字符串类型是str。
三种字符串类型：1. 普通的，使用（单/双）引号生成的；2. 原始字符串：在普通之前加上r，作用为特殊字符不需要转换而按照原来的面目显现。
             3. 长字符串：包含了换行缩进等排版字符，可以使用三重单引号’‘’或三重双引号“”“包裹起来，这就是长字符串。
Python 中的字符采用 Unicode 编码， 所以字符串可以包含中文等亚洲字符; 
  如果想在字符串中包含一些特殊的字符，例如换行符、制表符等， 在普通字符串中则需要转义，前面要加上反斜杠 \ 用于字符转义。
'''
# e.g.转义
print('Hello \n world')  #换行 转移字符将n变化为换行
print('Hello \' world')  #单引号 ，防止提前终止.
# 原始字符串
s=r'hello \n world'
print(s)     # 直接按照本来面目显现而没有控制效果,注意实际上是两个\出现.
# 长的字符串
longs='''hello1
hello2 \'   
hello3
'''        #也可使用双引号
print(longs)
# 将其他类型变量与字符串拼接到一起并进行格式化输出的情况。例如计算的金额需要保留小数点后四位， 数字需要右对齐等， 这些都需要格式化。
# 使用字符串带有的 format()进行格式化输入，即实现替换功能。注意那个format前面的点，例子如下
name1 = 'Klaus'
name2= 'Mike'
position='Doctor'
s='{0}的职位是{1}'.format(name1,position)
print(s)
s='{p}是{k}'.format(p=name2,k=position)   #指定名称替换
print(s)
a='Ab,{0}'
s=a.format(5)    # 注意这是可以分离写的。也就是说使用5的内容替代上面的{0}
print(s)
# 占位符中还可以有格式化控制符，对字符串的格式进行更加精准控制，此外如果只有一个需要格式化，{}内部可以去除，无歧义是正确的
money=1234.255461365156351
print("钱的数目为{0:6f}".format(money))    # 保留6位小数
print("钱的数目为{0:6.2f}".format(money))    # 一共保留6位(不含小数点)
print("钱的数目为{0:E}".format(money))    # 科学计数法
print('十进制数目{0:d}为十六进制{0:X}'.format(59))   # 十进制与十六进制的变化，注意浮点数不能用十六进制
"""
在给定的字符串中查找子字符串是比较常见的操作。字符串类（str）中提供了find 和rfind方法，返回值位置，没有找到返回-1.区别在于，rfind返回最右端的索引，find返回左端的。例子如下： 
"""
source_str = "There is a string accessing example" #注意str中空格也占据位置.
len(source_str)    # 测试字符串的长度，不可用于int类型的len()函数。
source_str.find('r',1,20)   # 起始和末尾编号，即搜索范围，第一个字符为0编号。空格也算一个位置
# 注释：函数与方法的区别是，方法(例如find())是定义在类中的函数，在类的外部调用时需要通过类或对象调用。而(顶层)函数(例如len())不在类中，直接可以调用。
# 总之方法也是一段代码，通过一个与对象相关联的名字来进行调用
# 字符和数值的转换,例子如下：
b=int('AC',16)  # 指定十六进制否则默认十进制AD不存在会报错的
# 打印出 b 会产生十进制效果
# 反向转换为str()函数,但是不提供格式化——可以附加的使用format函数。
# str(b)会将其转化为str变量, 一定要注意数据中不要有str名字的变量，不然会覆盖掉原有python自带的str()函数

# TODO Chapter 7
# 一些一维的算数符如下：
a = 100%12    # 取余数。此时为100=12*8+4 ，所以a的值为4
a = 12**3     # 取次方
a = 13//3     # 除法加向下取整数
# 字符串也可以使用 + 与 * 进行运算 # 效果为直接联结在后面而没有空格使用。
b='Xiong'
c=b+'Klaus'
d=c*2
#  比较操作符中的：不等号为!= ,可以对str对象进行比较，逻辑运算符号：not and or —— 都采用“短路”设计，提高其效率
c = 0x10110010
#元素移位。注意计算机64bit，因此会用0补齐的，或者说，低于64位的会自动前面用0补齐为64位.
print("c>>2={}".format(a>>2))   #如果计算机位数很低，那么会去除式移位，不会循环移位的
# 同于C++的简化符号，复制运算也可以简写。例如,c=c+10等价于
c+=10  # (Note:注意, 移位和计算机的bit有关, 64bit的和32bit的结果可能是不一样的. )
c=-0b1101 #二进制, 常识右移.(过程: 负数的原码已经给出, 其次使用补码(符号位补右移的位数), 移动, 补码返回).
print('c>>2={0}'.format(c>>2))
'''几个少用的赋值符号: %= 取余数. **=取幕 //=地板除法'''
#  其余的测试运算符如下 ，is, is not, 判定是否符合同一律,不同于==与!=是用于判定两个对象是不是一样的.一个关于类的较为复杂的例子如下
class Person:     # 注意类,if, else后面都有冒号
    def __init__(self, name, age):   #定义类的初始化函数
        self.name=name
        self.age=age
    def __eq__(self, other):  #重新定义等号'=='测定，使得后面为True，其余的符号操作类似
        if self.age==other.age and self.name==other.name:
            return True
        else: return False
p1=Person('Tony',18)   # 类的实例化
p2=Person('Klaus',23)
print(p1==p2) #False
print(p1!=p2) #True
p3=Person('Klaus',23)
print(p2==p3)    # 注意这里返回的是False,在希望获得相同的条件的情况下，需要人为定义其比较规则
# 用in 和 not in 判定元素属于与否
strx='abcdefghijklmn'
print('d' in strx)     # True
print('jc' in strx)    # 连续字符判定
# 优先级问题
'''运算符优先级大体从高到低是： 算术运算符→位运算特→关系运算符→逻辑运算符→赋值运算符'''

# TODO Chapter8
# if 和 else 的使用。例子如下
import sys  #  在下面的 Python 控制台中直接调用即可。
# “sys”即“system”，“系统”之意。该模块提供了一些接口，用于访问 Python 解释器自身使用和维护的变量，同时模块中还提供了一部分函数，可以与解释器进行比较深度的交互。
score= int(sys.argv[1])   # sys.argv能够读取命令行参数列,第一个为文件名(编号为0)，第二个参数为输入的参数(这里数目为1)
if score >= 85:     # TODO 这里似乎有问题.
    print("Excellent")
if score <= 85:
    print('unfoutunately')

# sys.byteorder字节序  little 的值
# sys.platform 平台  win32的值
# sys.executable  绝对路劲  值: 'D:\\Anaconda\\envs\\Xiong\\python.exe'
# sys.modules  包含模块到模块名的映射

# 除此之外还可以使用elif，这等于使用else if，一个例子如下
a=10
if a<1:
    print('a<1')
elif a>1 and a<5:      # 注意这里只会判定一个，判定两个必须使用and替代。类似的还有，not and or 一共三个
    print('a>1 and a<5')
else:
    print('a=10')

'''
#三元运算符，条件表达式的替代品如下： （优点在于具有返回值）  
result= 'great' if a>10 else "terrible"
print(result)
'''
# while 语句如下
a=0
while a<20 and a>1:    # 注意其缺陷：while 循环条件语句中只能写一个表达式， 而且是一个布尔型表达
    a=a+8
else:
    print(a)
#range()函数用于生成序列，range ([start , ] stop ( , step])，开始结尾步长三个参数。
# 可以将其使用于for之中 注意while和for 可以嵌套使用，包括if，只要控制好了逻辑即可
for i in range(1,21,4):   # 注意尾部的stop参数不算的
    print('{0}*{0}={1}'.format(i,i*i))
# python 有三个跳转语句，break, continue, return
# 23434 和 234_3_4 是等价的, 下划线不会影响数, 就是为了阅读方便.
a='hello Klaus'
for aa in a:   #字符串也可以作为范围对象.
    print('{0}'.format(aa))