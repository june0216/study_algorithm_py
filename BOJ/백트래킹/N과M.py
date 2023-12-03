N, M = map(int, input().split())
li = []
def dfs(start):
    if len(li) == M:
        print(" ".join(map(str, li)))
    for idx in range(start, N+1):
        if idx not in li:
            li.append(idx)
            dfs(idx+1)
            li.pop()
dfs(1)
