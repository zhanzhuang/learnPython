class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 私有属性在对象方法内部可以访问
        print("%s 的年龄是 %d" % (self.name, self.__age))


# 在属性、方法前面加上【__】就变成私有的了

xiaofang = Women("小芳")
# 私有属性在外界不能访问
# print(xiaofang.__age)

# 私有方法不能在外界访问
# xiaofang.__secret()
