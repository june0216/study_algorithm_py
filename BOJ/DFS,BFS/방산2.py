import sys
from collections import deque
def bfs(i,j,visit) :
    que = deque([[i,j]])
    melting_que = deque()
    visit[i][j] = 1
    while que :
        i,j = que.popleft()
        melt_cnt = 0
        for d_x, d_y in direction :
            next_x = i + d_x
            next_y = j + d_y
            if 0 <= next_x <= x-1 and 0 <= next_y <= y-1 and visit[next_x][next_y] == 0:

                if glacier[next_x][next_y] != 0:
                    visit[next_x][next_y] = 1
                    que.append([next_x,next_y])

                else :
                    melt_cnt += 1
        if melt_cnt :
            melting_que.append([i,j,melt_cnt])
    return melting_que

input=sys.stdin.readline
year = 0
x, y = map(int,input().split())
glacier = [[int(n) for n in input().split()] for _ in range(x)]
direction = ((1,0),(-1,0),(0,-1),(0,1))

while True :
    cnt = 0
    visit = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x-1) :
        for j in range(y-1) :
            if glacier[i][j] != 0 and visit[i][j] == 0 :
                cnt += 1
                melt = bfs(i,j,visit)
                while melt :
                    m_x, m_y, m = melt.popleft()
                    glacier[m_x][m_y] = max(glacier[m_x][m_y]-m, 0)
    if cnt == 0 :
        year = 0
        break
    if cnt >= 2 :
        break
    year += 1
print(year)