import sys
n = int(input())
s = input().strip()


for i in range(n-3):
    window1 = s[i:i+3]

    for k in range(i+1, n-3):
        window2 = s[k:k+3]
        if window1[0] == window2[0] and window1[-1] == window2[-1]:
            
            print("YES")
            sys.exit(0)

print("NO")
