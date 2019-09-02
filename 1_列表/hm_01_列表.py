name_list1 = ["jensen", "tom", 123]
name_list2 = ["public", "static"]
name_list1.extend(name_list2)
print(name_list1)

name_list1.insert(0, "one")
print(name_list1)

name_list1.append("end")
print(name_list1)

del name_list1[0]
print(name_list1)

name_list1.remove("jensen")
print(name_list1)

name_list1.pop()
print(name_list1)

print(name_list1.__len__())

print(name_list1.count(123))

# print(name_list1.reverse())

# print(name_list1.sort())

print(name_list1.index("static"))

