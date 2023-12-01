#가중치가 1이상이므로 다익스트라
import heapq
import sys
INF = sys.maxsize
city_num = int(input())
bus_num = int(input())

min_val = [INF] * (city_num+1)

input_num = [[] for _ in range(city_num+1)]


for _ in range(bus_num):
    u, v, w = map(int, input().split())
    input_num[u].append((w, v))
start, end = map(int, input().split())

min_val[start] = 0
que = []
result = [[] for _ in range(city_num+1)] #경로 저장용
result[start].append(start)
heapq.heappush(que, (0, start))
for i in input_num:
    i.sort()

while que:
    com_weigth, com_node = heapq.heappop(que)
    if com_node == end:
        break
    for weight, node in input_num[com_node]:
        if weight+com_weigth < min_val[node]:
            min_val[node] = weight + com_weigth
            result[node] = result[com_node] + [node]
            heapq.heappush(que, (com_weigth+weight, node))
print(com_weigth)
print(len(result[com_node]))
print(*result[com_node])

