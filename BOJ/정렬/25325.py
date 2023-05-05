n = int(input())
name_list = list(input().split())

name_dic = dict.fromkeys(name_list, 0)

for _ in range(n):
    like_list = list(input().split())
    for name in like_list:
        name_dic[name] +=1
result = sorted(name_dic.items(), key=lambda x: (-x[1], x[0])) #sorted, sort 차이
for key, val in result:
    print(str(key) + " " + str(val))
