import sys
input = sys.stdin.readline

w, n = map(int,input().split())

valueInfo = [list(map(int,input().split())) for _ in range(n)]
valueInfo.sort(key = lambda x : x[1], reverse = True)

result = 0
for m, p in valueInfo:
    if w - m >= 0:
        w -= m
        result += (m*p)
    else:
        result += (w*p)
        break

print(result)