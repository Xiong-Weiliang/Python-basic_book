# TODO chapter14 正则表达式，
'''正则表达式中理解各种元字符是学习的难点和重点。Python 也提供了利用正则表达式实现文本的匹配、查找和替换等操作的 re 模块。
# 给定一个正则表达式和另一个字符串，我们可以达到如下的目的：
# 1. 判断给定的字符串是否符合正则表达式的过滤逻辑（称作“匹配”）：
# 2. 可以通过正则表达式，从字符串中获取我们想要的特定部分。'''
# coding utf-8
'''正则表达式（ Regular Expression ，在代码中常简写为regex 、regexp 、RE 或re 〕是预先定
义好的一个“规则字符串”，通过这个“规则字符串”可以匹配、查找和替换那些符合“规则”的文本。'''
'''使用正则表达式实现这些功能会比较简单，比起直接使用查找函数，而且效率很高，唯一的困难之处在于编写合适的正则表达式。
可以使用于诸如如数据挖掘、数据分析、网络爬虫、输入有效性验证等。Python也提供了利用正则表达式实现文本的匹配、查找和替换等操作的re模块。
正则表达式字符串是由普通字符和元字符（ Metacharacters ）组成的
普通字符：字符字面意义表示的字符.元字符：预先定义好的一些特定字符，是用来描述其他字符的特殊字符，
'''
# 请务必注意, r的作用并没有限制一定为文本, 也可以被解析, 应当理解为对转义字符的一种简单表示.
# 常用的元字符如下：
#  \ 转义字符    . 任意字符    + 重复大于一次    * 重复大于零次
#  ？ 重复0次或者一次    | 选择    {} 定义量词   [] 定义字符类(相当于区间出现任何一个都匹配到)
#  () 分组   ^ 取反(不出现这个字符),或者一行的开始    $ 匹配一行的结束
# encoding='utf-8'
# import re
# p1= r'\w+@zhijieketang\.com' #等价于'\\w+@zhijieketang\\.com'  # 这里的 \w 为预定义字符类, 指可以匹配任何语言的单词字符.
# # r的作用为：在原始字符串里，所有的字符都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
# p2= r'^\w+@zhijieketang\.com$'   #开始^且尾部$匹配, 后续使得math只能返回none, 无匹配.
# text="Tony‘s email is tony_588@zhijieketang.com"
# m=re.search(p1,text)
# print(m)
# m=re.search(p2,text)    #只要存在就可以返回一个 match 对象
# print(m)
# p2='tony_588@zhijieketang.com'
# m=re.search(p2,text)
# print(m)
'''注意：在正则表达式中本身包含很多反斜杠“\”等特殊字符串，推荐使用Python中原始字符串表示正则表达式，
否则需要对这些字符进行转义，所以pl 变量也可以使用'^\\w+@zhijieketang\\.com$'普通字符串形式。'''

#  定义字符类:定义一个普通的字符类需要使用“[”和“]”元字符类.匹配Java或者java使用如下：
#  p = r'[Jj]ava'
#  m = re.search(p,'Here is Klaus')
#  print(m)
#  在正则表达式中指定不想出现的字符，可以在字符类前加“^”符号,如下例：
# p = r'[^0123456789]'
# m=re.search(p,'1234x')
# print(m)    #  只要出现了非零字符就可以匹配。
# 区间表示[0123456789]等价于[1-9]
# import re
# m=re.search(r'[A-Za-z0-9]','D10.3')  #字符串简写
# print(m)
# m=re.search(r'[0-25-7]','A1489DnkjF')
# print(m)
# # 出现次数的控制：{n,m}至少出现n次但不超过m次
'''预定义字符类'''
# .匹配任意字符   \\匹配反斜杠\   \n和\r匹配换行和回车   \f用于换页   \t匹配水平制表符
# \v匹配垂直制表符  \s匹配空格    \S和^\s相反, 匹配任何非空字符   \d匹配任何数字字符
# \D等价于^\d     \w匹配任何语言任何单词字符
'''量词'''
# ?出现0次或者一次   *出现零次或者多次   +出现一次或者多次
#  {n}出现n,   {n, m}至少出现n但是不超过m次    {n,}至少出现n次
# m = re.search(r'\d{1,8}','9fds87654321')
# print(m)
# # 贪婪量词和懒惰量词——即尽可能多的或者少的匹配字符，默认为贪婪，懒惰加？即可
# m = re.search(r'\d{1,8}?','87654321')  #  此时只会匹配8, 一位, 而且是最前面的一位.
# print(m)

# 分组的使用：可以在正则表达式中引用己经存在的分组
# import re
# p=r'(121){2}'   #表示对121重复两次，即121121，其实这里相当于两组数据，
# m=re.search(p,'121121abcabc')     # 作为单个字符串, p就是文本, 但是在search的时候, 文本的符号被赋予了意义..
# print(m)
# print(m.group())
# print(m.group(1))   # 返回第一个分组
# # groups()方法返回所有分组，例子如下
# p=r'(\d{3,4})-(\d{7,8})'
# m=re.search(p,'010-987654321')
# print(m)           # 返回地址
# print(m.groups())  # 返回两组('010', '98765432') 注意组的编号是从1开始的. 不是0.

'''访问分组除了可以通过组编号，也可以通过组名访问前提是要在正则表达式中为组命名。组命名通过在组开头添加“？P＜分组名〉”实现。'''
# import re
# info = r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})'
# m=re.search(info,'010-987654321')
# print(m)
# print(m.groups())
# print(m.groups('area_code'))    #根据组名字返回内容
#
# '''XML（Extensible Markup Language）可拓展标记语言文件，有效的XML 代码，开始标签和结束标签应该是一致的
# # 可以使用反向引用分组，即在内部引用之前的分组。'''
# import re
# p=r'<([\w]+)>.*</([\w]+)>'    #w:任一文本，+：出现一次或者而多次
# m=re.search(p,'<a>abc</b>')
# print(m)    #这里可以查找到的，因为前后都有字符，尽管不同.
# p=r'<([\w]+>).*</\1>'    #注意括号的位置
# m=re.search(p,'<a>abc</a>')
# print(m)       # 这里返回None，因为反向引用使得前后必须一致, 也就是说, 反向引用相当于在搜索之上加入了一个等式约束.
'''使用非捕获分组，当并不想引用子表达式的匹配结果，不想捕获严格的匹配结果，只是将小括号作为一个整体进行匹配的时候。
使用方法加‘？’  '''
import re
s='img1.jpg, ing2.jpg, img3.jpg'
p=r'\w+(\.jpg)'
mlist=re.findall(p,s)     #捕获分组,findall()函数返回string中所有与pattern匹配的全部字符串,返回形式为tuple.
print(mlist)
p=r'\w+(?:\.jpg)'         # 非捕获分组将整个括号内的分组，即？的部分也包括. 作为一整个整体.
mlist=re.findall(p,s)     #非捕获分组
print(mlist)

'''  search() and match()函数
search():在输入字符串整个中查找，返回第一个匹配内容，如果找到一个则match 对象，如果没有找到返回None.
match():在输入字符串开始处！开始查找匹配内容，如果找到一个则match 对象，如果没有找到返回None'''
# 返回的match对象有许多处理方法。group() 返回匹配的子字符串，start()和end()为索引，span()返回跨度
'''findall()和finditer()函数非常相似，它们的区别如下所示。
findall() 输入字符串中查找所有匹配内容， 如果匹配成功， 则返回m atch 列表对象
finditer() 匹配成功， 则返回容纳match 的可选代对象， 通过法代对象每次可以返回一个match 对象， 
如果匹配失败则返回None 。迭代对象可通过for进行遍历'''

# 字符串分割使用split（）函数，根据给定的字符串进行分割。
# re.split(pattern, string, maxsplit=O , flags=O)# 参数分别为：参数pattern是正则表达式； 参数string是要分割的字符串； 参数maxsplit是最大分
# 割次数，maxsplit默认值为零，表示分割次数没有限制：参数flags是编译标志。
#  字符串替换使用sub()函数
#  re.sub(pattern,repl,string,count=O,flags=O)
# 参数pattern是正则表达式； 参数repl是替换字符串；参数string是要提供的字符串；
# 参数count是要替换的最大数量，默认值为零， 表示替换数量没有限制;参数flags 是编译标志.
# 注意切换或者分割的地方都可以是正则表达式, 说明对分割处的描述.

'''但是为了提高效率， 还可以对Python正则表达式进行编译, 编译之后的正则表达式可以重复使用,从而能减少其后的反复解析或者验证. 
compile()函数可以编译正则表达式
re.compile(pattern[, flags=O])  # 参数分别为正则表达式与编译标志，翻译一个编译的正则表达式对象regex
'''
# 编译完成之后，可以使用regex.search(string,position,endposition)去替代re.search(pattern,string,flags=0)
#compile()函数编译正则表达式对象时，还可以设置编译标志。编译标志可以改变正则表达式引擎行为。
'''
1. ASCII 与Unicode编码，通过re.A与re.U设置。A似乎比U要严格许多，更容易造成不匹配
2. 忽略大小写，re.I(IGNORECASE)
3. 点元字符.匹配换行符'enter',使用re.DOTALL(或者使用re.S)
4. 多行模式，re.MULTILINE(即re.M)使得^和$匹配任意一行的开始与结束。默认为整个字符串的开始和结束。
5. 编译标志re.VERBOSE （或re.X）可以设置详细模式，可以在正则表达式中添加注释，可以有空格和换行
   在包含了换行等符号，所以需要使用双重单引号或三重双引号括起来，而不是使用原始字符串。
'''
# import re
# p=  """(java)  #正则表达式原本是(java).*(python）
#        .*
#        (python)
#     """
# regex=re.compile(p, re.I|re.VERBOSE)    #当需要设置多编译标志时使用或,编译标志之间需要位或运算符‘|’ 。
# m=regex.search('I like python and Java.')
# print(m)









