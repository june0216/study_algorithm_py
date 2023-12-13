import sys
INF = sys.maxsize
type_num, goal = map(int, input().split())
coins = []
for _ in range(type_num):
    coins.append(int(input())) #동전의 종류를 담을 리스트


dp = [INF] * (goal +1) # 목표 금액까지 가기 위한 최소 경우를 저장한다.
dp[0] = 0 # 0원일 경우 0가지 이므로 처리
for coin in coins:
    for j in range(coin, goal+1):
        dp[j] = min(dp[j], dp[j-coin]+1)
if dp[j] == INF:
    print(-1)
else:
    print(dp[goal])