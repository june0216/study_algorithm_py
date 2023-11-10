#톱니를 돌린다는 점에서 deque 자료구조
import collections
cycle = []
for i in range(4):
    cycle.append(collections.deque(list(input())))
total = int(input())
command = [list(map(int, input().split())) for _ in range(total)]

def right(idx, direct):
    if idx >3:
        return
    if cycle[idx][6] != cycle[idx-1][2]:
        right(idx+1, -direct)
        cycle[idx].rotate(direct)

def left(idx, direct):
    if idx < 0:
        return
    if cycle[idx][2] != cycle[idx+1][6]:
        left(num-1, -direct)
        cycle[idx].rotate(direct)

for i in range(total):
    num = command[i][0] - 1
    direct = command[i][1]
    left(num - 1, -direct)
    right(num+1, -direct)
    cycle[num].rotate(direct)


res = 0
if cycle[0][0] == '1':
    res+=1
if cycle[1][0] == '1':
	res+=2
if cycle[2][0] == '1':
	res+=4
if cycle[3][0] =='1':
	res+=8
print(res)