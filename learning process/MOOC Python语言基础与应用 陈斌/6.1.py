def fbnq(n):
    fblist = [1, 1]
    for i in range(2, n):
        fblist.append(fblist[i-1] + fblist[i-2])
    return fblist[n-1]


n = int(input())
print(fbnq(n))
