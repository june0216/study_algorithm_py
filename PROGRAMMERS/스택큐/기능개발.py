import pprint


def solution(progresses, speeds):
    answer = [0 for _ in range(len(progresses))]
    com = []
    f = 0
    for idx, val in enumerate(progresses):
        cnt = 0
        while val < 100:
            val = val + speeds[idx]
            cnt += 1

        com.append(cnt)
    answer[0] = 1
    before = com[0]
    j = 0
    for k in range(1, len(com)):
        if before >= com[k]:
            answer[j] += 1
        else:
            j += 1
            answer[j] += 1
            before = com[k]

    return answer[:j + 1]