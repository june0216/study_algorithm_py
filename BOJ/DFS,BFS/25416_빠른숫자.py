from collections import deque
n, m = map(int, input().split())
table = []
for _ in range(n):
    r = list(map(int, input().split()))
    table.append(r)

def dfs():
    # BFS 탐색을 위한 큐 초기화
    qu = deque()


    # 인접한 칸을 이동할 수 있는지 확인하고 큐에 넣음
    while qu:
        x, y = qu.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if nx >= 0 and nx < n and ny >= 0 and ny < m and table[nx][ny] != -1:
                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    # 목적지인 1이 적힌 칸까지의 최소 이동 횟수 반환
    if distance[n-1][m-1] == float('inf'):
        return -1
    else:
        return distance[n-1][m-1]
