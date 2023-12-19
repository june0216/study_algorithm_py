switch_num = int(input())
switch = list(map(int, input().split()))
people_num = int(input())

def change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1

for _ in range(people_num):
    gender, num = map(int, input().split())
    if gender == 1: #남자이면
        for i in range(switch_num):
            if (i+1)% num == 0:
                change(i)
    if gender == 2:
        change(num-1)
        for i in range(1, (switch_num//2+1)):
            if i == num:
                continue
            right = (num-1 + i)
            left = (num-1 -i)
            if left >= 0 and right < switch_num and switch[left] == switch[right]:
                change(left)
                change(right)
            else:
                break
for i in range(1, switch_num+1):
    print(switch[i-1], end=" ")
    if i % 20 == 0:
        print()

