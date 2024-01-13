from collections import deque

q = deque()
col, row, height = map(int, input().split())

# 토마토 저장소
tomato = [[list(map(int, input().split())) for _ in range(row)] for _ in range(height)]

# 날짜 저장소
day = [[[0] * col for _ in range(row)] for _ in range(height)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 익은 토마토 큐에 저장
for i in range(height):
    for j in range(row):
        for k in range(col):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()
    for i in range(6):
        xx = x + dx[i]
        yy = y + dy[i]
        zz = z + dz[i]
        if 0 <= xx < height and 0 <= yy < row and 0 <= zz < col and tomato[xx][yy][zz] == 0:
            tomato[xx][yy][zz] = 1
            day[xx][yy][zz] = day[x][y][z] + 1
            q.append((xx, yy, zz))

flag = 1
for i in tomato:
    for j in i:
        if 0 in j:
            flag = 0

res = 0
for i in day:
    for j in i:
        day_max = max(j)
        res = max(res, day_max)

if flag == 1:
    print(res)
else:
    print(-1)