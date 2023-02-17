def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
        answer = max(w) * max(h)

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))