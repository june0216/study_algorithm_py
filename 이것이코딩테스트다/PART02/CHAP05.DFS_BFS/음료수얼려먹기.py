N, M = map(int, input().split())
table = []
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    table.append(list(map(int, input())))

visited = [[False]*M for _ in range(N)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N or visited[y][x] == True or table[y][x] == 1:
        return 0
    visited[y][x] = True  # This line was missing in the original code
    for n in range(len(dx)):
        nx = x + dx[n]
        ny = y + dy[n]
        dfs(nx, ny)
    return 1


for j in range(N):
    for k in range(M):
        if visited[j][k] == False:
            answer += dfs(k, j)

print(answer)
