n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def binary_search(b):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if b > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(m):
    t = list(map(int, input().split()))
    a = t[0]
    b = t[1]
    if a == 1:
        print(len(A) - binary_search(b))

    elif a == 2:
        print(len(A) - binary_search(b+1))

    elif a == 3:
        start_idx = binary_search(b)
        end_idx = binary_search(t[2] + 1)
        print(end_idx - start_idx)
