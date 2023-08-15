#구간 내에 같은 것
from collections import defaultdict

total_len, same_limit = map(int, input().split())
num = list(map(int, input().split()))
max_len = 0
right = 0
left = 0
counts = defaultdict(int)

while right < total_len:
    counts[num[right]] += 1
    while counts[num[right]] > same_limit: #한계에 도달했을 때
        counts[num[left]] -= 1
        left += 1
    max_len = max(max_len, right - left + 1)
    right += 1

print(max_len)
