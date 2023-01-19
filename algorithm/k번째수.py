case = int(input())
for t in range(case):
    n, s, e, k = map(int, input.split())
    list = list(map(int, input().split()))
    a = a[s-1 ,e]
    a.sort()
    print("#", end=" ")
    print(t+1, a[k-1])




