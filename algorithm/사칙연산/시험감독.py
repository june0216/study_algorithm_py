n = int(input())

a = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0


for student in a:
    student = student - b
    result += 1

    if student > 0:
        result += student // c

        if student % c > 0:
            result += 1


print(result)