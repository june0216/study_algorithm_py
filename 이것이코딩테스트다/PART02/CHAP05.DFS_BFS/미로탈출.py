from collections import deque
Y, X = map(int, input().split())
table = []
for i in range(Y):
    table.append(list(map(int, input())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * X for _ in range(Y)] # 방문 리스트를 따로 만들지 않고 그냥 table의 값이 1이면 방문 안한 것이라고 생각하고 진행할 수 있음
def bfs(x, y):
    qu = deque()
    qu.append((x, y))
    visited[y][x] = True
    count = 0
    while qu:
        x, y = qu.popleft()

        for n in range(4):
            nx = dx[n] + x
            ny = dy[n] + y
            if nx < 0 or ny < 0 or nx >= X or ny >= Y or visited[ny][nx] == True:
                continue
            if table[ny][nx] != 0:
                qu.append((nx, ny))
                visited[y][x] = True
                table[ny][nx] = table[y][x] + 1
            count +=1
    return table[Y-1][X-1]

print(bfs(0, 0))
