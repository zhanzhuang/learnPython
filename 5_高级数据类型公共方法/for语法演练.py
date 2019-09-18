"""
for 变量 in 集合:
    循环体代码
else:
    没有通过break退出循环，循环结束后，会执行的代码
"""
for num in [1, 2, 3]:
    print(num)
    if num == 3:
        break
else:
    print("else中的代码")
print("循环结束")
