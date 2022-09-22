def solution(arr):
    arr.sort()
    max = arr[-1]
    res = arr[-1]
    while True:
        for i in range(len(arr) - 1):
            if res % arr[i] != 0:
                break
        else:
            return res
        res += max
print(solution([2,6,8,14]))

from fractions import gcd

def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer