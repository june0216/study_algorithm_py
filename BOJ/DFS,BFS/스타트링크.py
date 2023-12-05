from collections import deque
import sys

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
graph = [[] for _ in range(F + 1)]

queue = deque([S])
dist = [0] * (F + 1)


while queue:

    x = queue.popleft()
    if x == G:
        print(dist[x])
        break


    for nextX in (x + U, x - D):

        if nextX == x:
            continue;

        if 1 <= nextX <= F and not dist[nextX]:
            dist[nextX] = dist[x] + 1
            queue.append(nextX)
else:
    print("use the stairs")