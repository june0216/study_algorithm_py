import itertools
def solution(word):
    answer = 0
    ch = ["A", "E", "I", "O", "U"]
    li = []
    def mk(cnt, w):
        if cnt == 5:
            return
        for i in range(len(ch)):
            li.append(w+ch[i])
            mk(cnt+1, w+ch[i])

    mk(0, "")

    return li.index(word)+1
print(solution("AAAAE"))