
for tc in range(1, 11):
    N = int(input())
    TC = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        max_value = 0
        if TC[i] > TC[i - 1] and TC[i] > TC[i - 2] and TC[i] > TC[i + 1] and TC[i] > TC[i + 2]:
            for k in (TC[i - 1], TC[i - 2], TC[i + 1], TC[i +2]):
                if k > max_value:
                    max_value = k

            ans += TC[i] - max_value

    print('#{} {}'.format(tc, ans))
