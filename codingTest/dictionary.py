from collections import Counter

def solution(cars, k):
    # 각 차량의 개수를 카운트
    car_dic = Counter(cars)

    # 값이 큰 것부터 정렬하고, 값이 같다면 키를 알파벳 순으로 정렬
    sorted_car = sorted(car_dic.items(), key=lambda x: (x[1], x[0]), reverse=True)

    fail_car = []
    fail_sum = 0
    success_sum = 0

    # 상위 k-1개의 차량 개수를 더함
    for key, v in sorted_car[:k-1]:
        success_sum += v

    # 나머지 차량을 실패 목록에 추가하고 개수를 더함

    for key, value in sorted_car[k-1:]:
        fail_car.append(key)
        fail_sum += value

    # 실패 차량의 개수가 성공 차량의 개수보다 클 때까지 차량을 제거
    while fail_sum > success_sum:
        removed = fail_car.pop()
        fail_sum -= car_dic[removed]

    return fail_car[-1] if fail_car else None  # fail_car가 비어있지 않다면 마지막 원소 반환, 비어있다면 None 반환

# 테스트
print(solution(['a', 'b', 'a', 'c', 'a', 'b', 'd'], 2))
