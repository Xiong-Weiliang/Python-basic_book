# TODO 数据交换格式
# 数据交换格式由csv, xml, json 三种格式, csv在信息很长的时候可能会搞混. 所以由自带描述的json和xml信息.
# json的数据描述很少, 所以被成为轻量化的数据交换格式.
# 常见的一些字符编码方式无非有：Unicode、ASCII、GBK、GB2312、UTF-8
# csv(comma separated values)用Comma分割数据项(字段), 主要用于电子表格和数据库之间的交换.
# csv可以用excel(GBK编码)打开,但是可能会丢失信息. 要求不丢失信息的时候可以将csv保存为GBK字符集合.
# 处理csv用open()和spilt分割就可以了.
# csv模块提供的读写函数为csv.reader()和csv.writer()函数, 返回一个可迭代对象.
# csv.reader(csvfile, dialect='excel', **fmyparams) 参数分别为文件名. 方言(cvs.dialect的子类: csv.excel, csv.excel_tab,csv.unix_dialect种),最后参数为编码方式等等.
''' string.join()字符串连接  os.path.join()用于将路径连接返回'''
# import csv
# with open(r'E:\PYTHON_PROJECT\Python_book\Book_Numerical Python\books.csv','r',encoding='UTF-8') as rf:  # 注意中英文混用使用UTF-8编码.
#     reader=csv.reader(rf, dialect=csv.excel) #默认的格式使得reader一次返回一行.
#     for row in reader:
#         print('|'.join(row))     #注意这里用join()函数连接字符串, 同时用'|'进行分隔.
# 上述为join()函数的用法, 定义分隔符, 然后迭代进行.
'''writer()的用法类似以上'''
# import csv
# with open('Python_book/Book_Numerical Python/books.csv','r',encoding='UTF-8') as rf:
#     reader = csv.reader(rf)
#     with open('Python_book/Book_Numerical Python/books2.csv','w',newline='\n', encoding='UTF_8') as rf:
#         writer=csv.writer(rf,delimiter=',')   #  不同的定界符会有不同的写入效果.
#         for row in reader:
#             print('|'.join(row))
#             writer.writerow(row)
# writerow()将一个列表全部写入csv的同一行。writerows()将一个二维列表中的每一个列表写为一行。
''' XML语法要求很严格, '''
# 声明 version和encoding; 根元素 note; 子元素 to, content, from 等; 属性 e.g.<Note id="1">中id="1"就是属性名和属性值.
# 命名空间:用于为XML 文档提供名字唯一的元素和属性; 限定名,定义元素和属性的合法标识符.
# 作也是具有读写两种,读入称之为'解析', 由SAX和DOM两种流行的方式. 都位于XML模块之中. (另外一个可以使用的是ElemetTree结构)
# SAX事件驱动, 但是只能读入, 速度极快. DOM使用树状解析方法, 可以修改,文件大的时候很慢.
#  以下为一个示例代码, 关于xml的读取.
#
# import xml.etree.ElementTree as ET
# tree=ET.parse(r'E:\PYTHON_PROJECT\Python_book\Book_Numerical Python\Notes.xml')
# print(tree)
# root=tree.getroot()
# print(type(root))   #  <class 'xml.etree.ElementTree.Element'> 整个文档树.
# print(root.tag)      # tag属性可以获得标签.
# for index,child in enumerate(root):    # 遍历根元素.
#     print('The {0}th {1}element: attribute {2}'.format(index,child.tag,child.attrib))     #  attribute 获得属性.
#     for i,child_child in enumerate(child):  #  二次遍历, 此时遍历的是root的child元素.
#         print('Label{0}, content:{1}'.format(child_child.tag, child_child.text))      #  tag是获得子元素的标签名, text是获得子元素的文本内容.

'''
以上代码是遍历整个xml文档, 查找特殊元素或者属性时候使用find+Xpath.
1) find(match, namespace=None) 查找匹配match(标签名字或者路径)的第一个元素.
2) findall() 同上, 只是查找所有的元素.
3) findtext() 查找匹配的第一个文本.  
Xpath 类似于 SQL, 用于专门在XML中查找信息 .Xpath 将所有的元素,属性和文本都看作节点, 几个符号如下:
nodename 结点名称
.  当前结点    .. 父节点   / 路径指示符
// 所有子节点 [@attrib]  选择指定属性的所有节点,一个类似的是[@attrib='value']  [position] 指定位置,默认从1开始, 
./Note[1] 表示第一个Note节点, ./Note[last()]表示最后一个结点.  
结构化查询语言(Structured Query Language(SQL))提供了一套用来输入,更改和查看关系数据库内容的命令。
'''
# 以下为 XPath 的示例代码
import xml.etree.ElementTree as ET # 打开用绝对路劲准没错.
tree=ET.parse(r'E:\PYTHON_PROJECT\Python_book\basic_book_chapter\Notes.xml')
root=tree.getroot()
node=root.find("./Note")
print(node.tag, node.attrib)
node=root.findall("./Note/CDate")
print(node)
node=root.findall("./Note[@id='2']")
print(node)
# Json格式轻量级, 多用于web之中用于降低流量, json的两种结构对象为object和array.
# 一个简单的json例子如example1.json文件, 冒号匹配, Comma分割, 可以使用数组, 可以嵌套. Caution: json本身不接受注释, 必须加辅助软件.
# 将python转化为json格式称之为编码.
'''import json
py_dict={'name':'tony','age':30,'sex':True}
py_list=[1,3]
py_tuple=('A','B','C')
py_dict['a']=py_list       #  新增加的两个 dict 项.
py_dict['b']=py_tuple
print(py_dict)
print(type(py_dict))
# 编码方式和过程
json_obj=json.dumps(py_dict)
print(type(json_obj))
# 编码参数设定
json_obj=json.dumps(py_dict,indent=4) #indent=4 表示缩进4个空格.
print(type(json_obj))
# 将json文件写入到data1.json文件
with open(r'E:\PYTHON_PROJECT\Python_book\basic_book_chapter\data1.json','w') as f:
    json.dump(py_dict,f)  #另外一个写入函数是dumps(), 参数和dump类似.
'''
# 解码过程,  使用load()或者loads()函数. 返回python数据.
# import json
# # json_obj=r'{"name":"tony","age":30,"sex":true,"a": [1, 3],"b": ["A", "B", "C"]}'   #注意必须是严格的双引号, 单引号报错
# # py_dict=json.loads(json_obj,strict=False)
# # print(type(py_dict))
# with open(r'E:\PYTHON_PROJECT\Python_book\basic_book_chapter\data1.json',"r") as f:
#     data=json.load(f)  #将json的文件抽取出来.
#     print(data)
#     print(type(data))
    # str=f.read()
    # data=json.loads(str) # 读取字符串.
    # print(data)
# Windows配置文件所储存的格式为.ini, 也称为配置文件,但是在其余平台之下也可以用为数据交换格式.
# 配置文件使用 键-值 配对结构, 可以进行少量的数据交换和储存, 配置读取使用configparser模块进行.
'''读取配置文件'''
import configparser
config=configparser.ConfigParser()     #  创建配置解析器的对象, 使用read()读取.
config.read(r'E:\PYTHON_PROJECT\Python_book\basic_book_chapter\Setup.ini',encoding='UTF-8')
print(config.sections()) #  返回所有文件的节
section1=config['Startup']          # 返回 Startup 配置项
print(config.options('Startup'))    # 返回所有 Startup 的配置项,
print(section1['RequireOS'])        # 返回Startup中的配置项.
print(section1['RequireIE'])
print(config['Product']['msi'])   #两个中括号, 依次深化索引.输出Product的msi值
print(config['Windows 2000'],['MajorVersion'])
print(config['Windows 2000'],['ServicePackMajor'])
value=config.get('Windows 2000', 'MajorVersion')   # 返回字符串, 也可以用 getint 或者 getfloat,getbealoon 返回浮点或者布尔类型.
print(type(value)) #str对象.
''' 写入配置文件 '''
import configparser
config=configparser.ConfigParser()
config.read(r'E:\PYTHON_PROJECT\Python_book\basic_book_chapter\Setup.ini',encoding='UTF-8')
config['Startup']['RequireMSI']='8.1'
config.add_section('Section5')
config.set('Section5','5_Name','5_MAC')
with open(r'E:\PYTHON_PROJECT\Python_book\basic_book_chapter\Setup.ini','w') as fw:
    config.write(fw)


