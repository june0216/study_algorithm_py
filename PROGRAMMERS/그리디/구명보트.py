from collections import deque
def solution(people, limit):
    answer = 0
    qu = deque(sorted(people, reverse=True))
    while len(qu) > 1:
        if qu[0] + qu[-1] <= limit:
            qu.pop()
            qu.popleft()
            answer +=1
        else:
            qu.popleft()
            answer +=1
    if qu:
        answer +=1
    return answer