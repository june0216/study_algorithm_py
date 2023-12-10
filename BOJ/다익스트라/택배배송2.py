#최소 + 비용이 1이상 -> 다익스트라 or dp
#heapq를 쓰는 이유 ? 시작노드에서 가장 가까운 노드를 매번(반복할때마다) 찾기 위해(저장하기 위해) 우선순위 큐를 사용한다.

import heapq
import sys

INF = sys.maxsize
node, relation = map(int, input().split())
route = [[] for _ in range(node+1)]
for i in range(relation):
    n1, n2, w = map(int, input().split())
    route[n1].append((w, n2))
    route[n2].append((w, n1))
min_val = [INF] * (node +1)
que = []
heapq.heappush(que, (0, 1))
while que:
    weight , from_node = heapq.heappop(que)

    if from_node == node:
        print(weight)
        break

    for w, n in route[from_node]:
        if min_val[n] > w+weight:
            min_val[n] = w+weight
            heapq.heappush(que, (w+weight, n)) #이 부분 틀림 최소 갱신일때만 heapq에 넣어야함


