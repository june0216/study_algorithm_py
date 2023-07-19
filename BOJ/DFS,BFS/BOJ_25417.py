import sys
from collections import deque

# 방향 배열 정의
MOVE = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = sys.maxsize

# 범위를 벗어나는지 확인하는 함수
def out_of_range(row, col):
    return row < 0 or row >= 5 or col < 0 or col >= 5

# run 함수 정의
def run(current, direction):
    cur_row, cur_col = current[0], current[1]
    direction_type = direction[2]

    while True:
        # 1회 이상 이동 후에, 7을 만나면 멈춘다.
        if (cur_row != current[0] or cur_col != current[1]) and M[cur_row][cur_col] == 7:
            break

        # 다음 row, col 값으로 갱신
        next_row = cur_row + direction[0]
        next_col = cur_col + direction[1]

        # 칸을 벗어나거나 그 칸의 값이 -1일 때 멈춘다.
        if out_of_range(next_row, next_col):
            break
        if M[next_row][next_col] == -1:
            break

        # 도착 칸 업데이트
        cur_row = next_row
        cur_col = next_col

    # 도착 칸에 이미 방문을 했다면 None을 반환한다.
    if visit[direction_type][cur_row][cur_col] <= visit[current[2]][current[0]][current[1]] + 1:
        return None

    # 방문 값을 업데이트 한다.
    visit[direction_type][cur_row][cur_col] = visit[current[2]][current[0]][current[1]] + 1
    return (cur_row, cur_col, direction_type)

# walk 함수 정의
def walk(current, direction):
    # walk 값을 하나 더한다.
    next_row = current[0] + direction[0]
    next_col = current[1] + direction[1]
    # 걸은 수
    direction_type = direction[2]

    # 벗어난 경우
    if out_of_range(next_row, next_col):
        return None
    # -1칸인 경우
    if M[next_row][next_col] == -1:
        return None
    # 예전에 방문한 경우
    if visit[direction_type][next_row][next_col] <= visit[current[2]][current[0]][current[1]] + 1:
        return None

    # 새로 방문한 값 visit 업데이트
    visit[direction_type][next_row][next_col] = visit[current[2]][current[0]][current[1]] + 1
    return (next_row, next_col, direction_type)

# bfs 함수 정의
def bfs(start):
    q = deque()

    # 걸어서 방문과 뛰어서 방문 둘 다 넣기
    q.append((start[0], start[1], 0))
    q.append((start[0], start[1], 1))
    visit[0][start[0]][start[1]] = 1
    visit[1][start[0]][start[1]] = 1

    while q:
        current = q.popleft()

        # 걷는 것과 뛰는 것 나눠서 실행. type에는 0 혹은 1이 들어감. 이는 visit의 첫번째 구분과 동일
        for type in range(2):
            # 각 방향 별로 실행
            for d_row, d_col in MOVE:

                if type == 0:
                    next = run(current, (d_row, d_col, type))
                    # None이면 다음 방향으로 넘긴다.
                    if next is None:
                        continue
                else:
                    next = walk(current, (d_row, d_col, type))
                    if next is None:
                        continue

                q.append(next)

    # end 칸 기준으로 걷거나 뛰어서 도착했을 때 정답 값 비교
    answer = min(visit[0][end[0]][end[1]], visit[1][end[0]][end[1]])
    # 방문 못했으면 -1 출력
    return -1 if answer == INF else answer - 1

# 메인 함수
M = [[0] * 5 for _ in range(5)]
# 뛰어서 방문한 게 1, 걸어서 방문한 게 0
visit = [[[INF] * 5 for _ in range(5)] for _ in range(2)]

for i in range(5):
    line = input().split()
    for j in range(5):
        M[i][j] = int(line[j])
        if M[i][j] != 1:
            continue
        end = (i, j)

line = input().split()
start = (int(line[0]), int(line[1]))

print(bfs(start))
