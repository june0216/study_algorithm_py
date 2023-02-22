import pprint
def solution(c):
    c.sort(reverse=True)
    for idx, val in enumerate(c):
        if idx >= val:
            return idx
    return len(c)

print(solution([5]))