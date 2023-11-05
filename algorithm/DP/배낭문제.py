import sys
input = sys.stdin.readline

total, limit_weight = map(int, input().split())
table = [[0 for _ in range(limit_weight+1)] for _ in range(total+1)]
given = []
for i in range(1, total+1):
    weight , value = map(int, input().split())
    given.append([weight, value])
    for j in range(1, limit_weight+1):
        if j >= weight:
            table[i][j] = max(table[i-1][j], value + table[i-1][j-weight]) # 전의 값 vs 현재 + 전에 있었던 세트에서 (현재-직접값) -> 어차피 최적의 부분 구조임
        else:
            table[i][j] = table[i-1][j]

print(table[-1][-1])