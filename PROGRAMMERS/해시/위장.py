from collections import defaultdict
def solution(clothes):
    answer = 0
    dic = defaultdict(list)
    for c in clothes:
        dic[c[1]].append(c[0])
    answer = 1
    for i in dic.values():
        answer *= (len(i)+1)
    return answer -1
