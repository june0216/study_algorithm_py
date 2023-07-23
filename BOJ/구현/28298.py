N, M, K = map(int, input().split())
#처음에 패턴을 먼저 찾아야하나?라고 생각했지만 먼저 K*K 타일을 나눈 뒤 각 위치에서 가장 많이 나온 알파벳을 선택한다.
table = [list(input()) for _ in range(N)] #입력받기
count = 0 #타일의 최소 개수

for x in range(K): # 패턴 K*K로 분할한 영역을 확인, 0~K의 범위의  (x, y) 값들을 하나씩 확인하여 매순간 가장 많이 나타난 알파벳을 선택한다. (그리디)
    for y in range(K):
        alphabet = [0]*26 # 계수 정렬 -> 알파벳의 개수 세기(영문 알파벳이 26자)
        for i in range(0, N - K+ 1, K): #table을 K*K로 나눈 것들 영역의 위치(i, j) 하나씩 확인 -> K 구간씩 건너뛰기
            for j in range(0, M - K + 1, K):
                t = table[i + x][j + y] #K*K 분할한 각각의 영역 탐색 ->  (i, j)의 알파벳 확인
                alphabet[ord(t) - 65] += 1 #알파벳 개수 count
                #ord() -> 아스키코드 값을 정수형으로 반환,  ASCII 값에서 65('A'의 ASCII 값)을 뺌, 이렇게 하면 'A'부터 'Z'까지 각 알파벳에 대응하는 0부터 25 사이의 숫자를 얻을 수 있음

        max_alphabet = chr(alphabet.index(max(alphabet))+65) #각 영역들의 (i, j)위치에서 가장 많이 나타난 알파벳 찾기
        # chr () -> 유니코드 숫자에 해당하는 문자 변환

        #타일 변환 과정
        for i in range(0, N - K+ 1, K):
            for j in range(0, M - K + 1, K):
                if table[i + x][j + y] != max_alphabet: # 가장 많이 나온 알파벳이 아니라면 변환
                    table[i + x][j + y] = max_alphabet
                    count +=1 # 타일 변환 count 증가
print(count)
for t in table:
    print("".join(t))



