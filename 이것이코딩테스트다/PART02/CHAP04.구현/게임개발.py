n, m = map(int, input().split())
A, B, dir = map(int, input().split())
visited = [[0]*m for _ in range(n)]
table = []
for _ in range(m):
    table.append(list(map(int, input().split())))

visited[A][B] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

def turn_left():
    global dir
    dir -= 1
    if dir < 0:
        dir = 3

while True:
    turn_left()
    nx = A + dx[dir]
    ny = B + dy[dir]
    if visited[nx][ny] == 0 and table[nx][ny] == 0:
        visited[nx][ny] =1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time +=1
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if dir[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)



