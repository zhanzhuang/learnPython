"""
在开发中，将多个字典放入一个列表中
"""
card_list = [
    {"name": "张三",
     "qq": 123345,
     "phone": 110},
    {"name": "李四",
     "qq": 654321,
     "phone": 120}
]

for card_info in card_list:
    print(card_info)
