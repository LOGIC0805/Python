alist = list(map(int, input().split(' ')))
for i in range(len(alist)):
    if alist[i] % 2 == 0:
        alist[i] = int(alist[i] / 2)        # 已经是偶数，不用//而用/即可，注意类型转换
    else:
        alist[i] **= 2
print(sorted(alist))
