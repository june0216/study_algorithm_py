
#2로 나누어 떨어지면 -> 3가지
# 4단위라면 -> 2로 나누어떨어지는 거 + 2가지
n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    else :
        dp[i] = 0
print(dp[n])
