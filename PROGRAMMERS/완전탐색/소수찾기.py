import itertools
import math


def solution(numbers):
    answer = 0
    res = []
    cnt = 0

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    l = len(numbers)
    for i in range(1, l + 1):
        li = set(itertools.permutations(numbers, i))
        for k in li:
            t = "".join(k)
            if t[0] == "0":
                continue
            elif is_prime(int(t)) == True:
                cnt += 1
    return cnt
