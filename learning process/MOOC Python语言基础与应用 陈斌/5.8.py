n = int(input())
alist = [2]
for i in range(3, n):
    flag = True                 # 重点：标志值的使用方法
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        alist.append(i)
print(alist)
