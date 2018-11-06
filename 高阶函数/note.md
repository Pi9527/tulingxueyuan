```python
# 变量可以赋值
a = 100
b = a

# 函数名称就是一个变量
def funcA():
    print("funcA")
funcB = funcA
```
### 以上代码得出结论
- 函数名称是变量
- funcB和funcA只是名称不一样而已
- 既然函数名称是变量,则应该可以被当做参数传入另一个参数
```python
# 高阶函数举例
# funcA是普通函数,返回一个传入数字的100倍数

def funcA(n):
    return  n * 100
def funcB(n):
    return funcA(n) * 3
print(funcB(9))  

# 写一个高阶函数
def funcC(n, f):
    # 假定函数是把n扩大100倍
    return f(n) * 3
print(funcC(9, funcA))

# 比较funcC和funcB,显然funcC的写法要优于funcB
# 例如
def funcD(n):
    return n*10
# 需求变更,需要把n方法三十倍,此时funcB则无法实现
print(funcC(7, funcD)
```
### 系统高阶函数 - map
- 原意就是映射,即把集合或者列表的元素,每一个元素都按照一定规则进行操作,生成一个新的列表或者集合
- map函数是系统提供的具有映射功能的函数,返回值是一个迭代对象
```python
# map举例
# 有一个列表,想对列表里的每一个元素乘以10, 并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)

# 利用map实现
def mulTen(n):
    return n*10
l3 = map(mulTen, l1)
print(l3)
```
### reduce
- 原意是归并,缩减
- 把一个可迭代对象最后归并成一个结果
- 对于作为参数的函数有要求:必须有两个参数,必须有返回结果
- reduce([1,2,3,4,5]) == f(f(f(f(1,2)3)4)5)
- reduce需要导入functools包
```python
from functools import reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd, [1,2,3,4,5,6])
print(rst )

```

### 高阶函数 - 排序
- 把一个序列按照给定算法进行排序
- key:在排序前对每一个元素进行key函数运算,可以理解成按照key函数定义的逻辑进行排序
- python2和python3差别巨大
```python
# 排序案例
a = [123,345,123124,2134345,23,4356,567,1232]
al = sorted(a,reverse=True)
print(al)
# 排序案例2
a = [-23,234,56,4,-2154,-576,2]
# 按照绝对值进行排序
# abs是求绝对值的意思
# 即按照绝对值的倒叙排列
al = sorted(a, key=abs, reverse=True)
print(al)

# sorted案例
astr = ['dana', 'Danna', 'woaini']
satr1 = sorted(astr)
print(satr1)
str2 = sorted(astr, key=str.lower)
print(str2)
```
## 返回函数
- 函数可以返回具体的值
- 也可以返回一个函数作为结果
```python
# 定义一个普通函数
def myF():
    print('In myF')
    return None
a = myF(8)
print(a)

# 函数作为返回值返回,被返回的函数在函数体内定义
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3
# 使用上面定义
# 调用myF2,返回一个函数myF3,赋值给f3
f3 = myF2()
print(f3)
f3()


# 复杂一点的返回函数的例子
# args:参数列表
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5
f5 = myF4(1,2,3,4,5,6,7,8,9,0)
# f5的调用方式
f5()
```
## 闭包(closure)
- 当一个函数在内部定义函数,并且内部的函数应用外部函数的参数或者局部变量,当内部函数被当做返回值的时候,相关参数和变量保存在返回的
函数中,这种结果,叫做闭包
- 上面定义的myF4是一个标准闭包结构
```python
# 闭包常见的坑
def count():
    # 定义列表,列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
```
### 出现的问题:
- 造成上述状况的原因是,返回函数引用了变量i,i并非立即执行,而是等到三个函数都返回的时候才统一使用,此时i已经变成了3,最终调用的
时候,都返回的是3*3
- 此问题描述成,返回闭包时,返回函数不能引用任何循环变量
- 解决方案:再创建一个函数,用该函数的参数绑定循环变量的当前值,无论该循环变量以后如何改变,已经绑定的函数参数值不再改变
```python
# 修改上述函数
def count2():    
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())
```
### 装饰器
- 在不改动函数代码的基础上无限制扩展函数功能的一种机制,本质上讲,装饰器是一个返回函数的高阶函数
- 装饰器的使用: 使用@语法,即在每次要扩展到函数定义前使用@+函数名
```python
# 任务
# 对hello函数进行功能扩展,每次执行hello完打印当前时间
import time
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper

# 上面定义了装饰器,使用的时候需要用到@,此符号是Python的语法糖
@printTime
def hello():
    print("hello world")
hello()

```
# 转jupyter notebook装饰器
