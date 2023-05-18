import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(test_case,max(map(int,now))))