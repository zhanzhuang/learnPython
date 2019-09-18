# 使用global关键字修改全局变量的值
gl_number = 10


def demo1():
    global num
    num = 99
    print("demo1==> %d" % num)


def demo2():
    print("demo1==> %d" % gl_number)


demo1()
demo2()
