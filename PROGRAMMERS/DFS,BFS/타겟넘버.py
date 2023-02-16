def solution(numbers, target):
    val = 0
    lst = len(numbers)

    answer = 0
    def dfs(val,idx):
        global answer
        if idx == lst:
            if val == target:
                answer += 1
            return
        dfs(val+numbers[idx], idx+1)
        dfs(val-numbers[idx], idx+1)
    dfs(0, 0)
    return answer


