file = open("test.txt")

while True:
    text = file.readline()
    print(text)
    # 判断是否读取到内容
    if not text:
        break

file.close()
