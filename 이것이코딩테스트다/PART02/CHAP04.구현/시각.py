h = int(input())
count = 0

#문자열 자료형으로 변환해서 숫자가 있는지 확인
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            temp = str(i)+str(j)+str(k)
            if '3' in temp:
                count +=1
print(count)