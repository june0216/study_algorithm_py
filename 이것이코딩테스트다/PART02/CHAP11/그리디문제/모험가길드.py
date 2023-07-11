total = int(input())
panic_list = list(map(int, input().split()))
panic_list.sort()
i = len(panic_list)-1
count = 0
while True:
    if i == -1:
        break
    start = panic_list[i]
    for j in range(start):
        i-=1
    count +=1
print(count)

