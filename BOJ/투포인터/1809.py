total, S = map(int, input().split())

li = list(map(int, input().split())) + [0]
left = 0
right = 0
res = li[0]

while right < len(li):
    if res == S:
        right += 1
        res += li[right]
        res -= li[left]
    if res > S:
        res -= li[left]
        left -= 1
    if res < S:
        right += 1
        res += li[right]


