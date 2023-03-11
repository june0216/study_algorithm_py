from collections import Counter


def solution(topping):
    answer = 0
    right = Counter(topping)
    left = {}

    for i in range(len(topping)):
        if topping[i] in left:
            left[topping[i]] += 1
        else:
            right[topping[i]] = 1
        right[topping[i]] -= 1

        if right[topping[i]] == 0:
            del right[topping[i]]

        if len(left) == len(right):
            answer += 1

    return answer