n = int(input())
for i in range(1, n + 1):
    alist = []                  # 使用列表和for循环简化代码
    for j in range(1, i):
        if i % j == 0:
            alist.append(j)
    if i == sum(alist):
        print(i)
