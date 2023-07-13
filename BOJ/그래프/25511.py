

N, k = map(int, input().split())
edge = {0:-1}
for i in range(N-1):
    a, b =map(int, input().split())
    edge[b] =a
values = list(map(int, input().split()))
find_values = {}
for j in range(len(values)):
    find_values[values[j]] = j

def find():
    if k not in values:
        return -1
    target = find_values[k]
    depth = 0

    while edge[target] != -1:
        target = edge[target]
        depth += 1
    return depth
print(find())


