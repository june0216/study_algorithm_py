from collections import deque
#다각형
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    que = deque()

    # ㅁ 형태로 되어 있으면 테두리를 인식하지 못함
    line = [[-1]*102 for _ in range(102)]

    #테두리 작업
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x <x2 and y1 < y < y2: #자신의 사각형 내부라면
                    line[x][y] = 0
                elif line[x][y] != 0: # 다른 사각형의 내부가 아니라면
                    line[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((characterX * 2, characterY * 2, 0))
    visited = [[1] * 102 for i in range(102)]
    visited[characterX * 2][characterY * 2] = 0

    while q:
        x, y, cnt = q.popleft()

        if x == itemX * 2 and y == itemY * 2:
            answer = cnt // 2
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if line[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = 0

    return answer
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))