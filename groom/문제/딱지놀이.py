# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 별 동그라미 ?네모?ㅛㅔ모

def print_m(a, b, num):
    if (num == 0):
        result.append("D")
        return

    if (a.count(num) > b.count(num)):
        result.append("A")
        return

    elif (a.count(num) < b.count(num)):
        result.append("B")
        return

    else:
        print_m(a, b, num - 1)


N = int(input())
result = []
for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print_m(a[1:], b[1:], 4)
for k in range(len(result)):
    print(result[k])
print("")

