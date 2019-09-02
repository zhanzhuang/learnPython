name_list = ["jensen", "tom", "jack", "Sam", "jensen"]

list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len )
count = name_list.count("jensen")
print("张三出现了 %d 次" % count)

# 从列表中删除元素
name_list.remove("jensen1")

print(name_list)