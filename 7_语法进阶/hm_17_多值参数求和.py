def sum_numbers(*args):
    num = 0
    print(args)
    for i in args:
        num = num + i
    return num


result = sum_numbers(1, 2, 34, 5, 6)
print(result)
