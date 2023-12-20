# 최소 일수 구하기 -> BSF
# 하지만 0과 1로 구성되어 있는 게 아니라 n번 접근 가능함 -> deepcopy

#구역의 수 구하기

import sys
from collections import deque
from copy import deepcopy
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
total = int(input())
area = []
for _ in range(total):
    area.append(list(map(int, input().split())))


def count_colored():
    cnt = 0
    for i in range(total):
        for j in range(total):
            if area[i][j] != 0:
                cnt +=1
    return cnt

result = 0
while True:
    copy_area = deepcopy(area)
    if count_colored() == 0:
        break
    for i in range(total):
        for j in range(total):
            if copy_area[i][j] == 0:
                for n in range(4):
                    nx = dx[n] + i
                    ny = dy[n] + j
                    if 0 <= nx < total and 0 <= ny < total:
                        if area[nx][ny] > 0:
                            area[nx][ny] -=1
    result +=1

print(result)