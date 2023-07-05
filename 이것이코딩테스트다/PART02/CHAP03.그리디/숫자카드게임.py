m, n = map(int, input().split())
min_data = 0
for i in range(n):
    num = list(map(int, input().split()))
    temp = min(num)
    if(min_data <= temp):
        min_data = temp
print(min_data)
