import sys
input = sys.stdin.readline

st_num, q_num = map(int, input().split())
st_list = [list(input().split()) for _ in range(st_num)]

for _ in range(q_num):
    q_list = input().split()
    res = 0
    for st in st_list:
        flag = 0
        for i in range(3):
            if st[i] == q_list[i] or q_list[i] == '-':
                flag +=1
        if flag == 3:
            res +=1
    print(res)

