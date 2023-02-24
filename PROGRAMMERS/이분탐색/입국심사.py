def solution(n, times):
    answer = 0
    short, long = 1, max(times) * n
    while short <= long:
        mid = (short + long) //2
        p = 0
        for time in times:
            p += mid // time
            if p >= n:
                break
        if p < n:
            short = mid + 1
        elif p >= n:
            answer = mid
            long = mid - 1
    return answer