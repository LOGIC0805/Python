datastrs = input().split('.')
result = []
for datastr in datastrs:
    data = int(datastr)
    datastr = []
    while(data >= 2):
        res = data % 2
        data //= 2
        datastr.append(str(res))
    datastr.append(str(data))
    lenth = len(datastr)
    for i in range(8-lenth):
        datastr.append('0')
    result.append("".join(datastr[::-1]))
print("".join(result))