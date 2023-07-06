start = input()
dx = [-2, 2, 1, -1, -2, 2, -1, 1]
dy = [-1, -1, -2, -2, 1, 1, 2, 2]

#step = [(-2, 1), (-2, -1) .. ] 변경 가능
count = 0
for i in range(len(dx)):
    nx = dx[i] + start[0] - int(ord('a')) +1
    ny = dy[i] + start[1]
    if nx > 8 or ny > 8 or nx < 0 or ny < 0:
        continue
    count+=1