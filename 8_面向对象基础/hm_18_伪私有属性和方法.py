class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 私有属性在对象方法内部可以访问
        print("%s 的年龄是 %d" % (self.name, self.__age))


# 在属性、方法前面加上【__】就变成私有的了

xiaofang = Women("小芳")


# 在给属性、方法命名时，实际是对属性做了一些特殊处理，使得外界无法访问到
# 处理方法：在名称前面加上【_类名=>_类名__名称】
print(xiaofang._Women__age)
xiaofang._Women__secret()