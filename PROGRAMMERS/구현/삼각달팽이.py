def solution(n):
    # dp 느낌
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    arr = [[0] * i for i in range(1, n + 1)]
    idx = 0
    x = 0
    y = 0
    val = 1
    end_num = sum(i for i in range(1, n + 1))  # 직각삼각형 내부의 칸 수
    while val <= end_num:
        arr[x][y] = val
        val += 1
        nx = dx[idx] + x
        ny = dx[idx] + y
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
            y, x = ny, nx
        # 범위를 벗어나거나 값이 0이 아닐 경우 방향 변경
        else:
            idx = (idx + 1) % 3
            nx = dx[idx]
            ny = dx[idx]
            y += ny
            x += nx
    answer = []
    print(arr)
    for num in arr:
        for ans in num:
            answer.append(ans)

    return answer
print(solution(4))