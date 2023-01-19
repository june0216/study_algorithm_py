n = int(input())

list = [0] * (n+1)
res = 1
for i in range(2, n+1):
    if list[i] == 0:
        res += 1
        for j in range(i, n+1, i):
            list[j] = 1
print(res)