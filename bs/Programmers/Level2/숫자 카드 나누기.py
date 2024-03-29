
from math import gcd
def get_gcd(arr):
    g = arr[0]
    for i in range(1,len(arr)):
        g = gcd(g,arr[i])
    return g
def solution(arrayA, arrayB):
    res = 0
    A, B = get_gcd(arrayA), get_gcd(arrayB)

    for i in arrayB:
        if i % A == 0:
            break
    else:
        res = max(A,res)

    for i in arrayA:
        if i % B == 0:
            break
    else:
        res = max(B,res)

    return res





print(solution(	[10, 17], [5, 20]))
print(solution(	[10, 20],[5, 17]))
print(solution([14, 35, 119],[18, 30, 102]))

