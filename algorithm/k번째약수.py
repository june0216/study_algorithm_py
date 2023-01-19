import sys

n, k = map(int, input().split())
res = []
cnt = 0

for i in range(1,7):
    if n%i == 0 in res:
        cnt +=1
    else : res.append(n / i)
else:
    print(-1)


print(res[k-1])