alist = list(map(int, input().split(' ')))
blist = list(map(int, input().split(' ')))
clist = set(alist + blist)      # 利用集合去重
clist = list(clist)
print(sorted(clist))
