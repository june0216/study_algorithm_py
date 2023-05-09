import sys

n = int(input())
s = input().strip()

if n == 1:
    print("NO")
    sys.exit(0)

for i in range(1, n):
    window1 = s[:i]
    l = len(window1)
    window2 = s[n-l:n]
    if window2[0] == window1[0] or window1[-1] == window2[-1]:
        diff = 0
        for j in range(l):
            if window1[j] != window2[j]:
                diff += 1
            # 정확히 한 문자만 다르다면 비타민 문자열
        if diff == 1:
            print("YES")
            sys.exit(0)
    elif n == 2:
        if window1[0] != window2[0]:
            print("YES")
            exit(0)


print("NO")
