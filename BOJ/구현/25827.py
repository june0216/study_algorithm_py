total = int(input())
table = [0] * 86400  # 1초 길이의 시간 구간을 저장할 리스트 초기화
h = 3600
m = 60

for _ in range(total):
    q = list(input().split())
    start_list = list(map(int, q[1].split(":")))
    end_list = list(map(int, q[2].split(":")))
    start = start_list[0] * h + start_list[1] * m + start_list[2]
    end = end_list[0] * h + end_list[1] * m + end_list[2]

    if q[0] == '1':
        for i in range(start, end):
            table[i] += 1
    else:
        print(sum(table[start:end]))
