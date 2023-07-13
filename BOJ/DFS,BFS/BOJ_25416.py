from collections import deque
table = []
for i in range(5):
    table.append(list(map(int, input().split())))
start_x, start_y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*5 for _ in range(5)]

cnt = 0
def bfs(x, y):
    qu = deque()
    qu.append((x, y, 0))
    visited[x][y] = True
    flag = 0


    while qu:
        x, y, cnt = qu.popleft()
        if table[x][y] == 1:
            print(cnt)
            flag = 1
            break
        for j in range(4):
            nx = dx[j] + x
            ny = dy[j] + y
            if nx < 0 or ny < 0 or ny >= 5 or nx >= 5 or table[nx][ny] == -1 or visited[nx][ny]:
                continue

            qu.append((nx, ny, cnt + 1))
            visited[nx][ny] = True
    if flag == 0:
        print(-1)
bfs(start_x, start_y)




