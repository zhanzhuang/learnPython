def demo(num, num_list):
    print("函数开始")
    # num = num + num
    num += num
    # 列表变量使用+=不会进行+=操作
    # 本质上是在调用列表的extend方法
    # × num_list = num_list + num_list
    num_list = num_list + num_list
    # num_list += num_list
    print(num)
    print(num_list)
    print("函数完成")


gl_num = 9
gl_num_list = [1, 2, 3]
demo(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
