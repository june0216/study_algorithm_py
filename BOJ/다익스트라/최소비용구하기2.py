# [G3] 최소비용 구하기 2
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
for i in G:
    i.sort()
s, e = map(int, input().split())
H = [(0 ,s)]
INF = sys.maxsize
V = [INF] * (n+1)
V[s] = 0
D = [[] for _ in range(n+1)]
D[s].append(s)
while H:
    c, v = heapq.heappop(H)
    if v == e:
        break
    for mon, nxt in G[v]:
        if V[nxt] > c+mon:
            V[nxt] = c+mon
            D[nxt] = D[v]+[nxt]
            heapq.heappush(H, (c+mon, nxt))
print(c)
print(len(D[v]))
print(*D[v])