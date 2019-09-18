"""所以不推荐在对向外界设置属性"""


class Cat:
    def eat(self):
        # 哪一个对象调用的方法 self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
# 使用 .属性名 利用赋值语句就可以了
# tom.name = "Tom"

tom.eat()
tom.drink()
tom.name = "Tom"
