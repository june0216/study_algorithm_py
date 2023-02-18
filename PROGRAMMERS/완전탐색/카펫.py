def solution(brown, yellow):
    answer = []
    yellow_h = 0
    yellow_w = 0
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_h = i
            yellow_w = int(yellow / i)
            if yellow_h * 2 + yellow_w * 2 + 4 == brown:
                answer.append(yellow_w + 2)
                answer.append(yellow_h + 2)
                return sorted(answer, reverse=True)