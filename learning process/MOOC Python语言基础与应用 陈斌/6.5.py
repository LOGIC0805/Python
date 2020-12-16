def bubbleSort(alist):
    n = len(alist)
    for i in range(n-1):
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                # tmp = alist[j]
                # alist[j] = alist[j+1]
                # alist[j+1] = tmp
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


alist = list(map(int, input().split(' ')))
print(bubbleSort(alist))
