import pprint
N, M = map(int, input().split())
li = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    # li[i].append(list(map(int, input().split())))
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

def dfs(idx):
    # print(idx)
    for val in li[idx]:
        # pprint.pprint(locals())
        if visited[val] == False:
            visited[val] = True
            dfs(val)

cnt = 0
for x in range(1, N+1):
    if not visited[x]:
        visited[x] = True
        dfs(x)
        cnt+=1
print(cnt)