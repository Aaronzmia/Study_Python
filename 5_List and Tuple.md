# 列表
## 初使化
```
lst = list()  **使用List函数定义空列表，在转化为可迭代对象为列表时使用**
lst = []  **使用中括号定义空列表，建议使用**
lst = [COL1, COL2, ...]  **使用中括号定义带初始值的列表**
lst = list(range(start, stop))  **使用list函数把可迭代对象转化为列表**
```
## 列表访问及查找
* 通过索引下标访问，从前王后访问，下标从0开始
* 负数索引表示从后往前开始计数，由-1开始，-1表示最后一个元素 
* 当索引超出范围时，会抛出IndexError异常
* lst.index(value, [start, [stop]])：
    * 返回第一个查找到的元素
    * start参数指定从哪个所引开始查找
    * stop参数指定到哪个索引结束，并且不包含该索引
    * 当值不存在该范围的时候，会抛出ValueError
    * start和stop参数可以为负数，但是总是从左往右查找
    * 凡是stop比start小，总是抛出ValueError，相当于在空列表查询

```
In [1]: lst = [0, 1, 2, 3, 4]

In [2]: lst[-1] 
Out[2]: 4

In [3]: lst[-2] 
Out[3]: 3

In [4]: lst[0] 
Out[4]: 0

In [5]: lst[1] 
Out[5]: 1

In [6]: lst[100] 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-6-772ced463bc4> in <module>()
----> 1 lst[100]

IndexError: list index out of range

In [7]: lst[-100] 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-7-d090137bc7d0> in <module>()
----> 1 lst[-100]

IndexError: list index out of range

In [1]: lst = [1, 3, 5, 7, 5, 11]

In [2]: lst.index(5, 1, 4)
Out[2]: 2

In [3]: lst.index(5, 0, 2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-a461605461ec> in <module>()
----> 1 lst.index(5, 0, 2)

ValueError: 5 is not in list

```

## 列表方法
### 添加元素
* append(object)：原地修改添加元素到list结尾，返回None，不返回新列表
* insert(index, object)：在index前插入元素，返回None，不返回新列表
    * 索引为负数，会在第0个元素前插入
    * 索引正数，会在最后一个元素后插入
* extend(iterable)：将可迭代对象添加到list结尾，返回None，不返回新列表
* +：不修改list本身，返回一个新的list，list的连接操作，会开辟新的内存，调用__add__()
```
In [2]: lst = [1, 2, 3, 4, 5]

In [3]: lst.append('a') # O(1)，常数时间，效率与数据规模无关

In [4]: lst.insert(-1, 'b') # O(n)，线性时间，效率与数据规模线性相关 

In [5]: lst
Out[5]: [1, 2, 3, 4, 5, 'b', 'a']

In [6]: lst.extend(range(3))

In [7]: lst
Out[7]: [1, 2, 3, 4, 5, 'b', 'a', 0, 1, 2]

In [8]: lst + ['c', 'd']   # 直接返回新列表
Out[8]: [1, 2, 3, 4, 5, 'b', 'a', 0, 1, 2, 'c', 'd']
```
### 删除元素
* remove(value)：原地删除第一次出先的value，value不存在抛出ValueError
* pop([index])：返回并删除index所在的元素，默认删除返回最后一个
* clear()：删除列表所有元素，返回None，不返回新列表
```
In [10]: lst
Out[10]: [1, 2, 3, 4, 5, 'b', 'a', 0, 1, 2]

In [11]: lst.pop()
Out[11]: 2

In [12]: lst
Out[12]: [1, 2, 3, 4, 5, 'b', 'a', 0, 1]

In [13]: lst.pop(100)   # 索引超出范围，抛出IndexError
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-19-795b88347eea> in <module>()
----> 1 lst.pop(100)

IndexError: pop index out of range

In [14]: lst.remove(5)

In [15]: lst
Out[15]: [1, 2, 3, 4, 'b', 'a', 0, 1]

In [16]: lst.clear()

In [17]: lst
Out[17]: []

In [20]: lst.remove(10)   # value不村在，抛出异常
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-20-0db5c9e7363a> in <module>()
----> 1 lst.remove(10)

ValueError: list.remove(x): x not in list
```
### 删除列表
* del()：删除整个列表
```
In [1]: lst = [1, 2, 3, 2, 4, 2]

In [2]: del(lst)

In [3]: lst
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-24034128ed43> in <module>()
----> 1 lst

NameError: name 'lst' is not defined
```
### 统计元素
* count(value)：返回列表中value出现的次数
```
In [21]: lst = [1, 2, 3, 2, 4, 2]

In [22]: lst.count(2)
Out[22]: 3
```
### 计算长度
* len()
```
In [21]: lst = [1, 2, 3, 2, 4, 2]

In [23]: len(lst)
Out[23]: 6
```
### 翻转与排序
* reverse()：原地翻转列表
* sort()   
    * key 是带一个参数的函数, 用来为每个元素提取比较值. 默认为 None, 即直接比较每个元素
    * reverse 表示是否逆序排序，默认为False
```
In [24]: lst
Out[24]: [1, 2, 3, 2, 4, 2]

In [25]: lst.reverse()

In [26]: lst
Out[26]: [2, 4, 2, 3, 2, 1]

In [27]: lst.sort()

In [28]: lst
Out[28]: [1, 2, 2, 2, 3, 4]

In [29]: lst.sort(reverse=True)

In [30]: lst
Out[30]: [4, 3, 2, 2, 2, 1]
```
### 列表复制
* 浅拷贝：=，赋值操作传递的是引用，同一个内存地址
* 影子拷贝：copy()，只拷贝父对象，不会拷贝对象的内部的子对象
* 深拷贝：copy.deepcopy()，拷贝对象及其子对象
```
import copy  
a = [1, 2, 3, 4, [1, 2]] #原始对象  

b = a # 赋值，传引用  
c = copy.copy(a) # 浅拷贝  
d = copy.deepcopy(a) # 深拷贝  

a.append(5) #修改对象a  
a[4].append(3) # a[4]的列表中添加元素  

print('a = ', a)  
print('b = ', b)  
print('c = ', c)  
print('d = ', d)  

a =  [1, 2, 3, 4, [1, 2, 3], 5]
b =  [1, 2, 3, 4, [1, 2, 3], 5]
c =  [1, 2, 3, 4, [1, 2, 3]]
d =  [1, 2, 3, 4, [1, 2]]     # deepcopy未改变
```

# 元组
## 初始化定义
```
t = tuple()
t = ()
t = (1, 2, 3)
t = tuple(range())
```
## 元组与列表的不同
**元组中的元素不可修改**
```
In [1]: t = (1, 2, 3, 4, 5)

In [2]: t[1]
Out[2]: 2

In [3]: t[1] = 5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-e9323da3946c> in <module>()
----> 1 t[1] = 5

TypeError: 'tuple' object does not support item assignment
```
## 元组的方法
### 修改元组
* \+：元组中的元素不可以修改，但是可以使用‘+’号连接组合，但是返回的是新元组
```
In [1]: t1 = (1, 2, 3)

In [2]: t2 = ('a', 'b', 'c')

In [3]: t1 + t2
Out[3]: (1, 2, 3, 'a', 'b', 'c')
```
### 删除元组
* del：del可以删除整个元组
```
In [4]: t1
Out[4]: (1, 2, 3)

In [5]: del(t1)

In [6]: t1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-7533422ecb03> in <module>()
----> 1 t1

NameError: name 't1' is not defined

```
### 元组方法
* count()
* index()  
**同列表使用方法一致** 

### 命名元组 namedtuple
* 定义：collections.namedtuple(typename, field_names, verbose=False, rename=False) 
    * typename：要定义的元组名称
    * field_names：定义元组中元素的名称
    * rename：如果元素名称中含有python的关键字，则必须设置为rename=True
```
IIn [6]: Stu = collections.namedtuple('studen', 'name, age, sex')

In [7]: Stu = collections.namedtuple('student', 'name, age, sex')

In [8]: Tom = Stu(name='Tom', age=20, sex='male')

In [9]: Tom
Out[9]: student(name='Tom', age=20, sex='male')

In [11]: Tom.name
Out[11]: 'Tom'

In [12]: Tom.age
Out[12]: 20

同元组一样，元素不可变
```
