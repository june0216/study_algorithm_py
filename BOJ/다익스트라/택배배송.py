#최소 비용인데 길이가 정해져있음
import heapq
import sys
INF = sys.maxsize
node_num, path_num = map(int, input().split())
info = [[] for _ in range(node_num+1)]
for _ in range(path_num):
    u, v, w = map(int, input().split())
    info[u].append((w, v))
    info[v].append((w, u))
que = []
min_val = [INF] * (node_num + 1)
heapq.heappush(que, (0, 1))
while que:
    weight , node = heapq.heappop(que)
    if min_val[node] < weight: #이미 더 짧은 경로를 통해 처리된 노드를 다시 처리하지 않도록 하여 알고리즘의 효율성을 높이는 역할 + 방문 노드 검사
        continue
    if node == node_num:
        print(weight)
        break
    for next_weight, next_node in info[node]:
        if min_val[next_node] > next_weight + weight:
            min_val[next_node] = next_weight + weight
            heapq.heappush(que, (next_weight+weight, next_node))

