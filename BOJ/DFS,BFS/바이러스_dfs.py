node = int(input())
relation = int(input())
li = [[] for _ in range(node+1)]
visited = [0 for _ in range(node+1)]
for _ in range(relation):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
cnt = 0
def dfs(idx):
    global cnt
    visited[idx] = 1
    for num in li[idx]:
        if visited[num] == 0:
            cnt += 1
            dfs(num)

dfs(1)
print(cnt)