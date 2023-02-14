import math
import heapq
T = int(input())

def check(li):
    right = []
    left = []
    middle = li[0]
    result = [middle]
    for idx, val in enumerate(li[1:], 1):
        if val > middle:
            heapq.heappush(right, val)
        else:
            heapq.heappush(left, (-val, val))
        if idx % 2 == 0:
            if len(right) > len(left):
                heapq.heappush(left, (-middle, middle))
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = heapq.heappop(left)[1]
            result.append(middle)
    print(len(result))

    for k in range(len(result)):
        if k != 0 and (k+1) % 10 == 1:
            print()
        print(result[k], end=" ")


for i in range(T):
    M = int(input())
    li = []
    if M % 10 == 0:
        for _ in range(M//10):
            li.extend(list(map(int, input().split())))
    else:
        for _ in range(M//10 + 1):
            li.extend(list(map(int, input().split())))


    check(li)




