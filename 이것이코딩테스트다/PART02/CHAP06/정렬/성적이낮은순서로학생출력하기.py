total = int(input())
table = []
for _ in range(total):
    input_data = list(map(int, input().split()))
    table.append((input_data[0], input_data[1]))
result = sorted(table, key = lambda table:table[1])
for re in result:
    print(re[0], end = ' ')