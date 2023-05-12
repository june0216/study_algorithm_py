import sys
input = sys.stdin.readline
n = int(input())

h = 3600
m = 60
table = [0] * (h * 24 + m * 60 + 60)  # [00:00:00, 23:59:59]의 각 초를 저장할 리스트 초기화

for _ in range(n):
    q = list(input().split())
    start_list = list(map(int, q[1].split(":")))
    end_list = list(map(int, q[2].split(":")))
    start = start_list[0] * h + start_list[1] * m + start_list[2]
    end = end_list[0] * h + end_list[1] * m + end_list[2]

    if q[0] == '1':
        table[start] += 1
        table[end] -= 1
    else:
        for i in range(1, len(table)):
            table[i] = table[i] + table[i - 1]
        print(sum(table[start:end]))
        for i in range(len(table) - 1, 0, -1):
            table[i] -= table[i - 1]