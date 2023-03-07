from collections import deque


def solution(prices):
    answer = []
    qu = deque(prices)
    while qu:
        temp = qu.popleft()
        num = 0
        for i in qu:
            num += 1
            if i < temp:
                break
        answer.append(num)
    return answer
