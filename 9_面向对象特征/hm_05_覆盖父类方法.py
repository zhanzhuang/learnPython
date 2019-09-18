class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    def bark(self):
        print("嗷嗷叫")


xtq = XiaoTianQuan()
# 子类重写父类方法
xtq.bark()
