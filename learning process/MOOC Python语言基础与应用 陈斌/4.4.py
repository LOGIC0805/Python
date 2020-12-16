alist = list(map(int, input().split(' ')))
alist = sorted(alist, key=abs)
print(alist)
