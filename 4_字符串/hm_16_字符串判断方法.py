# 1. 判断空白字符
space_str = "  \t\n\r"
print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# 2.1都不能判断小数 将123改成123.1
# num_str = "123"
# num_str = "\u00b2"
# num_str = "(1)"
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
