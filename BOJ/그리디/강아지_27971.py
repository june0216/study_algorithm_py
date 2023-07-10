from collections import deque

N, M, A, B = map(int, input().split())
interval = []
for _ in range(M):
    interval.append(list(map(int, input().split())))


def bfs():
    qu = deque()
    qu.append((0, 0))
    while qu:
        num, cnt = qu.popleft()
        if num == N:
            return cnt
        for i in range(M):
            inter = interval[i]
            if inter[0] >= num and inter[1] <= num:
                continue
            if num + A <= N:
                qu.append((num+A, cnt +1))
            if num + B <= N:
                qu.append((num+B, cnt +1))
    return -1


print(bfs())

