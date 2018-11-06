#1 模块
- 一个模块就是一个包含python代码的文件,后缀名是.py就可以,模块就是python文件
- 为什么用模块
    - 程序太大,编写维护不方便,需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用,避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件,任何代码可以直接书写
    - 不过根据模块的规范,最好在模块中编写以下内容
        - 函数(单一功能)
        - 类(相似功能的组合,或者类似业务模块)
        - 测试代码
- 如何使用模块
    - 模块直接导入
        - 加入模块名称直接以数字开头
            import importlib
            a = importlib.Student("01")
    - 语法
        import module_name
        module_name.function_name
        module_name.class_name
    - 案例 p01,p02
    - import 模块 as 别名
    - from module_name import func_name, class_name
        - 按上述方法有选择性导入
        - 直接使用,不需要前缀
    - from module_name import *
        - 导入模块所有内容
        - 不能有效避免命名污染(带前缀可有效避免)
- 'if __name__ == "__main__"' 的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口
#2 模块的搜索路径和存储
- 什么是模块的搜索路径:
    - 加载模块的时候,系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
    import sys
    sys,path 属性可以获取路径列表   
    (#)案例p03.py 
- 添加搜索路径
    sys.path.append(dir)
- 模块加载顺序
    1.搜索内存中已经加载好的模块
    2.搜索python的内置模块
    3.搜索sys.path的路径

#3 包
- 包是一种组织管理代码的方式,里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构
    /---包
    /---/--- __init__.py  包的标志文件
    /---/--- 模块1
    /---/--- 模块2
    /---/--- 子包(子文件夹)
    /---/---/--- __init__.py 包的标志文件
    /---/---/--- 子包模块1
    /---/---/--- 子包模块2
- 包的导入操作
    - import package_name
        - 直接导入一个包,可以使用__init__.py中的内容
        - 使用方式:
            package_name.func_name
            package_name.class_name.func_name
        - 此种方式访问内容是
        - 案例 pkg01, p04.py
    - impo package_name as p
        - 具体用法和作用方式,与上述简单导入一致
        - 注意的是此种方法时默认对__init__.py内容的导入
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
            package.module.func_name
            package.module.class_name.func()
            package.module.class.var
        - 案例 p05.py
    - impor package.module as pm    
-from ... impor 导入
    - from package import module1, module2.....
    - 此种导入方法不执行"__init__"内容
        from pkg01 import p01
        p01.sayHello()
    - from package import *
        - 导入当前包"__init__.py"文件中所有的函数和类
        - 使用方法
            func_name()
            class_name.func_name()
            class_name.var
        - 案例 p06.py  注意此种导入的具体内容
- from package.module import *
    - 导入包中指定模块的所有内容
    - 使用方法
        func_name()
        calss_name.func_name()
- 在开发环境中经常会引用其他模块,可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径
- "__all__"的用法
    - 在使用from package import * 的时候, * 可以导入的内容
    - "__init__.py"中如果文件为空, 或者没有"__all__", 那么只可以把"__init__"中的内容导入
    - "__init"如果设置了"__all__"的值.那么则按照"__all__"指定的子包或者模块进行导入,如此则不会载入"__init__"中的内容
    - "__all__=["module1", "module2",...]"

#命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突
    setName()
    Student.setName()
    Dog.setNamg()

#4 异常
- 广义上的错误分为错误和异常
- 错误指的是可以人为避免
- 异常是指在语法逻辑正确的前提下,出现的问题
- 在python里,异常是一个类,可以处理和使用
#5 异常处理
- 不能保证程序永远正确运行
- 但是,必须保证程序在最坏的情况下得到的问题被妥善处理
- python的异常处理模块全部语法:
    try:
        尝试实现某个操作
        如果没出现异常,任务就可以完成
        如果出现异常,将异常从当前代码块扔出去,尝试解决异常
    except 异常类型1:
        解决方案1:用于尝试在此处处理异常解决问题
        except 异常类型2:
        解决方案2:用于尝试在此处处理异常解决问题
    except (异常类型1, 异常类型2...):
        解决方案:针对多个异常使用相同的处理方式
    except:
        解决方案:所有异常的解决方案
    else:
        如果没有出现任何异常,将会执行此处代码
    finally:
        不管有没有异常都要执行的代码
    - 示例
        (#)越具体的错误,越往前放
        except ..... as e:
            print()
            print(e)
            exit()
            .
            .
            .
        (#)所有异常都是继承自Exception,下面代码,任何异常都会拦截住          
        except Excepttion as e:
            print()
#6 用户手动引发异常
- 当某些情况,用户希望自己因为一个异常的时候,可以使用
- raise 关键字来引发异常
---
    try:
        print()
        print()
        (#)手动因为一个异常
        (#)注意语法
        raise ValueError
    (#)自定义异常
    (#)注意:自定义异常必须是系统异常的子类
    class DanaError(ValueError):
        pass
---    
    (#)else语句案例
    try:
        num = int(input("Plz input your number:"))
        ret = 100/num
        print("计算结果是: {0}".format(rst))
    except Exception as e:
        print("Exception")
    else:
        print("No Exception")
    finally:
        print("反正要执行我")
 
#7 关于自定义异常
- 只要是raise异常,推荐自定义异常
- 在自定义异常的时候,一般包含以下内容:
    - 自定义异常的异常代码
    - 自定义发生异常后的问题提示
    - 自定义发生异常的行数
- 最终的目的,一旦发生异常,方便程序员快速定位错误现场

#8 常用模块,下述所有模块使用理论上都应该先导入,string是特例
- calendar
    - 跟日历相关的模块
    (#)使用需要先导入
    import calendar
    (#)calendar:获取一年的日历字符串
    (#)w = 每个日期之间的间隔字符数
    (#)l = 每周所占用的行数
    (#)c = 每个月之间的间隔字符数
    cal = calendar.calendar(2017)
    print(type(cal))
    cal = calendar.calendar(2017, l = 0, c = 5) 结果紧凑
---
    (#)isleap:判断某一年是否闰年
    calendar.isleap(2000)
    (#)leapdays:获取指定年份之间的闰年个数
    calendar.leapdays(2001, 2018)
---
    (#)month:获取某个月的日历字符串
    (#)格式:calendar.month(年, 月)
    (#)回值:月日历的字符串
    m3 = calendar.month(2018, 3)
    print(m3)
---
    (#)monthrange: 获取一个月的周几开始和天数
    (#)格式:calendar.monthrange(年, 月)
    (#)回值:元祖(周几开始, 总天数)
    (#)注意:周默认 0 - 6 表示周一到周天
---
    (#)monthcalendar:返回一个月每天的矩阵列表
    (#)格式:calendar.monthcalendar(年, 月)
    (#)回值:二级列表
    (#)注意:矩阵中没有天数用0表示
---
    (#)prcal:直接打印日历
    (#)calendar.prcal(2018)
---
    (#)prmonth:直接打印整个月的日历
    (#)格式:calendar.prmonth(年, 月)
    (#)返回值: 无
---
    (#)weekday:获取周几
    (#)格式:calendar.weekday(年, 月, 日)
    (#)返回值:周几对应的数字,0 - 6 表示周一到周日      
- time
    - 时间戳
        - 一个时间表示,根据不同语言,可以是整数或者浮点数
        - 是从1970年1月1日0时0分0秒到现在的经理的秒数
        - 如果表示的时间是1970年以前或者太遥远的未来,可能出现异常
        - 32位操作系统能够支持到2038年
    - UTC时间
        - 世界标准时间
    - 夏令时
        - 每天变成25小时,本质没变还是24小时
    - 时间元祖
        - 一个包含时间内容的普通元祖
---
    import time
    (#)时间模块的属性
    (#)tinezone:当前时区和UTC时间相差的秒数,在没有夏令时的情况下的间隔
    (#)altzone:获取当前时区与UTC时间相差的秒数,在有夏令时的情况下
    (#)daylight:测当前是否是夏令时时间状态, 0 表示是
    print(time.timezone)
    (#)localtime:得到当前时间的时间结构
    (#可以通过点好操作符得到相应的属性元素的内容
    t = time.localtime()
    print(t.tm_hour)
    (#)asctime:返回元祖的正常字符串化之后的时间格式
    (#)格式:time.asctime(时间元祖)
    (#)返回值:字符串 Tue Jun 6 11:11:00 2017
    t = time.localtime()
    tt = time.asctime(t)
    print(tt)
    (#)ctime:获取字符串化的当前时间
    t = time.ctime()
    (#)mktime:使用时间元祖获取对应的时间戳
    (#)格式:time.mktime(时间元祖)
    (#)返回值:浮点数时间戳
    lt = time.localtime()
    ts = time.mktime(lt)
    print(ts)
    (#)clock:获取cpu时间, 3.0 - 3.3版本直接使用,3.6调用有问题
    (#)sleep:使程序进入睡眠, n秒后继续
    for i in range(10):
        print(i)
        time.sleep(1)
---
- strftime:将时间元祖转化为自定义字符串格式
---
    格式  含义  备注
    %a  本地(locale)简化星期名称
    %A  本地完整星期名称
    %b  本地简化月份名称
    %B  本地完整月份名称
    %c  本地相应的日期和时间表示
    %d  一个月中的第几天(01 - 31)
    .
    .
    .
```python
    (#)把时间表示成: 2018年3月26日 21:05
    t = time.localtime()
    ft = time.strftime("%Y年%m月%d日 %H:%M",t)
    print(ft)  
```    
- datetime
    - 提供日期和时间的运算和表示
    (#) datetime常见属性
    (#) datetime.date:一个理想化的日期,提供year, month, day属性
 ```python
dt = datetime.date(2018, 3,26)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
```
   (#) datetime.time:提供一个理想化的时间,提供hour, minute, sec, microsec等
   (#) datetime.datetime:提供日期跟时间的组合
```python
from datetime import datetime
# 常用类方法
# today
# now
# utcnow
# fromtimestamp:从时间戳中返回本地时间
dt = datetime.date(2018, 3,26)
print(dt.today())
print(dt.now())
print(dt.utcnow())
print(dt.fromtimestamp(time.time()))
```
   (#) datetime.timedelta:提供一个时间差,时间长度
```python
from datetime import datetime, timedelta
t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
td = timedelta(hours=1)
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))
```     

- timeit
    - 时间测量工具
```python
# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间,可能很难实现
c = '''
sum = []
for i in range(1000)
    sum.append(i)
'''
# 利用timeit调用代码,执行100000次,查看运行时间
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
# 测量代码c执行100000次运行结果
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)

```    
- os:操作系统相关
    - 与系统相关的操作,主要包含在三个模块里
        - os, 操作系统目录相关
        - os.path, 系统路径相关操作
        - shutil,高级文件操作,目录树的操作,文件赋值,删除,移动
    - 路径
        - 绝对路径:总是从根目录上开始
        - 相对路径:基本以当前环境为开始的一个相对的地方
```python
    # getcwd()获取当前的工作目录
    # 格式：os.getcwd()
    # 返回值：当前工作目灵的字符串
    # 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
    import os
    mydir = os.getcwd()
    print(mydir)
    # chdir()改变当前的工作目录
    # 格式:os.chdir(路径)
    # 返回值:无
    os.chdir('字符串')
    mydir = os.getcwd()
    print(mydir)
    # listdir()获取一个目录中所有子目录和文件的名称列表
    # 格式:os.listdir(路径)
    # 返回值:所有子目录和文作名称的列表
    ld = os.listdir()
    print(ld)
    ****** 识别结果 1******

    # makedirs()递归创建文件荚
    # 格式:os.makedirs(路径)
    # 近回值：无
    # 递归路径:多个文件夹层层包含的路径就是递归路径,例如a/b/c...
    rst = os.makedirs("dana")
    print(rst)
    # system()运行系统shell命令
    # 格式:os.system(系统命令)
    # 返回值:打开一个shell或者终端界面
    # ls是列出当前文件和文件夹的系统命令
    rst = os.system("ls")
    print(rst)
```


- shutil
- zip
- math
- string
- 