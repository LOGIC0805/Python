n = int(input())
sum = 0
for i in range(n + 1):
    if not ('7' in str(i) or i % 7 == 0):   # 逆向判断，省略中间无用代码
        sum += i ** 2
print(sum)
