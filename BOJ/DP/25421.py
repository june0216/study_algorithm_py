# 1 -> 3
# 2 -> 4
# 3 -> 5
# 4-> 42, 43, 44, 45, 46 => 5
# 5 -> 53, 54, 55, 56, 57 => 5
# 6 -> 64, 65, 66, 67, 68
# 7 -> 75, 76, 77, 78, 79
# 8 -> 86. 87, 88, 89,=> 4
# 9 -> 97 98 99


# 3자리 -> 0
num = [1 for _ in range(9)]

n = int(input())

for _ in range(2, n+1):
    temp = []
    for i in range(9):
        temp.append(sum(num[max(0, i - 2):min(10, i + 3)]) % 987654321)
    num = temp

print(sum(num) % 987654321)







