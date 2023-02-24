#  TODO Chapter10 函数
#  Python 中的函数很灵活，它可以在模块中、但是在类之外定义，即函数，其作用域是当前模块；
#  也可以在别的函数中定义，即嵌套函数：还可以在类中定义,即方法。 函数的定义必须位于使用之前, 否则会出错.
'''格式如下：
def 函数名(参数列表):
    函数体
    return 返回值
def rectangle_area(width=100,length=20):        #这里显然设定了默认值,作为默认参数值.
    area=width*length
    return area
t1=rectangle_area(10,50)
print(t1)  #  Python的函数定义必须位于调用之前。同时，Python的传递参数有多种形式
t1=rectangle_area(length=10,width=50) #换位的效果一样的，但要确保无歧义
# 在调用函数时，一旦其中一个参数采用了关键字参数形式传递，那么其后的所有参数都必须采用关键字参数形式传递
# 其次，在定义函数的时候可以为参数设置一个默认值，调用函数时可以忽略该参数
t1=rectangle_area(length=10)
'''
# Python 不支持函数重载，而是使用参数默认值的方式提供类似函数重载的功能,函数的参数个数可以变化，它可以接受不确定数量的参数，这种参数称为可变参数。
# 可变参数有两种，即参数前加*或**形式, *可变参数在函数中被组装成为一元组，**可变参数在函数中被组装成为一个字典。
# 备注： ＊可变参数不是最后一个参数时，后面的参数需要采用关键字参数形式传递,否则歧义报错
'''
def sum(*data,multiple=10):   #元组可变参数
    total=0
    for i in data:
        total=total+i
    return total*multiple
print(sum(50,50,60,multiple=2))   #返回320
tru1=[50,60,20]    # 这里元组和列表都可以, 反正后面函数会自动封装成为元组的. 
print(sum(30,*tru1))      # 使用*拆解元组，输出的是 30+50+60+20 *10 = 1600 使用了默认的倍数为10倍. 
def show_info(sep = '->', **info):    # 注意这里的**是声明, 一旦到达函数组中,默认加入了一次类似于zip的字典集合操作. 可变参数, 字典. 注意自带你可变参数必须位于正规参数之后, 否则会报错的. 
    for k,v in info.items():   # 字典读取. 
        print('THE {0} {1} {2}'.format(k,sep,v))
    return None
dict3 = dict(zip(['a','b','c','d','e'],[1,2,3,5,'final']))
stu_dict = {'1':'a', '2':'b'}
show_info(sep='=:',info=dict3) # TODO 这里为什么不能使用整数型的输出？注意不可以使用**赋值拆包，否则会报错的
show_info(sep='=:',**dict3)   #注意上行输出一行, 而下面输出5行. 
show_info(sep='=:',dict3)   # error. 
'''
# 对字典使用*a会输出所有的keys值
# Python 函数的返回值三种形式：无返回值、单一返回值和多返回值
# 对于无返回的希望有返回，直接使用return或者return None,(常用于判定特殊情况以提前跳出函数)
# 返回多个值时候直接返回一个元组，因为不可变也比较安全。e.g.
def position(dt,speed):
    x=speed[0]*dt
    y=speed[1]*dt
    return (x,y)
move=position(50,(10,-9))
print(move)     #通过简单的赋值就可以使用. a, b=move.
# 一个模块就是一个.py文件。以下考虑函数中以及模块中的作用域问题。当存在局部函数中的变量x时候，在函数作用域内会屏蔽
# 全局x变量。在函数中将变量声明为global ， 这样就可以把变量的作用域变成全局的。
x=9
def chancex():
    global x #注意声明和赋值不可以放在一起,分两行.
    x+=1
chancex()   #定义后运行了才有值变化
print(x)
# yield而不是return返回变量时候，会返回一个generator变量。注意数据上使用列表[]而不是元组(),前者可变。
# 生成器对象是一种可迭代对象，隐含调用__next__()函数。已经没有元素可迭代时候会抛出StopIterative异常。
def square(num):
    for i in range(1,num,3):
        yield i*i
for ip in square(10):
    print(ip)    # 返回 1 16 49
# 也可以使用__next__()函数隐式调用—————注意：生成器特别适合用于选历一些大序列对象，函数内部可以嵌套函数
# Python提供了一种函数类型 function，任何函数的调用都是一种对象的实例化。可以return函数名。
def cal_fun(opr):
    def add(a,b):
        return a+b
    def mutiple(a,b):
        return a*b
    if opr=='+':
        return add   #注意这里的缩进, 缩进代表了逻辑问题.
    if opr=='*':
        return mutiple
f1=cal_fun('+')
print(f1(12,56)+cal_fun('*')(12,23))     # 返回68值, 这里说明可以多重使用.
# Lambda 表达式本质上是一种匿名函数，形式:lambda参数列表.Lambda 体部分不能是一个代码块，不能包含多条语句，只能有一条语句，
# 函数式编程的本质是通过函数处理数据，过滤 filter()、映射 man()和聚合 reduce()是处理数据的三大基本操作。
# lambda 参数分别为输入输出和(集合的)参数.
# Example1 about filter
c=lambda a,b:a*b   #  注意这里的c是函数变量.也就是说声明了一个简单的函数 c(a, b)
print(c(4,4))
user=['AA','Aa','b','ab']   # 'ASDF'.lower() 小写转化
user2=filter(lambda u:u.startswith('A'),user)  # 返回一个filter对象.参数为返回布尔值的函数f对象(这里使用lambda定义,返回bool对象), 和一个可以迭代的对象.
# user 为迭代的地方，是filter的参数。 函数选择出来以A开始的字符.
listuser2=list(user2)    # 返回一个filter转化成功的list对象.
print(list(listuser2))   # list转换为列表
print(user2)   #否则指挥输出信息为<filter object at--(location)
# 函数式编程时数据可以从一个函数“流”入另外一个函数， 但遗憾的是Python 并不支持“链式” API，这意味着必须进行多步分开的操作
use_map=map(lambda u: u.lower(),listuser2)   # 必须使用list后进行筛选   lower() 用于将其变化为小写.
print(list(use_map))
# 聚合操作会将多个数据聚合起来输出单个数据， 聚合操作中最基础的是归纳函数reduce(),
from functools import reduce   # 必须使用functools先行导入才能使用.
a=range(1,10,1)       # 其中acc参数是上次累积计算结果，i是当前元素
a_re=reduce(lambda acc,i: acc+i, a, 26)   #逻辑: 从a=26初始化, 指定为acc, 第二个元素为i, 然后相加, 现在acc=26+1, i=2, 然后不停后向刷完.
print(a_re)  # 累计到1~9+26  #即71值.


















