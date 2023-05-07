n, m = map(int, input().split())
power_list = list(map(int, input().split()))

power_list = sorted(power_list)
num = 0

for i in range(n // 2):
    if power_list[i] + power_list[n - 1 - i] >= m:
        num +=1
print(num)
