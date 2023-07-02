import sys
input = sys.stdin.readline
N, M = map(int, input().split())
number_list = []
naming_list=[]
for i in range(N):
    key, value = input().split()
    value = int(value)
    number_list.append(value)
    naming_list.append(key)

def binary_search(number_list, target):
    start = 0
    end = N-2
    while start <= end:
        mid = (start + end) //2
        if target > number_list[mid]:
            start = mid+1
        else:
            end = mid-1
    return naming_list[end+1]

for _ in range(M):
    power = int(input())
    print(binary_search(number_list,power))
