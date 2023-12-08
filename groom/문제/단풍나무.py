import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
park = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for y in range(1, N + 1):
    trees = list(map(int, input().split()))
    for x in range(1, N + 1):
        park[y][x] = trees[x - 1]


def is_colored():
    global N
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if park[y][x]:
                return 0
    return 1


if is_colored():
    print(0)
    exit(0)

update = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
day = 1

while True:
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny < 1 or nx < 1 or ny > N or nx > N:
                    continue
                if not park[ny][nx]:
                    update[y][x] += 1

    for y in range(1, N + 1):
        for x in range(1, N + 1):
            park[y][x] = max(0, park[y][x] - update[y][x])

    if is_colored():
        break

    day += 1
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            update[y][x] = 0

print(day)