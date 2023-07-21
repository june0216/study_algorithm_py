tel = list(map(str, input().split()))
prefix =input()
count = 0
for t in tel:
    if len(prefix) == len(t):
        continue
    temp = t[:len(prefix)]
    if temp == prefix:
        count+=1
print(count)
