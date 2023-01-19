4, 6, 8, 12, 20

n, m = map(int, input().split())

a = list(map(int, input.split()))
res = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            res.add(a[i] + a[j]+a[k])

a = list(res)
a.sort()
print(a[m-1])