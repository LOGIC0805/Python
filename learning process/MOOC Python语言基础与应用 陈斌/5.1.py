max = int(input())
for i in range(100, max + 1):
    num = str(i)
    flower = 0
    for j in num:
        flower += int(j) ** len(num)
    if flower == i:
        print(flower)
