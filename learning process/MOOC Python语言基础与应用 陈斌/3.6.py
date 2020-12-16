import math

r = int(input())
cir = 2 * r * round(math.pi, 5)         # 注意：math库中pi常量的调用
area = r ** 2 * round(math.pi, 5)
print(round(cir, 4), round(area, 4))
