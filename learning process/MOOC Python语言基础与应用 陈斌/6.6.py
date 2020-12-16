def foo(alist):
    blist = []
    n =len(alist)
    for i in range(1, n, 2):
        blist.append(alist[i])
    return blist


alist = list(map(int, input().split(' ')))
print(foo(alist))
