#연산 1 = 1을 더하기
#연산 2 = 2를 곱하기
A, K = map(int, input().split())
count = 0
while True:
    if A == K:
        print(count)
        break
    else:
        if K % 2 == 0 and K >= A*2:
            K = K//2
            count +=1
        else:
            K = K-1
            count +=1

