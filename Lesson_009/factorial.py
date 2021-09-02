def first_factorial(num):
    if num == 1:
        return num
    factorial_num_minus_1 = first_factorial(num=num - 1)
    return num * factorial_num_minus_1


print(first_factorial(int(input())))
