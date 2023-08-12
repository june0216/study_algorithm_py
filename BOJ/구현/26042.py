from collections import deque

n = int(input())
#(명수, 번호)
qu = deque()
max_num = -1
count = -1
for i in range(n):
    c = input()
    if c.startswith("1"):
        cmd, num = map(int, c.split())
    if c == "2":
        qu.popleft()
    else:
        qu.append((cmd,num))
        qu_len = len(qu)
        if count ==qu_len:
            if max_num > num:
                max_num = num
        elif count < qu_len:
            max_num, count = num, qu_len
print(str(count) + " " + str(max_num))


