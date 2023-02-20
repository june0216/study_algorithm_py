from collections import deque

def solution(k, dungeons):
    answer = -1
    qu = deque()
    qu.append((k, []))
    while qu:
        k, route = qu.popleft()
        for idx, val in enumerate(dungeons):
            if idx not in route and val[0] <= k:
                qu.append((k-val[1], route + [idx]))
            else:
                answer= max(answer, len(route))
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))

