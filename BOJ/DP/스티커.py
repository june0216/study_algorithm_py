# 계단 오르기 문제와 다른 점=> 계단 오르기는 한칸 넘기 vs 안넘기 둘 중 하나만 고르면 되는데 이거는 여러 경우가 있음
total = int(input())
for _ in range(total):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n > 1:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2])+ sticker[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))
