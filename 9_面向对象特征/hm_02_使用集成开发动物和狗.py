class Animal:
    def eat(self):
        print("chi")

    def drink(self):
        print("he")

    def run(self):
        print("pao")

    def sleep(self):
        print("shui")


class Dog(Animal):
    # def eat(self):
    #     print("chi")
    #
    # def drink(self):
    #     print("he")
    #
    # def run(self):
    #     print("pao")
    #
    # def sleep(self):
    #     print("shui")

    def bark(self):
        print("wangwang")


# 继承：自雷拥有父类的所有方法和属性

# wangcai = Animal()
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
