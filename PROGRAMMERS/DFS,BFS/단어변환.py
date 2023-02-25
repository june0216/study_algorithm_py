from collections import deque
from collections import deque
def solution(begin, target, words):
    answer = 0
    route = []
    cnt = 0
    visited = [False] * (len(words) + 1)
    qu =deque()
    qu.append((begin, 0))
    while qu:
        w, cnt= qu.popleft()
        if w == target:
            answer = cnt
            break
        for k in range(len(words)):
            if visited[k] == False:
                tmp = 0
                for i in range(len(words[k])):
                    if w[i] != words[k][i]:
                        tmp +=1
                if tmp == 1:
                    visited[k] = True
                    qu.append((words[k], cnt+1))
    return answer

print((solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])))