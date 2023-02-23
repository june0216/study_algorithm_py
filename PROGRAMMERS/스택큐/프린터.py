def solution(priorities, location):
  answer = 0
  from collections import deque

  qu = deque([(v, i) for i, v in enumerate(priorities)])
  while len(qu):
      item = qu.popleft()
      if qu and max(qu)[0] > item[0]:
          qu.append(item)
      else:
          answer +=1
          if item[1] == location:
              break

  return answer