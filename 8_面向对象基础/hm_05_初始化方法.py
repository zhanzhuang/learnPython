class Cat:
    def __init__(self):
        print("执行 init 方法")

        # self.属性名 = 属性初始值
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用__init__方法
tom = Cat()
tom.eat()
print(tom.name)
