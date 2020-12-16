def lcm(num1, num2):
    num_1, num_2 = num1, num2
    while num1 != num2:
        if num1 < num2:
            # tmp = num1
            # num1 = num2
            # num2 = tmp
            num1, num2 = num2, num1
        num1 -= num2
    return int(num_1 * num_2 / num1)


num1 = int(input())
num2 = int(input())
print(lcm(num1, num2))
