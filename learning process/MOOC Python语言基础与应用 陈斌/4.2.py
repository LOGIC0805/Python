alist = list(map(int, input().split(' ')))
n = int(len(alist) / 2)                     # 注意类型转换
value1 = alist[0:n]
value2 = alist[n:]
print({'1': value1, '2': value2})
