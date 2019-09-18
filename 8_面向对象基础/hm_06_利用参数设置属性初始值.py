class Cat:
    def __init__(self, name):
        print("执行 init 方法")

        # self.属性名 = 属性初始值
        # self.name = "Tom"
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用__init__方法
tom = Cat("Tom")
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
