s = str(input())
n = int(input())
# 注意：题意中n可能大于s的长度，每s个长度回到原字符串，为一个周期
while n > len(s):
    n -= len(s)
frt = s[0:n]
scd = s[n:]
print(scd+frt)
