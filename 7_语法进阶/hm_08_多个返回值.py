def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")
    # 元组-可以包含多个数据，所以可以使用元组
    # 如果返回类型是元组，小括号可以省略
    # return [temp,wetness]
    return temp, wetness


result = measure()
print(result)
print(type(result))
# 单独拿到温度、湿度
print(result[0])
print(result[1])
# 如果函数返回的类型是元组，同时希望单独处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数应该和元组个数一样
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
