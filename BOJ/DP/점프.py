#타뷸레이션 -> 하향식
N = int(input())
games = []
for _ in range(N):
    games.append(list(map(int, input().split())))

route = [[0]* N for _ in range(N)] #경우의 수 담을 배열
route[0][0] = 1
for x in range(N):
    for y in range(N): #모든 지점들을 방문
        if x == N-1 and y == N-1:
            break
        nx = games[x][y] + x #해당 칸에서 갈 수 있는 오른쪽 지점
        ny = games[x][y] + y #해당 칸에서 갈 수 있는 왼쪽 지점
        if 0 <= nx < N: #틀 안에 있다면 경우의 수에 포함함(하나의 루트가 되는 것)
            route[nx][y] += (route[x][y])
        if 0 <= ny < N:
            route[x][ny] += (route[x][y])
print(route[-1][-1])
