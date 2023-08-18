import heapq

heap = []
N = int(input())
#한줄 기준으로 정렬되어 있음
#앞에 있는 것 비교를 통해 범위를 알 수 있음
num = []
for i in range(N):
    temp = map(int, input().split())
    for t in temp:
        if len(heap) < N:
            heapq.heappush(heap, t)
        else:
            if heap[0] < t:
                heapq.heappop(heap)
                heapq.heappush(heap, t)
print(heap[0])



