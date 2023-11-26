from collections import deque
node = int(input())
relation = int(input())
li = [[] for _ in range(node+1)]
visited = [0 for _ in range(node+1)]
for _ in range(relation):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
qu = deque()
qu.append(1)
visited[1] = 1
count = 0
def bfs():
    global count
    while qu:
        a= qu.popleft()
        for num in li[a]:
            if visited[num] == 0:
                qu.append(num)
                visited[num] = 1
                count +=1

bfs()
print(count)