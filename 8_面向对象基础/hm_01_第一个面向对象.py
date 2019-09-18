class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()
print(tom)

addr = id(tom)
print("%d" % addr)  # %d是十进制打印
print("%x" % addr)  # %x是十六进制打印
