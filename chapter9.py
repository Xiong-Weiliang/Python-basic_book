# TODO Chapter9  序列、元组、集合 和字典，
"""
数据结构，常见的有数组(Array)、集合(Set)、列表(List)、队列(Queue)、链表(Linkedlist)、树(Tree)、堆(Heap)、栈(Stack)和字典(Dictionary〕等结构
注意：Python 中并没有数据结构，因为数纽要求元素类型是一致的，而python是动态语言。元组（tuple ）是一种序列(Sequence）结构, 序列是一种可迭代的① 、元素有序、可以重复出现的数据结构。
序列可以通过索引访问元素。序列包括的结构有列表（ list）、字符串（ str）、元组、范围(range）和宇节序列（bytes）。序列可进行的操作有索引、分片、加和乘。索引同样从0开始。
"""
import sys
# 如果直接使用中括号, 可以建立一个列表. 但是小括号是无法修改的元组
b=[1,4]
print(type(b)) #list类型
a='Hello'   # 字符串的索引与显示
print(a[1])
print(a[-4]) #注意允许负值索引，第一元素永远为0，从后向前-1，-2，-3，。。。
min(a)   #可以使用最大值max，最小值min，长度函数len，输出o   min的含义是最开始的元素，max类似
# 序列之间的切片如下：,begin,end,step 三个参数值
print(a[1:3:1]) #注意包括开始而不包括结束位置，所以输出为el，允许正负索引混用。

a=1,2,3,5     #不用括号自动成为元组 (当－个元组只有一个元素时，后面的逗号不能省略, 多个元素时随意)
b=(12,13,16)  # 注意也可以使用空原组 (务必注意这里是小括号)
print(type(b))  #查看参数的类型为type()函数。结果tuple
c=('zero','fi','nla', 5, 5.26)  #元组甚至可以类型混用，
print(c[2])    #结果为nla     #方括号用于索引
str1,str2,*str3=c # *用于将剩余的元素全部赋值给str3的值,并且作为一个list类型.  (拆开成为两个str, 一个list )
print(str3)    #结果为nla,5,5.26
for item in str3:     #for 遍历元组
    print(item)
# enumerate(c) 函数可以获得a的元组对象，该元组对象有两个元素， 第一个元素是索引， 第二个元素是数值。
for i,item in enumerate(c):  #再匹配的情况下，同时for两个值是可以的
    print('{0} -- {1}'.format(i,item))    # 从0开始进行便利输出映射.

# 列表，可以使用 list([Iterable])函数，或者直接方括号构建。索引一直都是方括号.列表也可以直接等号赋值
dlist=[1,2,'ir','sf','sdaf',]  #  每个元素后面必须有都好，最后一个一般省略。
dlist2=list((20,10,50,40,30))  #  将不可更改的元组通过list转化为列表
# 列表追加元素可以使用append() 函数，也可以直接使用+符号或者extend()。
dlist.append('gsg')    # 追加到最后面, 但是只能增加一个元素.
dlist+=['add1','aff2']
dlist.extend('ex1')   # 注意这里实际上插入3个元素，'e','x','1' 三个值.
dlist.extend(['ex1'])   #这时候就仅仅插入一个'ex1',由于带有了一个方括号将其绑定为一个元素.
print(dlist)
# 插入元素使用insert()函数方法，替换元素直接=赋值就可以
dlist2.insert(2,'insert_element')  # 插入完毕后新元素就在2的位置.
dlist2[3]='替换赋值'
# 删除的是remove(),注意输入参数是元素值，而不是序号
dlist2.extend([40])   # 注意这里实际上插入1个元素，因为有方括号
dlist2.remove(40)   # 删除第一个40,后面的不会动的。
# 删除也可以是pop(),注意输入的是序号，省略时候为最后一个元素
dlist2.pop() # 删除最后一个元素，即40 和append函数是一对.
i=1
dlist2.pop(i) #去除h指标为i的元素.
print(dlist2)
# 其他函数  • reverse()：倒置列表；
# • copy()： 复制列表； 注意,如果使用等号赋值会共享内存，因此只是提供了别名而没有生成真正意义上的新的变量,改一个另一个也会被改了.必须使用copy以生成新的变量. 
# • clear()： 清除列表中的所有元素  #注意，如果使用copy，那么a.clear()，清除之后，b依然会保存复 制时候的值，如果直接用b=a，a在clear之后，b也没了。
# • index(x[,i,j])：返回查找x 第一次出现的索引，from i to j 
# • count(x)：返回x 出现的次数，该方法继承自序列，元组和字符串也可以使用该方法。
dlist3=[10, 40, 10, 20, 20, 20, 3, 0, 0 ]
print(dlist3.index(10,1,5))   #只会搜寻第一个位置，这里会输出2
# Python 的特殊表达式一一推导式，将一种数据结构作为输入，经过过滤、计算等处理， 最后输出另一种数据结构——可分为列表推导式、集合推导式和字典推导式
#  列表推导式语法结构，其中in 后面的表达式是“输入序列”； for 前面的表达式是“输出表达式”，它
# 的运算结果会保存一个新列表中： if 条件语句用来过滤输入序列，
n_list = [x**2 for x in range(10) if x%2==0 & x%3==0]  #example1  #列表推导式子, 两个if是and关系,直接使用and也可以,类似的还有or, &(注意仅仅判定前一个)
print(n_list)

# 一种新的格式：集合，其中元素不允许重复，分为可变集合（set）和不可变集合（frozenset）。
# 使用大括号声明集合，或者使用set()转化，自动去除重复的元素
seta={'a','b','c','1',2,3,3}  #小括号为元组, 中括号列表, 大括号集合.
print(type(seta))   #集合set
setb={} #dict
print(type(setb))   #字典dict----即建一个空的集合则不能使用｛｝表示，只能使用set()
setc=set({})        # 这里就是一个空的集合。
print(type(setc))
setc.add('ele1')
#修改可变集合，
#  add(elem):添加元素，如果元素已经存在，则不能添加，不会抛出错误；一下只能增加一个.
# • remove(elem): 删除元素， 如果元素不存在抛出错误；
# • discard(elem）： 删除元素， 如果元素不存在，不会抛出错误：
# • pop(): 删除返回集合中任意一个元素，返回值是删除的元素；
# • clear():清除集合。
#集合是无序的， 没有索引， 不能通过下标访问单个元素。但是可以通过for访问，同样可以使用enumerate()函数
# setc={'ele1','ele2','ele3','ele1'}  #自动删除重复元素
# setc=set([1,2 ,3 ,4, 5])
# for i,item in enumerate(setc):  # 此时变 i 不是索引， 只是遍历集合的次数。
#     print('第{0}个元素为{1}'.format(i,item))
'''创建不能被修改的不可变的集合的唯一方法是使用frozenset()函数。例如setc=frozenset(setc)'''
# student_set = frozenset({'a','b','c'})
# 类比于列表推导式，集合推导式也是一样的结构
# set=[1,1,1,1,2,2,3,3,3,3,3]  # lsit
# n_set={x**2 for x in set}   # 集合推导式子自动去除重复元素，大括号而不是中括号,注意这两个输出的不同之处
# print(n_set)
# n_set=list(n_set)  #等价于n_set=[n_set]
# # n_set=[x**2 for x in set]    # 列表推导式
# print(n_set)
'''同样的有集合推导式子, 区别在于, 使用的是{}而不是[], 返回的也不是List而是set. '''
'''字典dict可迭代的、可变的数据结构，通过键来访问元素。字典结构比较复杂，它是由两部分视图构成的， 一个是键(key)视图，另一个是值(value)视图。
键视图不能包含重复元素，值集合可以，键和值是成对出现的。'''
#建立方法，dict()或者大括号，但同时包含‘键：值’，  ()是tuple, [] 是list, {}是set或者dict
'''dict1 = {102: '张三', 105: '李四', 109: '王五'}    #注意在字典里在不能使用之前的[0]索引, 而应该使用[102]的基于key的索引.
len(dict1)
t1=dict({111 : '第六'})
dict2=(dict1,t1)    # 字典缝合 直接使用小括号. 
print(dict2)
# zip()函数，将两个可选代对象打包成元组，e.g.
dict3=dict(zip([1,2,3,4,5,],[1,2,2,3,'final']))
print(dict3)
# 也可以使用如下形式
dict4=dict(A1='1',A2='2',A3='3')   #该方法的要求，1. 键索引必是字符，不可使用int否则混乱，2. 键的引号全部省略。
print(dict4['A1'])
操作函数 pop(),popitem(),前者返回键，后者返回元组对象。语句为del()。
dict4.pop('A1')  #删除这一项. 
字典还需要一些方法用来访问它的键戒值，这些方法如下。
• get(key[, default］） ：通过键返回值，如果键不存在返回默认值。
• items():返回字典的所有键值对。
• keys():返回字典键视图。
• values():返回字典值视图。
也可以使用in 和 not in来访问内部结构。  例如L:  'A1' in dict4
字典的遍历过程可以只遍历值视图，也可以只遍历键视图，也可以同时遍历。这些遍历过程都是通过for 循环实现
使用 keys和values调用键与值的循环，使用items调用元组序列循环
遍历过程可以只遍历值视图，也可以只遍历键视图，也可以同时遍历。这些遍历过程都是通过for 循环实现
'''
dict5=dict(zip([1,2,3,4,5,6,7],[3,5,7,9,11,13,16]))
output={k:v for k,v in dict5.items() if v%2!=0}    # 注意这里的k:v 和 k,v是一个整理，表明一个键加值合起来。
print(output)
output={k for k,v in dict5.items() if v%2==0}   # 只返回k也就是key。
print('{0}IS THAT'.format(output))


