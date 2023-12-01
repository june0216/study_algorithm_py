import heapq
import sys
INF = sys.maxsize
city_num, road_num, dist, start = map(int, input().split())
road_info = [[] for _ in range(city_num+1)]
min_val = [INF] * (city_num+1)
for _ in range(road_num):
    a, b = map(int, input().split())
    road_info[a].append(b)
que = []
result = []
heapq.heappush(que, (0, start))
min_val[start] = 0
while que:
    weight, node = heapq.heappop(que)
    if min_val[node] < weight: #이미 더 짧은 경로를 통해 처리된 노드를 다시 처리하지 않도록 하여 알고리즘의 효율성을 높이는 역할
        continue
    for n in road_info[node]:
        if min_val[n] > weight+1:
            min_val[n] = weight + 1
            heapq.heappush(que, (weight+1, n))
flag = -1
for r in range(len(min_val)):
    if min_val[r] == dist:
        print(r)
        flag = 1
if flag == -1:
    print(flag)
