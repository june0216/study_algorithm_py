N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(li[i][0]+i, N+1):
        if dp[j] < dp[i] + li[i][1]:
            dp[j] = dp[i] + li[i][1]
print(dp[-1])