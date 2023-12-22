#타뷸레이션, 상향식 , 숫자를 1개 사용할 때 ~ 8개 사용할 때까지
# 3개를 사용하는 경우의 수 == ( 1개를 사용하는 경우의 수 ) [연산] ( 2개를 사용하는 경우의 수 )
def solution(N, number):
    answer = -1
    dp = [set([int(str(N)*i)]) for i in range(1, 9)]

    for idx in range(8): #전체 다 돌기
        for st in range(idx): #구하는 값 하나씩 선정
            for op1 in dp[st]: #2가지 피연산자 구하기 n-.... 경우들
                for op2 in dp[idx-st-1]:
                    dp[idx].add(op1 + op2)
                    dp[idx].add(op1 - op2)
                    dp[idx].add(op1 * op2)
                    if op2 != 0:
                        dp[idx].add(op1 // op2)
        if number in dp[idx]:
            return idx+1

    return answer
print(solution(5, 12))