import heapq
total = int(input())
cards = []
for _ in range(total):
    heapq.heappush(cards, int(input()))
result = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_val = a+b
    heapq.heappush(cards, sum_val)
    result += sum_val
print(result)
