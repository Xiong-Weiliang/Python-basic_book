# TODO Chapter11 面向对象编程(Object Oriented Programming,OOP)
'''
在Python 中一切数据类型都是面向对象的，即类与实例.面向对象的封装与真实世界的目的是一样的。封装能够使外部访问者不能随意存取对象的内部数据，
隐藏了对象的内部细节，只保留有限的对外接口。外部访问者不用关心对象的内部细节，操作对象变得简单。
1.继承：父类与子类（超类与派生类）object 是所有类的根类。对象的生命周期包括：创建、使用和销毁。销毁是自动的
代码的pass语句什么操作都不执行，用来维持程序结构的完整。代码不想编写，又不想有语法错误，可以使用pass 语句占位。
'''
class Animal(): # 声明
    pass        # 不作为
cat=Animal()    # 实例化
print(cat)    #  输入类的类别.  实际上是调用了__str__()方法说明对象的描述信息.
'''
# 类的成员：成员变量(attributer)、成员方法和属性(property);成员变量又分为特有的实例变量和共有的类变量;
成员方法又分为实例方法、类方法和静态方法。 使用setter()和getter()函数对attributer()进行设定和操作。
'''
# class Animal(): # 声明
#     name='Animal'    # 类变量，共有
#     def __init__(self,age,sex,weight):   # C++ 的私有变量( python 的实例变量)
#         # 构造方法中的self指向当前对象实例的引用
#         self.age=age
#         self.sex=sex
#         self.weight=weight
# cat=Animal(10,'male',20)   # 可以混合使用
# '''类名类变量”事实上是有别于包和模块的另外一种形式的命名空间。注意：不要通过实例存取类交量数据。'''
# print(cat.sex)   # 访问方法.
# print(cat.name)
# cat.add='change_add'   # 这个实例变量无法通过类中的方法访问。但可以实例访问,人为增加的一个成员变量.但是不要这么干,会导致程序混乱.
# print(cat.__dict__)   # 为了查看实例cat的变量有哪些，可以通过object提供的__dict__变量查看
# cat1=Animal(1,1,1)    # 这个是没有high变量的。
# cat1.add='add of cat1'
# print(cat1.add)
# （魔法）构造方法 __init__()：定义时它的第一个参数应该是self，其后的参数才是用来初始化实例变量的。调用构造方法时不需要传入self。
class Animal(): # 声明
    name='Animal'    # 类变量，共有
    def __init__(self,age,sex,weight=0):   # 私有变量
        # 构造方法中的self指向当前对象实例的引用
        self.age=age
        self.sex=sex
        self.__weight=weight   #Python 的封装性使用命名实现，私有变量用__开头声明即可,不能直接更改而是使用setter
    @classmethod   #装饰器Decorators用于calssmate声明以下是类方法
    #类方法可以通过类名调用, 但也可以(不规范的)使用实例名字调用.
    def NameReturn(cls,num):  #这个cls是指定的参数，type类型:当前Account类型的实例。
        print('NameReturn function is using'*num)
        return cls.name      #只能在类方法中可以访问其他的类变量和类方法,不能访问其他实例方法和实例变量。
    def eat(self):    #类里面的函数定义方法
        #简而言之, 类方法使用cls, 而实例方法使用self. 分别映射到类和实例.
        self.__weight+=0.05
        print('eat')
    def __run(self):   #私有方法，改名类似。只能在类定义的内部使用, 不用使用实例化的调用方法.
        self.__weight-=0.04
        print('run')
    @staticmethod   # 静态方法只是为了提供一个基于类名的命名空间,既不会和类名字绑定,也不会和实例绑定.
    def static(amt):  # 不指明cls和self,只传递参数。可以通过类名或者实例调用.
        return Animal.NameReturn(amt)
    @property   # 用于getter
    def weight(self):   #注意, getter的名称不是叫'getter'而是和属性名字一致, 用property来修饰.setter一致, 只是修辞语言不一致.
        #定义属性时应该先定义getter 访问器， 再定义setter 访问器
        return self.__weight
    @weight.setter   #用于setter
    def weight(self,weight):
        self.__weight=weight
cat1=Animal(10,10,10)
# cat1.set_weight(123)
cat1._Animal__run()   # 非 常规 调用这些实例方法， 注意其中不需要传入self 参数。
print('a1体重：{0}'.format(cat1.weight))   #外部访问会出错,只能函数内部调用，
# 双下画线__开头的私有变量其实只是换了一个名字，它们的名规律为“_类名__变量”， 快捷键F1书签。
print('a1体重：{0}'.format(cat1._Animal__weight))   #这个可以输出，但是只是换了个名字。这样可能会破坏封装性质
a=cat1.NameReturn(2)
print(a)
'''区别是：一句话描述：self是类（Class）实例化对象，cls就是类（或子类）本身，取决于调用的是那个类。'''
#  在严格意义上的面向对象设计中， 一个类不应该公有实例成员变量的，应该全为私有，通过公有的 setter与 getter 访问器访问。
#  ＠property用来修饰getter访问器，＠属性名.setter 用来修饰setter访问器

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        template='Person[name={0},age={1}]'
        s= template.format(self.name,self.age)
        return s
class Student(Person):
    def __init__(self,name,age,school): #声明所有的变量
        super().__init__(name,age)   #继承其方法（只能继承公有的变量和方法）
        self.school=school
    def info(self):   #重写函数
        template='Student [name={0},age={1}，school={2}]'
        s= template.format(self.name,self.age,self.school) # 这里也说明, format的格式是可以分离书写的.
        return s
stu1 = Student('Klaus', 22, 'ETH')
Person1 = Person('Hohn', 19)
print(stu1.info())
print(Person1.info())
#  Python 支持多继承,注意函数的查找从左到右。
class Doctor(Student,Person):      # 如果顺序反过来，报错：无法实现一致解析 Cannot create a consistent 
    pass                           # method resolution order (MRO) for bases Person, Student
Doc1=Doctor('Mike',29,'Oxford')
print(Doc1.info())
# 多态性：发生的前提为继与重写。————多态发生时， Python 解释器根据引用指向的实例调用它的方法。
# 所谓多态性的本质就是，相同的函数名字，不同的类中可以内容不同.

# 用isinstance(object, classinfo)函数可以检查其实例是否为某一个类, 例如：
print(isinstance(Doc1,Doctor))
print(isinstance(Doc1,Student))    # 注意继承的也会返回true
# 类似的一个函数是issubclass()函数, 用于检查类是否为类的子类
''' 鸭子类型：不关注变量的类型，而是关注变量具有的方法,只要函数存在，而不会管传入的类型是什么——因为python不会检查。Python 所有类都直接或间接继承自object类， 
它是所有类的“祖先”，object有很多方法，这意味着所有的类通用。
两个可以重写的典型： __str__() ： 返回该对象的字符串表:为了日志输出等处理方便，所有的对象都可以输出自己的描述信息
__eq__()：指示其他某个对象是否与此对象“相等” 。在类中需要精确定义其类型，否则可能报错。
两个函数的作用: 前者决定了print()打印出的实例信息, 后者决定了比较规则. 
'''
# 枚举是用来管理一组相关的有限个数常量的集合，
#   为了使枚举类常量成员只能使用整数类型，可以使用enum.IntEnum 作为枚举父类。
#   为了防止常量成员值重复，可以为枚举类加上＠enum.unique 装饰器
import enum   #枚举类的使用要基于enum库.
@enum.unique  # 用于防止成员变量值重复. 如果有相同值报错
class weekdays(enum.IntEnum):
    Mon=1   # 由name 和 value构成. 可以访问.
    Frs=2   # 注意不要出现两个相同的命名
    Tus=3   # 常量成员值可以是任意类型， 多个成员的值也可以相同。
    Fri=5
day=weekdays.Fri
print(day)
print(type(day.value))  # 枚举值和枚举名 这里输出就是int类型.
print(day.name)




