import sys
input = sys.stdin.readline
n = int(input())
s = input().strip()

for length in range(1, n):
    # 시작부분과 끝부분 문자열 선택
    front = s[:length]
    back = s[-length:]

    # 두 문자열에서 다른 문자의 개수 계산
    diff = sum(a != b for a, b in zip(front, back))

    # 다른 문자가 정확히 하나라면 '비타민 문자열'
    if diff == 1:
        print("YES")
        sys.exit(0)


print("NO")