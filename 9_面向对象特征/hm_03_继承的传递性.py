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


xtq = XiaoTianQuan()
xtq.fly()  # 自己的方法
xtq.bark()  # 狗的方法
xtq.run()  # 动物类方法
