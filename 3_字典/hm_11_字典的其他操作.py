xiaoming_dict = {"name": "小明",
                 "age": 18}

# 1 统计键值对的数量
print(len(xiaoming_dict))

# 2 合并字典，如果被合并的字典已经包含存在的键值对
# 会覆盖之前的键值对
temp_dict = {"height": 1.75,
             "age": 111}
xiaoming_dict.update(temp_dict)

# 3 清空字典
xiaoming_dict.clear()
# print(xiaoming_dict.items())
# print(xiaoming_dict.keys())
# print(xiaoming_dict.values())

print(xiaoming_dict)
