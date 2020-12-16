def hcf(num1, num2):
    while num1 != num2:
        if num1 < num2:
            # tmp = num1
            # num1 = num2
            # num2 = tmp
            num1, num2 = num2, num1
        num1 -= num2
    return num1


num1 = int(input())
num2 = int(input())
print(hcf(num1, num2))
