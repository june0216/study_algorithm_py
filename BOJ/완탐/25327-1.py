import sys
from collections import defaultdict

input = sys.stdin.readline

st_num, q_num = map(int, input().split())

st_dict = defaultdict(int)
for _ in range(st_num):
    st_list = tuple(input().split())
    st_dict[st_list] += 1

pas = 0
for _ in range(q_num):
    q_list = list(map(str, input().split()))
    res = 0
    for st in st_dict: #여러 개의 iterable자료형이 개수가 동일할 때 사용, 인자로 넘어온 자료 구조 내의 모든 요소가 참일 때만 True를 반환
        if all(q == '-' or q == s for q, s in zip(q_list, st)): #all() 함수는 반복문으로 순회할 수 있는(iterable) 모든 객체를 인자로 받을 수 있다. 쉽게 말해 여러 데이터를 담을 수 있는 리스트(list), 튜플(tuple)과 같은 파이썬
            #zip() = 같은 인덱스 짝별로 튜플에 담아 변환
            res += st_dict[st]
    print(res)