#처음에 풀이가 그리디같아 보였지만 그리디는 아님 => 그리디라면 테이블에 저장하는 게 아니라 당시에 최소값을 픽스했을 것임 이 풀이는 픽스하는 것이 아니라 테이블에 보관한다.
#모든 경우를 table에 담아서 고려해주었기 때문에 DP임
n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

dp = [[0]* (n+1) for _ in range(3)]
for i in range(n): #집
    table[i][0] += min(table[i-1][1], table[i-1][2])
    table[i][1] += min(table[i - 1][0], table[i - 1][2])
    table[i][2] += min(table[i - 1][0], table[i - 1][1])

print(min(table[-1]))