import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

MAX_VAL = sys.maxsize
V = [MAX_VAL] * (N+1)
H = []
# 여물수, 위치
heapq.heappush(H, (0, 1))
while H:
    c, v = heapq.heappop(H)
    if v == N:
        print(c)
        break

    for next_v, next_c in G[v]:
        total_c = c + next_c
        if V[next_v] > total_c:
            V[next_v] = total_c
            heapq.heappush(H, (total_c, next_v))