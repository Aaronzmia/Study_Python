# Hello World
**尊重传统，将这一句作为开始**
```python
In [1]: print("Hello World")
Hello World
```

# 变量与常量
## 字面含义：非标准
**常量**：一旦赋值，就不可再改变，换句话说，就是不能对它重新赋值；**python没有真正的常量**  
**字面常量**：一个单独出现的量，未赋值给任何变量或常量  
**变量**：是一个名字，再赋值符号"="的左边，可以指代赋值符号右边的内容，一段地址内存的引用
## 命令规则
1. 只能包含字母、数字、下划线  
2. 可以以字母或下划线开头，但不能以数字开头  
3. 不能包含空格，也不要将Python关键字和函数名用作变量名，如print  
4. 下划线开头的变量名有特殊含义：  
    * _：单独的下划线作为临时时用，后续不会再次使用  
    * _Name：被看作“私有的”，在模块或类外不可以使用，不能’from module import *’导入
    * \_\_Name\_\_：以双下划线开头和结尾的代表python里特殊方法专用的标识
5. 更多可以看看：PEP8--Python的代码风格 http://www.jianshu.com/p/2a573f846af9
```python
In [4]: Var_Name = "5abc"  # python中，除了代码缩进外的空格无意义

In [5]: 5Var = "5abc"  # 不能以数字开头
  File "<ipython-input-5-cd37b3b67a94>", line 1
    5Var = "5abc"
       ^
SyntaxError: invalid syntax
```

# Python的类型系统
* Python是**强类型**语言：不同类型之间不能相互计算，运算的时候会做类型检查
```
In [6]: 2 + 'a'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-4a87aa4cef8b> in <module>()
----> 1 2 + 'a'

TypeError: unsupported operand type(s) for +: 'int' and 'str'

In [7]: 2 + 2
Out[7]: 4

In [8]: 'a' + 'a'
Out[8]: 'aa'
```
* python是**动态类型**语言：变量可以重新赋值为其他类型
```python
In [9]: var = 520

In [10]: type(var)
Out[10]: int

In [11]: var = "love"

In [12]: type(var)
Out[12]: str

In [13]: var = love
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-4f38a4f54d29> in <module>()
----> 1 var = love

NameError: name 'love' is not defined
```

