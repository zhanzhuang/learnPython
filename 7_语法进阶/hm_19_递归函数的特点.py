def sum_number(num):
    if num == 0:
        return 0
    return num + sum_number(num - 1)


print(sum_number(100))
