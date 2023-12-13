test_case = int(input())
test_arr = [int(input()) for _ in range(test_case)]
max_test_val = max(test_arr) #여러 테스트 케이스가 존재하는데 수열이므로 최대 숫자까지의 수열을 다 구한 후 각각 테스트 케이스에 맞게 출력합니다.
dp = [0 for _ in range(max_test_val+1)] #수열을 담을 배열

dp[0] = 0
dp[1] = 1 #규칙 적용되기 전의 초기값 세팅
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6, max_test_val + 1):
    dp[i] = dp[i - 5] + dp[i - 1] #구하는 값에서 -5위치와 -1 위치의 값을 더한 값이 구하는 값이 되는 규칙 적용

for tc in test_arr: #테스트 케이스 별로 출력
    print(dp[tc])