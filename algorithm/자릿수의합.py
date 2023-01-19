num = int(input())
list = list(map(int, input().split()))
temp = []
res = 0

def digit_sum(x):
    res = 0
    if x < 9: 
       return x
    while x > 0:
        res = res + x % 10
        x = x//10
    return res

for i in range(num):
    temp.append(digit_sum(list[i]))
print(max(temp))

