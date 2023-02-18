
def solution(answer):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0]*4
    for idx, val in enumerate(answer):
        if one[idx%len(one)] == val:
            result[1] +=1

        if two[idx%len(two)] == val:
            result[2] +=1
        if three[idx%len(three)] == val:
            result[3] +=1
    m = max(result)
    res = []
    for k in range(len(result)):
        if m == result[k]:
            res.append(k)
    return res
print(solution([1, 2, 3, 4, 5]))