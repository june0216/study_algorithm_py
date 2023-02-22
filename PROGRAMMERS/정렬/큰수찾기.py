import itertools


def solution(numbers):
    answer = ''
    num = list(map(str, numbers))
    num.sort(key=lambda x: x * 4, reverse=True)

    return str(int("".join(num)))