#4, 6, 8, 12, 20

n, m = map(int, input().split())

min_num = min(n, m)
max_num = max(n, m)

res = 0
max = 0
list = []
for i in range(min_num):
    for j in range(max_num):
        list.append(i+j)

for i in range(len(list)):
    tmp = list.count(list[i])
    if max < tmp:
        max  = tmp
        
        