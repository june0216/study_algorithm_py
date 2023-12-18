
n, target_score , rank_num = map(int, input().split())
if n: # n이 0보다 큰 경우에만 점수가 주어진다.
    score = list(map(int, input().split()))
    score.append(target_score)
    score.sort(reverse=True)
    idx = score.index(target_score) + 1
    if idx > rank_num:
        print(-1)
    else:
        if target_score == score[-1] and n == rank_num:  # 랭킹이 꽉 차있다면 이전 점수보다 더 좋지 않은 경우
            print(-1)
        else:
            print(idx)
else:
    print(1)
