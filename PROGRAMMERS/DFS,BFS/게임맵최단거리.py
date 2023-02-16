from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    X = len(maps[0])
    Y = len(maps)
    visited = [[False]*X for _ in range(Y)]
    visited[0][0] = True
    qu = deque()
    qu.append((0, 0))
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < X and 0 <= ny < Y and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    qu.append((nx, ny))
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
    if maps[Y - 1][X - 1] == 1:
        return -1
    else:
        return maps[Y - 1][X - 1]
