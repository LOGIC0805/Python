import math

a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2                               # 注意：Python除法生成的值为float类型
area = math.sqrt(p * (p-a) * (p-b) * (p-c))
print('%.2f' % area)
