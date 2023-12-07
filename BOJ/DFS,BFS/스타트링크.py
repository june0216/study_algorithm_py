from collections import deque
total, now, target , up, down = map(int, input().split())

qu = deque()
qu.append((now, 0))
flag = -1
#왜 visited가 필요할까?
visited = [False] * (total+1)
visited[now] = True
while qu:
    stair, cnt = qu.popleft()
    if stair == target:
        flag = 1
        break
    if stair-down >= 1 and down != 0 and visited[stair-down] == False:
        qu.append((stair-down, cnt+1))
        visited[stair - down] = True
    if stair+up <= total and up != 0 and stair+up != now and visited[stair+up] == False:
        qu.append((stair+up, cnt+1))
        visited[stair+up] = True
if flag == -1:
    print("use the stairs")
else:
    print(cnt)