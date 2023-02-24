# TODO Chapter13 常用模块math, random, datetime, logging
# coding=utf-8 注意编码仅仅在第一行注释有效.
'''  数学的 math 模块只能处理实数, 复数使用 cmath 进行操作.
math.ceil(a）和math.floor(a)用来返回大于或等于a的最小整数。
math.floor(a)返回小于或等于a的最大整数。
round()可以对a进行四舍五入计算。
math.log(a,b) a关于b的对数函数，即 math.log(8,2)=3.0
math.sqrt(a) 平方根
math.pow(a,b)  求a的b次幂
三角函数 sin,cos,tan,
反三角函数 asin，acos,atan
弧度和角度的转换函数 degrees radians   '''

''' # 随机的random模块  使用方法 random.randint(1,4)   
random()  [0,1]之间的随机浮点数
randrange(stop)  [0,stop]之间的整数型随机数
randrange(start,stop,step) 步长为step之间的随机整数
randint(a,b)  返回范围内的随机整数
'''
# import math
# import random
# print(math.sin(2))
# print(random.randrange(1,5,1))
# for i in range(1,15):
#     x=random.randrange(1,57)
#     print(x,end=';')     #随机产生数组应该使用numpy库,这样for太死板了.
# time和datetime模块
# time 为底层的C接口，严重依赖于硬件平台，而datetime对tine进行了高级的封装，主要有以下的几个类
'''
datatime：时间和日期
date: 日期
time：时间
timedelta:计算时间跨度
tzinfo：时区 (time zone information)
'''
# 使用时import datatime
# datatime类别实例的构建方法。      datetime.datetime(year,month,day,hour=O,minute=O,second=O,
#()如果超出了预设范围会抛出异常值       microsecond=O ,tzinfo=None)
# 建立一个新的时间如下
# import datetime
# dt=datetime.datetime(2018,2,28)    #注意只有闰年才有29
# print(dt)     # 打印出时间.
# dt=datetime.datetime.today()      # 返回当前时间和日期
# print(dt)  #输出2022-04-12 09:01:34.957512
'''类似的函数如下   #UTC 协调世界时间,它以原子时为基础，是时刻上尽量接近世界时的一种时间计量系统, 输入一个很大的秒数, 然后换算为当前标准时间.
# 注意以下可以直接用于实例化之上, 也可以使用datetime两次, 细节化模块. 
e.g. dt.utcnow()  或者使用datetime.datetime.utcnow()
datetime.now(tz=None)  返回本地当前的时间和日期，参数为None时候等价于Now()
datetime.utcnow()  返回当前UTC的时间和日期
datetime.fromtimestamp(timestamp) 返回与UNIX时间戳对应的本地日期和时间.
datetime.utcfromtimestamp(timestamp)：返回与UNIX时间戳对应的UTC日期和时间。
''' #：在Python 语言中时间戳单位是“秒”， 所以它会有小数部分。
# dt=datetime.datetime.utcfromtimestamp(99999999.999)
# print(str(dt))   # 其实用不用str无所谓 str的作用是将一个类变化为str,然后print()打印出,

''' 一个date对象可以表示日期等信息，构造方法和函数如下：
# datetime.date(year,month,day)  #三个参数是不能省略
# date.today()  #返回当前本地日期。
# date.fromtimestamp(timestamp）：返回与UNIX 时间戳对应的本地日期。'''
# 注意python中的时间单位是second, 所以出现小数部分是正常的.
# 一个time对象可以表示一天中的时间信息，data以天为单位, datatime就是天+具体时分秒..
# datetime.time (hour=0,minute=0,second=0,microsecond=0,tzinfo=None)
# 日期时间计算的方法，使用timedelta类，代表时间的变化。# 使用timedelta对象可以精确到微秒
# datetime.timedelta(days=0,seconds=0,microseconds=0,milliseconds=0, minutes=0,hours=0,weeks=0)
# import datetime
# dt=datetime.datetime(2018,2,28)+datetime.timedelta(10)    #注意只有闰年才有29
# print(dt)   # 输出2018-03-10 00:00:00
# dt=datetime.datetime(2018,2,28)+datetime.timedelta(weeks=10)    #注意只有闰年才有29
# print(dt)   # 输出2018-03-10 00:00:00

# 当显示在界面上时，都需要进行格式化输出，使它能够符合当地人查看日期和时间的习惯。
# 与日期时间格式化输出相反的操作为日期时间的解析，即输入字符，转化为time()对象。
# 使用strftime()和strptime(), 前者将类输出为给定格式的序列, 后者相反.
# datetime, date, time 中都有一个格式化参数format,用来控制日期时间的格式,使用为%,.%y等等
# import datetime
# str_date ='2018-02-19 10:40:26'     #数据位置和格式位置一一对应，6位对6位
# date = datetime.datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')
# print(date)
'''
如果想使用时区信息，使用timezone类， 它是tzinfo的子类， 提供了UTC偏移时区的实现。构造方法为：
datetime.timezone(offset，name=None)   #offset为UTC偏移量，例如-5为Newyork，name为时区名称，可以省略掉

# 想导入所有的类可以用from datetime import *  语句。
# .astimezone()函数是调整时区，
# from datetime import datetime,timezone,timedelta
# utc_dt=datetime(2008,8,19,23,59,59,tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt=timezone(timedelta(hours=9))   #定义时区
# bj_dt=utc_dt.astimezone(bj_dt)       # 重新定义时区。这个函数接受一个timezone的类实例,将现有时间改为类的时区. 
# print(bj_dt)                         # 时间后退9个小时
#bj_dt.strptime('%Y-%m-%d %H:%M:%S %z')
# print()功能有限，要想满足复杂的日志输出需求，，可以使用logging 模块，它是Python 的内置模块。
'''
# # 从低到高五种输出模式：Debug(), info(), warning(), error(), critical()
# import logging
# logging.basicConfig(level=logging.INFO)   # logging之中设置日志级别为 ERROR# 改变日志级别为DEBUG ，所有日志函数信息都能输出，
# logger=logging.getLogger('chapter13')  # 定义一个新的日志化对象.
# logger.debug("这是debug信息")     #  输出其与其上级的所有警告
# logger.info("这是info信息")
# logger.warning("这是Warning信息")
# logger.error("这是ERROR信息")
# logger.critical("这是Critical信息")
# 输出显示的root: 说明进行日志输出的对象是root日志器（logger），也可以使用getLogger（）函数创建自己的日志器对象，
# 然后上述程序运行完毕之后, 会在文件夹内部生成一个logger.conf文件.
# 上面使用getlogger之后, 就会输出ERROR:chapter13:这是ERROR信息等, 显示当前模块名字而不是root默认.
'''可以根据自己的需要设置日志信息的格式布局format格式。'''
# %(name)s 日志器名  %(asctime)s 输出日志时间 %(filename)s 包括路径的文件名%(funcName)s 函数名
# %(levelname)s 日志等级 %(processName)s 进程名 %(threadName)s 线程名 %(message)s 输出的信息
# import logging
# logging.basicConfig(level=logging.INFO,     # 等级, 日志时间,线程名字,
#                     format='%(asctime)s - %(threadName)s-'
#                     '(name)s-%(funcName)s-%(levelname)s-%(message)s',  # 日志名称. 函数名, 日志等级, 输出信息.
#                     filename='test.log')   # 自动新建一个文件test.log，如果没有的话，然后信息追加进去一直保留/
# logger=logging.getLogger(__name__)   # 注意实际输出的显式为__main__函数。随便改为其他的会报错的
# # 1.__name__是python的一个内置函数，记录着一个字符串。
# # 2.如果是被其他文件通过import xxx，执行时候，__name__的名字为模块名
# # 3.如果是当前程序执行__name__,其名字为__main__ # 显然这里是当前程序执行.
# logger.debug("这是debug信息")
# logger.info("这是info信息")
# logger.warning("这是Warning信息")
# logger.error("这是ERROR信息")
# logger.critical("这是Critical信息")
# def funlog():
#     logger.info('进入了funlog函数')    #输出的格式化是无效的?
# logger.info('调用funlog函数')
# print(funlog())
# 日志重定位: 日志信息默认是输出到控制台的，也可以将日志信息输出到日志文件中，甚至可以输出到
# 网络中的其他计算机。使用filename重定位于test.log
'''上文配置参数都是在basicConfig之中进行的，但是实际上可以直接读取文件，这样的一个文件之中存在的是需要的格式所写成的代码。
即使用配置文件，配置信息可以从配置文件中读取。
'''
# import logging
# import logging.config
# logging.config.fileConfig("logger.conf")   # 声明读取配置文件的位置
# logger=logging.getLogger('logger1')        # 从文件中读取数据的格式信息
# logger.debug("这是debug信息")
# logger.info("这是info信息")
# logger.warning("这是Warning信息")
# logger.error("这是ERROR信息")
# logger.critical("这是Critical信息")
# def funlog():
#     logger.info('进入了funlog函数')         # TODO 运行错误？
# logger.info('调用funlog函数')
# funlog()












