import pprint
from collections import deque
def solution(s):
    answer = True
    s = deque(s)
    stack = []
    while s:
        f = s.popleft()
        if f == ")":
            #pprint.pprint(locals())
            if len(stack) == 0:
                return False
            else : stack.pop()
        else:
            stack.append(f)
    if len(stack) != 0:
        return False

    return True