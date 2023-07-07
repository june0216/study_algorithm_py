total = int(input())
table = []
for _ in range(total):
    table.append(int(input()))

result = sorted(table, reverse=True)

for i in range(result):
    print(result[i],  end = ' ')