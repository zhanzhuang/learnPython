# 1.打开
file_read = open("test.txt")
file_write = open("text[copySmall].txt", "w")

# 2.读之后写
text = file_read.read()
file_write.write(text)
# 3.关闭
file_read.close()
file_write.close()
# 一次性读取文件
