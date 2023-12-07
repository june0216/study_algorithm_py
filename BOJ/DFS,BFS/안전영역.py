import sys
sys.setrecursionlimit(100000)
N = int(input())
area = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_val = 0
min_val = sys.maxsize

for _ in range(N):
    area.append(list(map(int, input().split())))
    min_val = min(min_val, min(area[-1]))
    max_val = max(max_val, max(area[-1]))


def dfs(x, y,  rain):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny]== False and area[nx][ny] > rain:
                visited[nx][ny] = True
                dfs(nx, ny, rain)


result = 0

for rain in range(min_val, max_val):
    cnt = 0
    visited =  [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and area[i][j] > rain:
                visited[i][j] = True
                dfs(i, j,rain)
                cnt+=1
    result = max(cnt, result)

print(result)