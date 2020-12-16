import math

a = int(input())
b = int(input())
c = math.sqrt(a**2+b**2)        # 注意： math.sqrt()函数的返回值为float类型
print(round(a*b/c, 2))
