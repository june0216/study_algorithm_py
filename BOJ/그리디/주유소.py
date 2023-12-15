#다익스트라?
#최소인 주유소가 있으면 최대 충전, 하지만 나머지에서는 도로를 지나갈 정도로만 충전
import heapq
from copy import deepcopy
total_num = int(input())
if total_num == 0:
    print(0)
    exit()
road = []
station = []

road = list(map(int, input().split()))
station = list(map(int, input().split()))

que = []
for s in station:
    heapq.heappush(que, s)
result = 0

while que:
    node  = (heapq.heappop(que))
    idx = station.index(node)
    for i in range(idx, len(road)):
        if road[i] != -1:
            result += (road[i] * node)
            road[i] = -1
        else:
            break
print(result)
