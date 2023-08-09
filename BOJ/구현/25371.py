# n 진수로 표현하기
# 0 기준으로 나누기  -> 더히기

num, n = map(int, input().split())
def change(n, num):
    result = ""
    while True:
        if num < n:
            result += str(num)
            break
        result += str(num % n)
        num //= n
    return result[::-1]
result = change(n, num)
result_sum = 0
for r in result.split("0"):
    if r == '':
        continue
    result_sum += int(r)

print(int(change(n, result_sum)))