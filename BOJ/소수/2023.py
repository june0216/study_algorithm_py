n = int(input())
start = [2, 3, 5, 7]
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return False
    return True

def dfs(num):
	# 목표 길이 도달 시 멈춤
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp=num*10+i
            if isPrime(temp):
                dfs(temp)

for s in start:
    res = dfs(s)
    if res is not None:
        print(res)