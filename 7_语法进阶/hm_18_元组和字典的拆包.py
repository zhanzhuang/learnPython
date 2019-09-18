def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = (1, 2, 3)  # 元组变量
gl_dict = {"name": "小明", "age": 18}  # 字典变量

# 拆包的语法：元组前一个*、字典前两个*
demo(*gl_nums, **gl_dict)
