#0, 1 배낭문제 느낌
#row -> 1~goal
#col -> coin의 종류
#경우의 수이니까 값을 없데이트하는 것이 아니라 축적해야한다.

type_num, goal = map(int, input().split())
coins = []
for _ in range(type_num):
    coins.append(int(input())) #동전의 종류를 담을 리스트


dp = [0] * (goal +1) # 목표 금액까지 가기 위한 여정을 하나씩 작은 동전부터 계산하여 업데이트한다.
dp[0] = 1 # 왜 dp[1] = 1이 아니라 dp[0] = 1으로 해야하는가? dp[j-coin] 이 부분에서 j-coin이 2-2라면 2원짜리 동전이 추가된 것이므로 1을 더해야함
for coin in coins:
    for j in range(coin, goal+1):
        dp[j] += dp[j-coin] #최소 경우라면 더하는 것이 아니라 대입해야하지만 이 경우는 경우의 수니까 축적(더해야)한다.

print(dp[goal])