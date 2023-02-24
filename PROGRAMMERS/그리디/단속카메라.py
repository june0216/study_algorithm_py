def solution(routes):
    answer = 0
    # 중간의 값이 제일 겹침
    routes.sort(key=lambda x: x[1])
    camera = []
    camera.append(routes[0][1])  # 나간 시점을 기준으로 카메라 설치
    for r in routes:
        if r[1] >= camera[-1] and r[0] <= camera[-1]:
            continue
        else:
            camera.append(r[1])
    return len(camera)

    return answer