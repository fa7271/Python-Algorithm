import math
def solution(n):
    x = n ** (1/2)
    return (x + 1)**2 if x % 1 == 0 else -1
print(solution(121))