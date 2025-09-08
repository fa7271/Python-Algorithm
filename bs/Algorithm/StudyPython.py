a= [ (x*y) for x in range(1,10) for y in range(1,10)]


# 반복문 사용 팩토리얼
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# 재귀함수 사용 팩토리얼

def factorial(n):
    if n=1:
        return 1
    return n * factorial(n-1)

# 피보나치 수열
def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1

    for i in range(1,n):
        a,b = b, a+b

    return a