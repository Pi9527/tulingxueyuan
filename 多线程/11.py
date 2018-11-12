import multiprocessing
import os

def info(title):
    print(title)
    print("module name:", __name__)
    # 得到父进程的id
    print('parent process:', os.getppid())
    # 得到本身进程的id
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

