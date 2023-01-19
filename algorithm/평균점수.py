n = map(int , input())

s = list(map(int, input()))

#round_half_even 방식이다. 짝수 값으로 근사값으로 채택
print(round(4.5))
print(round(5.5))
# int(6.5 + 0.5)로 하는 것이 즉 반올림이다. 


ev = int(sum(s)/len(s) + 0.5)
min = 0
index = 0

for i in range(len(s)):
    if min < abs(s[i] - ev):
        min = s[i]

print(s.index(min))

