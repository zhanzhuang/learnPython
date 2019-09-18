class Cat:

    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


# tom是一个全局变量
tom = Cat("Tom")
# 希望输出的是自己控制的信息，则定义str方法
print(tom)
