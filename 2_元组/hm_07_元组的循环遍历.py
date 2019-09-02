info_tuple = ("张三", 18, 1.123)

for item in info_tuple:
    # 使用格式字符串拼接item这个变量不方便！
    # 因为元组中通常保存的数据类型是不同的！
    print(item, end="")
