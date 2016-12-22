# 字符串
## 字符串的定义
* ''
* ""
* ''' ''' or """ """
    * 在Python中，''和""定义字符串的方法完全一样
    * ''' '''和""" """使Python可以跨行定义字符串
```
In [1]: s = '''hello
   ...: world
   ...: '''

In [2]: s
Out[2]: 'hello\nworld\n'    # 加上了\n换行符
```
## 字符串的转义
* \：转义，特殊如\n换行，\t横向制表符，\r回车
* r''：加r前缀代表此字符串是自然字符串，不会被转义
```
In [6]: s = 'i\'m Az'

In [7]: s
Out[7]: "i'm Az"

In [14]: s = r'\n\t'

In [25]: s1 = '\n\t'

In [26]: print(s1)

	

In [27]: s2 = r'\n\t'

In [28]: print(s2)
\n\t
```
## 字符串的操作
### 下标操作
* 字符串是一个集合，可迭代对象(具有__iter__()方法的对象)
* 字符串不可变
```
In [29]: s = 'Python'

In [30]: s[1]
Out[30]: 'y'

In [32]: s[1] = 'P'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-32-1143d2fb186e> in <module>()
----> 1 s[1] = 'P'

TypeError: 'str' object does not support item assignment
```
### 字符串的连接
* join：S.join(iterable)，S
* \+  
```
In [33]: lst = ['从', '入', '门', '到', '放', '弃']

InIn [34]: ''.join(lst)
Out[34]: '从入门到放弃'

In [35]: '*'.join(lst)
Out[35]: '从*入*门*到*放*弃'

In [36]: lst[0] + lst[1] + lst[2] + lst[3] + lst[4] + lst[5]
Out[36]: '从入门到放弃'

In [37]: 123 + 'abc' # 要注意类型的转化，str(123)或者`123`
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-37-31ba0f9d7deb> in <module>()
----> 1 123 + 'abc'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
### 字符串的分割
* split：S.split(sep=None, maxsplit=-1),默认以空格分割，多个空格会当成一个空格处理；从左往右分割，maxsplit=N表示分割多少次，-1表示分割所有;
* rsplit：同split，但是从右往左进行分割,效率低于split
```
In [40]: s = "To be a better man"

In [41]: s.split()
Out[41]: ['To', 'be', 'a', 'better', 'man']

In [42]: s.split(maxsplit=2)   # 分割2次
Out[42]: ['To', 'be', 'a better man']

In [43]: s.split('a')    # 指定'a'为分隔符
Out[43]: ['To be ', ' better m', 'n']

In [44]: s.rsplit(maxsplit=2)    # rsplit，从右往左分割2次
Out[44]: ['To be a', 'better', 'man']
```
* splitlines：S.splitlines([keepends])，分割多行字符串，默认按行分割，并且返回结果不带换行符号；加上True换带上换行符
```
In [48]: s = """1
    ...: 2
    ...: 3
    ...: """

In [49]: s.splitlines()
Out[49]: ['1', '2', '3']

In [50]: s.splitlines(True)     # 保存了换行符
Out[50]: ['1\n', '2\n', '3\n']
```
* partition：S.partition(sep) -> (head, sep, tail), 根据指定的分隔符将字符串进行分割，如果字符串包含指定的分隔符，则返回一个3元的tuple，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串;
* rpartition：从右往左分隔
```
In [51]: s = "IPADDR=127.0.0.1"

In [53]: s.partition('=')
Out[53]: ('IPADDR', '=', '127.0.0.1')
```

### 字符串大小写转换
* S.upper()：将小写字母全部转成大写，返回一个新字符串
* S.isupper()：判断字符串是否全部都是大写
* S.lower()：转换小写
* S.islower：判断字符串是否全部是小写，返回新字符串
* S.title()：将所有单词的首字母转换成大写，返回新字符串
* S.istitle()
* S.capitalize()：首字母大写
* S.casefold()：将大写转换小写，通常用来忽略大小写
* S.swapcase()：将大小写转换
```
In [64]: s = 'upPer upPer'

In [65]: s.upper()
Out[65]: 'UPPER UPPER'

In [66]: s.upper().lower()
Out[66]: 'upper upper'

In [67]: s.title()
Out[67]: 'Upper Upper'

In [68]: s.capitalize()
Out[68]: 'Upper upper'

In [69]: s.casefold()
Out[69]: 'upper upper'

In [70]: s.swapcase()
Out[70]: 'UPpER UPpER'
```
### 字符串修改
* S.replace：S.replace(old, new[, count]) -> str，只能从前往后替换，count转换次数，不指定默认替换所有，返回新字符串
```
In [1]: 'i love love you'.replace('love', 'hate')
Out[1]: 'i hate hate you'

In [2]: 'i love love you'.replace('love', 'hate', 1)
Out[2]: 'i hate love you'
```
* S.strip()：S.strip([chars]) -> str，返回去掉()中定义的字符的字符串，默认为空格
* S.lsrip()：使用strip()删除左边指定
* S.rstrip()：使用strip()删除右边指定
```
In [3]: '  i love you  '.strip()
Out[3]: 'i love you'

In [4]: '  i love you  '.rstrip()
Out[4]: '  i love you'

In [5]: '###i love you###'.lstrip('#')
Out[5]: 'i love you###'

In [6]: '{{i love you}}'.lstrip('{}')
Out[6]: 'i love you}}'
```
* S.ljust()：S.ljust(width[, fillchar]) -> str，往左边添加fillchar已满足定义的width，如果S超过width,原样输出S
* S.rjust()：同ljust，往右边添加
```
In [7]: 'love'.ljust(10, '*')
Out[7]: 'love******'

In [8]: 'love'.rjust(10, '*')
Out[8]: '******love'

In [9]: 'lovelovelove'.rjust(10, '*')
Out[9]: 'lovelovelove'
```
* S.center()： S.center(width[, fillchar]) -> str，居中，两边填充fillchar，如果S超过width,原样输出S
```
In [10]: 'love'.center(10, '*')
Out[10]: '***love***'

In [11]: 'lovelovelove'.center(10, '*')
Out[11]: 'lovelovelove'
```
### 字符串查找
S.find：S.find(sub[, start[, end]]) -> int，返回第一次查找到的sub串首字母的索引，从左往右，没有则返回-1
S.rfind：从右往左的find()
    * start：定义开始位置
    * end：定义结束位置，end本身不包含
S.index：功能同S.find，但没有值会抛出ValueError
S.rindex：从右往左的S.index
```
In [12]: s = "love like love" 

In [14]: list(enumerate(s))    # enumerate(sequence, [start=0]), 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），将其组成一个索引序列，同时获得索引和值
Out[14]: 
[(0, 'l'),
 (1, 'o'),
 (2, 'v'),
 (3, 'e'),
 (4, ' '),
 (5, 'l'),
 (6, 'i'),
 (7, 'k'),
 (8, 'e'),
 (9, ' '),
 (10, 'l'),
 (11, 'o'),
 (12, 'v'),
 (13, 'e')]
In [16]: s.find('love')
Out[16]: 0

In [17]: s.find('love', 1, 13)
Out[17]: -1

In [18]: s.find('love', 1, 14)
Out[18]: 10

In [19]: s.index('love', 1, 14)
Out[19]: 10

In [20]: s.rindex('love')
Out[20]: 10
```
S.count：S.count(sub[, start[, end]]) -> int，返回sub在S中的统计数量
```
In [21]: s.count('love')
Out[21]: 2

In [22]: s.count('lover')     # 不存在，返回0
Out[22]: 0
```
### 字符串判断
* S.startwith()：是否以prefix开头
* S.endwith()：是否以prefix结尾
* S.isalpha()：判断字符是否为英文字母
* S.isalnum()：字母或数字
* S.isdigit()：数字
* S.isspace()：空格
* S.isidentifier()：判断字符串是否是合法的标识符，字符串仅包含中文字符合法
```
In [24]: 'love like love'.startswith('love')
Out[24]: True

In [25]: 'love like love'.endswith('like')
Out[25]: False

In [27]: 'love'.isidentifier()
Out[27]: True
```

## 字符串格式化
* join连接
* '+'连接
* printf style
* format方法
### printf style
**基本的用法是将一个值插入到一个有字符串格式符(如%s，%d)的字符串中**
* Python字符串格式化符号 http://www.runoob.com/python3/python3-string.html
```
    %%   输出一个%号
    %c	 字符及其ASCII码
    %s	 字符串
    %d	 整数
    %u	 无符号整型
    %o	 无符号八进制数
    %x	 无符号十六进制数
    %X	 无符号十六进制数，大写字符
    %f	 浮点数字，可指定小数点后的精度 .3%f
    %e	 用科学计数法浮点数
    %E	 作用同%e，用科学计数法格式化浮点数
    %g	 %f和%e的简写，自动选择
    %G	 %f 和 %E 的简写，自动选择
    %p	 用十六进制数格式化变量的地址

    \*   定义占位符宽度，%8d
    .*   定义小数点后的位数
    -    左对齐，%-d
    0    补0
```

### format方法
**Python3更推荐的方法**
#### 基本用法
S.format(*args, **kwargs) -> str
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
```
In [1]: 'i love {}'.format('it')
Out[1]: 'i love it'

In [2]: 'love {}, love {} {}'.format('her','her','dog')
Out[2]: 'love her, love her dog'

In [4]: 'love {0}, love {1} {2}'.format('her','her','dog')
Out[4]: 'love her, love her dog'

In [6]: 'love {0}, love {0} {1}'.format('her','dog')
Out[6]: 'love her, love her dog'

In [7]: 'love {name}, love {name} {animal}'.format(name='her',animal='dog')    # 通过关键字参数
Out[7]: 'love her, love her dog'

In [8]: test = ['her','dog']

In [10]: 'love {test[0]}, love {test[0]} {test[1]}'.format(test)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-10-6367dd35a8d1> in <module>()
----> 1 'love {test[0]}, love {test[0]} {test[1]}'.format(test)

KeyError: 'test'

In [11]: 'love {0[0]}, love {0[0]} {0[1]}'.format(test)    # 注意
Out[11]: 'love her, love her dog'
```
#### 格式限定符 {:[填充]}
```
f/d/s/b/d/o/x：同printf      
^      居中
<      左对齐
>      右对齐
*      占位符宽度
.*     精度
填充   只能是单个字符，不指定使用空格填充
```
```
In [14]: print('1: {0:18} {1:18} {2:<18}'.format('i', 'love', 'python'))
1: i                  love               python            

In [15]: print('1: {0:18} {1:18} {2:<18}'.format('i', 'lovelove', 'python'))
1: i                  lovelove           python            

In [16]: print('1: {0:18s} {1:18d} {2:<18}'.format('i', 'lovelove', 'python'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-16-fed3e702fab8> in <module>()
----> 1 print('1: {0:18s} {1:18d} {2:<18}'.format('i', 'lovelove', 'python'))

ValueError: Unknown format code 'd' for object of type 'str'

In [17]: print('1: {0:18s} {1:18d} {2:<18}'.format('i', 1525, 'python'))     # 数字右对齐
1: i                                1525 python 

In [21]: print('1: {0:18s} {1:18.3f} {2:<18}'.format('i', 1525.555555, 'python'))
1: i                            1525.556 python
```


