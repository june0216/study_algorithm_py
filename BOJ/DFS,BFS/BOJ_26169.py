from collections import deque

table = []
for i in range(5):
    table.append(list(map(int, input().split())))
start_y, start_x = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*5 for _ in range(5)]


def backtrack(x, y, count, apple):
    if apple >= 2 and count <= 3:
        return 1

    if count >= 3 and apple < 2:
        return 0

    result = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >= 0 and ny >= 0 and nx < 5 and ny < 5 and table[nx][ny] != -1:
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            temp = table[nx][ny]
            if table[nx][ny] == 1:
                apple += 1
            table[nx][ny] = -1
            result = max(result, backtrack(nx, ny, count + 1, apple)) # 모든 경우의 수를 탐색 후 1이 되는 경우가 있으면 있다고 판단
            visited[nx][ny] = False # 복구
            table[nx][ny] = temp  # 복구
    return result

apple = 0
if table[start_y][start_x] == 1: # 시작 위치에 사과가 있는 경우
    apple = 1
    table[start_y][start_x] = -1
visited[start_y][start_x] = True
print(backtrack(start_y, start_x, 0, apple))

# 조건을 만족하면 종료하도록 짜다가 그냥 모든 경우를 탐색해야 함