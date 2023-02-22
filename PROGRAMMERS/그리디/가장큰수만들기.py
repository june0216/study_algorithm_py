def solution(number, k):
    answer = []

    for num in number:
        while answer and k > 0 and num > answer[-1]:
            answer.pop()
            k -=1
        answer.append(num)

    if k > 0:
        answer = answer[:-k]

    return "".join(answer)

