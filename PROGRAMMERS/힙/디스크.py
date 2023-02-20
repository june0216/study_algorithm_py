import heapq

def solution(jobs):
    answer = 0
    i = 0
    now = 0
    start = -1
    heap = []
    total = len(jobs)
    while i < len(jobs):
        for k in jobs:
            if start < k[0] <= now:
                heapq.heappush(heap, [k[1], k[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i+=1
        else:
            now +=1
    return answer//total

print(solution([[0, 3], [1, 9], [2, 6]]))