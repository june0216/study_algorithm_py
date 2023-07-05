n = int(input())
x = 1
y = 1
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
c_type = ['R', 'L', 'U', 'D']
command = list(map(int, input().split()))
for c in command:
    for i in range(len(c_type)):
        if c_type[i] == c:
            nx = dx[i] + x
            ny = dy[i] + y
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
