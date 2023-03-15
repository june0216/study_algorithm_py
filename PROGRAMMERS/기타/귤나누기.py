from collections import Counter


def solution(k, tangerine):
    answer = 0
    dic = Counter(tangerine)
    dic = dict(sorted(dic.items(), key = lambda x: -x[1]))
    tmp = 0

    for key, value in dic.items():
        if tmp < k:
            tmp += value
            answer += 1
        else:
            return answer

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))