# 1.打开
file_read = open("test.txt")
file_write = open("text[copyBig].txt", "w")

# 2.读之后写
while True:
    text = file_read.readline()
    # 读取到文件末尾break
    if not text:
        break
    file_write.write(text)
# 3.关闭
file_read.close()
file_write.close()

# 一行一行读取写入
