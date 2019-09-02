xiaoming_dict = {"name": "小明"}
# 1. 取值
print(xiaoming_dict["name"])

# print(xiaoming_dict["name1"])

# 2. 增加/修改
# 如果key存在就是新增键值对
xiaoming_dict["age"] = 18
# 如果key存在就是修改键值对
xiaoming_dict["name"] = "Jensen"
# 3. 删除
xiaoming_dict.pop("name")

print(xiaoming_dict)
