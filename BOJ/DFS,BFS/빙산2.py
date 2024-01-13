from collections import deque
from copy import deepcopy
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
row, col = map(int, input().split())
ice = []
qu = deque()
#모든 지점 -> 동시에
for r in range(row):
    ice.append(list(map(int, input().split())))
for r in range(row):
    for c in range(col):
        if ice[r][c] == 0:
            qu.append((r, c))

def bfs(idx, idy):
    check_que = deque()
    check_que.append((idx, idy))
    while check_que:
        cx, cy = check_que.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < row and 0 <= ny < col:
                if visited[nx][ny] == False and ice[nx][ny] != 0:
                    check_que.append((nx, ny))
                    visited[nx][ny] = True

result = 0
while True:
    copy_ice = deepcopy(ice)
    flag = 0
    for i in range(row):
        for j in range(col):
            if copy_ice[i][j] == 0:
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < row and 0 <= ny < col:
                        if copy_ice[nx][ny] > 0:
                            ice[nx][ny] -= 1
                            flag = 1

    result += 1
    visited = [[False] * col for _ in range(row)]
    count = 0
    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and ice[i][j] != 0:
                visited[i][j] = True
                bfs(i, j)
                count += 1
    if count >= 2:
        print(result)
        break
    else:
        if flag == 0:
            print(0)
            break


