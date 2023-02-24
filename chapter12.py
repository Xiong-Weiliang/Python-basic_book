# TODO 异常处理
# 通过open('abc.txt')用于打开一个文件. 如果不存在就出现OSError下的FileNotExistError.
# 通过input（）函数从控制台读取字符串，
# i=input('please input number:')    #这里如果输入0会报错ZeroDivisionError: division by zero
# print(5/int(i))
# Python 中异常根类是BaseException，其子类Exception 是非系统退出的异常，异常类命名主要的后级有Exception 、Error和Warning
'''常见异常如下：
AttributeError 异常: 访问一个类中不存在的成员
OSError： 是操作系统相关异常，包括输入输出异常，文件未找到FileNotFoundError 异常属于此类
IndexError 异常是访问序列元素时，下标索引超出取值范围所引发的异常。
KeyError 异常是试图访问字典里不存在的键时而引发的异常。
NameError 是试图使用一个不存在的变量而引发的异常
TypeError 是试图传入变量类型与要求的不符合时而引发的异常。
ValueError 异常是由于传入一个无效的参数值而引发的异常。
当捕获的多个异常类之间存在父子关系时，捕获异常顺序与except 代码块的顺序有关。从上到下先写捕获的子类， 后写捕获的父类， 否则子类捕获不到。
'''
# 捕获异常是通过try-except 语句实现的，结构如下
# try
#     <可能异常的语句>
# except  #  可以同时使用多个语句
#     <处理异常>
# import datetime as dt   #  内置的时间模块
# import traceback as tb
# def read_date(in_data):
#     try:
#         date=dt.datetime.strptime(in_data,'%Y-%m-%d')  #  strptime()函数的作用为将in_data转化为标准的时间格式.
#         return date
#     except (ValueError,OSError) as e:  # 使用元组进行多重异常捕获   # 获得异常对象(多重捕获), 赋值给e值, 然后, 可以将print()打印出来.
#         print('处理ValueError异常')
#         tb.print_exc()  #  打印堆栈信息 (操作窗口显示为红色的地方.)
#         # print(e)  # 这里会报错。unconverted data remains: -00，即错误的地方
#     finally:
#         print("final处理")  #这里一般显示为某种文件的关闭或者内存的清理文件.
# str_data = '2018-8-18-1'
# print('日期={0}'.format(read_date(str_data)))
''' 
几个文件读取的函数 open()打开文件读取字符串，read()从文件中读取数据。
strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
try-except 不仅可以嵌套在try 代码块中，还可以嵌套在except代码块或finally代码块'''
#  假如多个异常以同一个方式处理，可以把这些异常放到一个元组中，然后一起判定。这样写的时候只要保证最高级的父类被写了就可以

#  从程序员的角度需要知道更加详细的异常信息时，可以打印堆栈跟踪信息。用print_exc()实现：
#  格式traceback.print_exc(limit=None, file=None, chain=True) 参数:限制堆栈个数；判断是否输出堆栈跟踪信息到文件（默认为None）。
''''''
#  try-except =语句后面还可以跟有一个finally 代码块，以及使用else语句。
# 注意：所有可以自动管理的资源，需要实现上下文管理协议（ Context Management Protocol ） 。
# 为了自动管理资源，可以在try中使用with as语句或者finally, 对于finally, 无论try还是except怎么运行, finally后面跟上的释放资源始终可以实现.
# 至此而不需要使用finally代码。自动释放资源
'''自定义异常类，需要继承exception类或其子类'''  # 自定义异常：只需要提供一个字符串参数的构造方法就可以了。
# class MyException(Exception):
#     def __init__(self,message):     #message 异常描述信息
#         super().__init__(message)   #调用父类的构造方法
'''可以显式抛出异常 使用raise语句，在其他的异常处理中那个人为raise到自己的定义异常之中。'''
# 注意： raise 显式抛出的异常与系统生成并抛出的异常在处理方式上没有区别，就是两种方法，要么捕获自己处理，要么抛出给上层调用者
'''显式抛出异常'''
import datetime as dt
class MyExpception(Exception):
    def __int__(self, message):
        super().__int__(message)
def read_data_from_file(filename):
    try:
        file = open(filename)
        in_data = file.read()
        n_data = in_data.strip()  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        date = dt.datetime.strptime(n_data,'%Y-%m-%d')       #必须移除之后, 才能匹配格式, data.txt位于同一文件夹之下.
        return date
    except ValueError as e:
        raise MyExpception('It isn\'t a reliable data')
    except FileExistsError as e:
        raise MyExpception('Not such a file')
    except OSError as e:
        raise MyExpception('There is a OS system error')
date = read_data_from_file('data.txt')
print('data={0}'.format(date))
#  raise 的异常抛出处理机制和系统自身的机制没有区别, 就是要么自己处理, 要么抛出给上层调用者.
