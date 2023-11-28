#가중치가 1이상이므로 다익스트라
import heapq
import sys
from collections import defaultdict
INF = sys.maxsize
edge_num, line = map(int, input().split())
start = int(input())
min_val = [INF] * (edge_num+1)

input_num = [[] for _ in range(edge_num+1)]


for _ in range(line):
    u, v, w = map(int, input().split())
    input_num[u].append((w, v))


info = [(0, start)]
min_val[start] = 0
while info:
    weight, edge = heapq.heappop(info)
    for w, e in input_num[edge]:
        if min_val[e] > w+weight:
            min_val[e] = weight + w
            heapq.heappush(info, (weight+w, e))

for i in range(1, edge_num+1):
    if min_val[i] == INF:
        print("INF")
    else:
        print(min_val[i])
