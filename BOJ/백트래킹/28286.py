from collections import deque
N, K = map(int, input().split())

answer = list(map(int, input().split()))
paper = list(map(int, input().split()))



def pull(temp, i):
    a1, a2 = temp[:i], deque(temp[i:])
    a2.rotate(-1)
    a2[-1] = -1
    return a1 + list(a2)

def push(temp, i):
    a1, a2 = temp[:i], deque(temp[i:])
    a2.rotate(1)
    a2[0] = -1
    return a1 + list(a2)

def count(answer, paper):
    result = 0
    for k in range(len(paper)):
        if answer[k] == paper[k]:
            result +=1
    return result

max_score = 0

def backtracking(paper, k):
    global max_score

    score = count(answer, paper)
    if score > max_score:
        max_score = score

    if k >= K:
        return

    for i in range(N):
        # i번째 문제부터 답안을 당기거나 밀어보기
        pulled = pull(paper.copy(), i)
        pushed = push(paper.copy(), i)
        # 각각의 상황에 대해 재귀적으로 탐색
        backtracking(pulled, k+1)
        backtracking(pushed, k+1)

backtracking(paper, 0)
print(max_score)



# 단순 리스트로 pull 을 구현했는데 실패 -> deque를 이용


