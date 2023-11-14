import sys
sys.setrecursionlimit(10000)
total = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))
visited = [0 for _  in range(len(cal))]
max_val = -1e9
min_val = 1e9
def dfs(i, val):
    global max_val, min_val
    if i == total:
        min_val = min(val, min_val)
        max_val = max(val, max_val)
    else:
        if cal[i] != 0 and i == 0 and visited[i] == False:
            dfs(i + 1, val + num[i])
            visited[i] = True
        if cal[i] != 0 and i == 1 and visited[i] == False:
            dfs(i + 1, val - num[i])
            visited[i] = True
        if cal[i] != 0 and i == 2 and visited[i] == False:
            dfs(i + 1, int(val * num[i]))
            visited[i] = True
        if cal[i] != 0 and i == 3 and visited[i] == False:
            dfs(i + 1, int(val / num[i]))
            visited[i] = True



dfs(0, num[0])
print(max_val)
print(min_val)

