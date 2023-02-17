
def solution(nums):
    temp = set(nums)
    total = len(nums)//2
    if total <= len(temp):
        return total
    else:
        return len(temp)