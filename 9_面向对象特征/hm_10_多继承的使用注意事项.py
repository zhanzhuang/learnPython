class A:
    def test(self):
        print("A ---test 方法")

    def demo(self):
        print("A ---demo 方法")


class B:
    def test(self):
        print("B ---test 方法")

    def demo(self):
        print("B ---demo 方法")


# A、B有同名方法，子类会调用前面的方法
# class C(A, B):
class C(B, A):
    """多继承可以让子类对象同时具有多个父类的属性和方法"""
    pass


c = C()
c.test()
c.demo()

# 确定C类调用方法的顺序
# 如果C中没有，则在B中找，B中没有在C中找
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__mro__)