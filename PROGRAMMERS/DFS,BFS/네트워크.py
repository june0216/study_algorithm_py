def solution(n, computers):
    visited = [False]*(n+1)
    def dfs(idx):
        for d, val in enumerate(computers[idx]):
            if visited[d] == False and val == 1:
                visited[d] = True
                dfs(d)

    cnt = 0
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(i)
            cnt +=1
    return cnt

print(solution(3, 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


