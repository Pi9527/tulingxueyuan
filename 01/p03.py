#
# class Student():
#     name = "dana"
#     age = 18
#
#     # 注意say的写法，参数有一个self
#     def say(self):
#         self.name = "aaaa"
#         self.age = 200
#         print("My name is {0}".format(self.name))
#         print("My age is {0}".format(self.age))
#
# yueyue = Student()
# yueyue.say()
#
# class Teacher():
#     name = "dana"
#     age = 19
#
#     def say(self):
#         self.name = "yaona"
#         self.age = 17
#         print("My name is {0}".format(self.name))
#         # 调用
#         print("My age is {0}".format(self.age))
#     def sayAgain():
#         print("Hello, nice to see you again")
#     def sayAgain1():
#         print(__class__.name)
#         print(__class__.age)
#         print("Hello, nice to see you again")
#
# t = Teacher()
# t.say()
# # 调用绑定类函数使用类名
# Teacher.sayAgain()
# t.sayAgain1()
# t.sayAgain()

# 关于self的案例
class A():
    name = "aaa"
    age = 11

    # 构造函数
    def __init__(self):
        self.name = "sss"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "ccc"
    age = 90

a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()

# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)

# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

# 以上代码，利用了鸭子模型，像鸭子，有鸭子的属性，就是鸭子