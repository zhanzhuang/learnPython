def demo(num, *nums, **person):
    print(num)
    print("-------------")
    print(nums)
    print("-------------")
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5)
gl_dict_person = {"name": "小明",
                  "age": 18,
                  "sex": "男"}
demo(1, 2, 3, 4, 5, name="小明", age=18)
