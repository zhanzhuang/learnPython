"""
字符串、列表、元组可以使用+
字典不可以
"""
print([1, 2] * 5)

print((1, 3) * 2)

print("hello" + "python")

print([1, 2] + [2, 3, 4])

print((1, 2) + (2, 3, 4))

t_list = [1, 2, 0]
t_list.extend([2, 3, 4])
print(t_list)

t_list.append(0)
print(t_list)
t_list.append([8, 9])
print(t_list)
"""
成员运算符
"""
print("a" in "abcd")
print("e" not in "abcd")

print(1 in [0, 1, 2])
print(5 not in [0, 1, 2])

print("a" in {"a": "老王"})  # 针对key
