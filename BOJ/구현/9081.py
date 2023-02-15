def permu(s):
    k = -1
    for i in range(len(s)-1):
        if s[i] < s[i+1]: #오름차순이 아닌 것의 앞을 저장
            k = i
    if k == -1:
        return False
    for j in range(len(s)-1,-1 , -1):
        if s[j] > s[k]: #뒤에서부터 확인 -> 지금보다 커야하니까 그거랑 그 다음 큰 거랑 자리를 바꿈
            m = j
            break
    s[m], s[k] = s[k], s[m]
    L = s[:k+1]
    L.extend(list(reversed(s[k+1:])))
    return L


total = int(input())
for _ in range(total):
    st = input()
    res =permu(list(st))
    if res:
        print("".join(res))
    else:
        print("".join(st))
