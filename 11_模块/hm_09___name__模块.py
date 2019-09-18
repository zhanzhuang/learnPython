# 模块可以提供全局变量 函数 类
# 注意：直接执行的代码不是向外界提供的工具


def say_hello():
    print("你好你好，我是 say hello")


# 不加__main__的时候其他模块导入本模块会执行
# 加上__main__之后其他模块导入本模块就不会执行
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行
    print("小明开发的模块")
    say_hello()
"""
主程序的正确写法
def main():
    pass
if __name__ == "__main__":
    main()
"""
