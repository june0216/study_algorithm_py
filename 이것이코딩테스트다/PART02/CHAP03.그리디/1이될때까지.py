n, m = map(int, input().split())
count = 0

while True:
    target = (n // m ) * m
    count += (n - target)
    n = target
    if n < m:
        break
    n = n // m
    count +=1

count += (n -1) # 나머지 부분 1로 만들기


print(count)
