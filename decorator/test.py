# coding=utf-8
def log(func):  # func为被装饰的函数，作为参数传递进来
    def wrapper(*args, **kwargs):  # wrapper为实际装饰的功能函数
        print "i'll decorate ", func.__name__  # 功能函数的功能
        return func()  # 返回被装饰的函数

    return wrapper()


@log
def test():  # 定义需要被装饰的函数，也就是上面的func函数
    print "i need to be decorated"


test  # 执行被装饰后的函数,后面不能加（），
'''
当执行test时，实际流程是 log(test) => wrapper() => func()/test(),
如果test后加(),实际流程是 log(test)() => wrapper()() => func()()/test()(),而test函数已经没有return，不能再次被调用，
此时会报 'NoneType' object is not callable
'''
