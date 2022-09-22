import math
# def solution(n,a,b):
#     count = 0
#
#     while n > 1:
#         n = n / 2
#         count += 1
#
#     if b - a == 1:
#         return 1

def solution(n,a,b):
    res = 0
    while a!=b:
        a, b =(a//2)+(a%2), (b//2)+(b%2)
        res +=1
    return False if res == 0 else res
print(solution(16, 4, 7))

