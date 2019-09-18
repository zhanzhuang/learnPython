# 1.打开文件
file = open("test.txt")
# 2.读取文件内容
text = file.read()
print(text)
print(text.__len__())
print("-" * 50)
# 第二次读取文件内容不会输出,因为文件指针已经从开始位置移动到结束位置
text2 = file.read()
print(text2)
print(text2.__len__())
# 3.关闭文件
file.close()
