set1 = set(input())         # 可直接转换为set，省略中间无用步骤
set2 = set(input())
print(sorted(set1 | set2))
