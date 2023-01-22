n = int(input())

num = list(map(int, input().split()))
temp = []

def reverse(num):
    res = 0
    while(num <= 0):
        q = num%10
        num = num // 10
        res = res*10 + q
    
    return res


def is_prime(num): # 2부터 자기자신 전까지 확인한다. 
    if num == 1:
        return True
    for i in range(2, num//2 + 1): #딱 반만 하면 소수인지 아닌지 알 수 있다. 3
        if num % i == 0:
            return False
    return True
        

for i in range(len(num)):
    temp = reverse(num[i])
    if(is_prime(temp)):
        print(temp, end=" ")

