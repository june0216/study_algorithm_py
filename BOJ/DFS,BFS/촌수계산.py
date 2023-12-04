from collections import deque
total_person = int(input())
t1, t2 = map(int, input().split())
child = max(t1, t2)
parent = min(t1, t2)
relation_num = int(input())
relation = [[] for _ in range(total_person+1)]
for _ in range(relation_num):
    a , b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
    relation[a].sort()
    relation[b].sort()

qu = deque()
qu.append((parent, 0))
visited = [False] * (total_person+1)
result = []
def dfs(start, cnt):
    cnt +=1
    visited[start] = True
    if start == parent:
        result.append(cnt)
    for node in relation[start]:
        if not visited[node]:
            dfs(node, cnt)
dfs(child, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)
