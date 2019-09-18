a = 6
b = 100

# 解法1： -使用中间变量
# c = a
# a = b
# b = c
# print(a)
# print(b)

# 解法2： -不使用其他变量
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)

# 解法3： --Python解法
# a, b = (b, a)
# a, b = [b, a]
a, b = b, a  # 这里是一个元组，只是把小括号省略了
print(a)
print(b)
