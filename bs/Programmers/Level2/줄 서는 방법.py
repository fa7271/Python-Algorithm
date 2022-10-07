import math
from itertools import permutations
def solution(n, k):
    arr = [i for i in range(1,n+1)]
    print(arr)
    res = []
    while n != 0:
        fac = math.factorial(n-1)
        idx , k = (k-1)//fac, k % fac
        res.append(arr.pop(idx))
        n -= 1
    return res
print(solution(3,5))
# //몫 , %나머지