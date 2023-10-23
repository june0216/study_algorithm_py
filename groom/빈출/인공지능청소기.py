#맨하튼 거리
case_num = int(input())

def can_reach(x_target, y_target, n_target):
    distance = abs(x_target) + abs(y_target)
    if n_target < distance:
        return "NO"
    remaining_moves = n_target - distance
    return "YES" if remaining_moves % 2 == 0 else "NO"

for _ in range(case_num):
    x_target, y_target, n_target = map(int, input().split())
    print(can_reach(x_target, y_target, n_target))
