from itertools import combinations

total = []
for i in range(3):
    total.append(list(input()))

k = int(input())
combi = set()
result = set()

for s in total:
    for subset in combinations(s, k):
        subset_str = ''.join(subset) # 튜플로 된 것을 문자열로 변경
        if subset_str in combi:
            result.add(subset_str)
        combi.add(subset_str)

if len(result) == 0:
    print(-1)
else:
    for r in sorted(result):
        print(r)
