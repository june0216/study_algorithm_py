
from itertools import combinations
import sys
INF = sys.maxsize
n, max_num = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2: #치킨집인 경우의 좌표들을 다 저장
            chicken.append([i, j])
        if city[i][j] == 1: #집인 경우 좌표들을 다 저장
            house.append((i, j))

result = INF #최소값을 업데이트하기 위해 저장할 변수 -> 최소의 값을 저장하기 위해 초기값은 maxsize로 초기화
for choose_chicken in combinations(chicken,max_num): #max_num의 개수만큼 모든 경우의 수를 반환
    res = 0
    for x2, y2 in house: #집의 좌표를 기준으로 거리를 구한다.
        chicken_len = INF #집에 대한 치킨 거리
        for c in choose_chicken: #하나의 집을 기준으로 모든 치킨집을 돌면서 가장 가까운 치킨 거리를 구한다.
            x1 = c[0]
            y1 = c[1]
            dis = abs(x1 - x2) + abs(y1 - y2)
            chicken_len = min(dis, chicken_len)
        res += chicken_len
    result = min(result, res) #하나의 경우를 돈다음 최소값 업데이트

print(result)