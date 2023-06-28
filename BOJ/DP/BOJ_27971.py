N, lim, A, B = int(input().split())
limit = []
# 1) 목표지점
#2) 행동 최소
#3) 구간
for _ in range(len(limit)):
    limit.append(tuple(int(input().split())))
table = [0 for _ in range(N)]

for num in range(N):
    res = []
    if num < A and num < B:
        table[num] = -1
        continue
    while num >0:
        if num - A >= 0:
            res.append(A)
            num = num - A
        elif num - B >= 0:
            res.append(B)
            num = num - B
    if num == 0:
        table[num] = len(res)
    else:
        table[num] = -1



