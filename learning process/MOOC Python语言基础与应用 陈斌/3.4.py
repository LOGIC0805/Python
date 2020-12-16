s = str(input())
str_list = s.split(' ')
str_list[0] = str_list[0].lower()       # 注意：题目要求不区分大小写
str_list[1] = str_list[1].lower()
cnt = str_list[0].count(str_list[1])
print(cnt)
