import sys
input = sys.stdin.readline

st_num, q_num = map(int, input().split())

dic = {}
def wild(sub, fruit, color):
    query = sub + fruit + color
    if query.count('-') == 3:
        for key in dic.keys():
            dic[key] += 1
    elif query.count('-') == 2:
        if sub != '-':
            for key in dic.keys():
                if sub in key:
                    dic[key] +=1
        elif fruit != '-':
            for key in dic.keys():
                if fruit in key:
                    dic[key] +=1
        elif color != '-':
            for key in dic.keys():
                if color in key:
                    dic[key] +=1
    else:
        if sub == '-':
            for key in dic.keys():
                if fruit in key and color in key:
                    dic[key] +=1
        elif fruit == '-':
            for key in dic.keys():
                if sub in key and color in key:
                    dic[key] +=1
        elif color == '-':
            for key in dic.keys():
                if sub in key and fruit in key:
                    dic[key] +=1


for num in range(st_num):
    temp = ''.join(input().split())
    dic[temp] = 0

pas = 0
for s in range(q_num):
    sub, fruit, color = input().split()
    query = sub + fruit +color
    if sub in '-' or fruit in '-' or color in '-':
        wild(sub, fruit, color)
    else:
        dic[query] +=1
    print(sum(dic.values()) - pas)
    pas = sum(dic.values())




