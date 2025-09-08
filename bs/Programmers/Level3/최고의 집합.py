def solution(n, s):
    if n > s :
        return [-1]
    if n == s:
        return [1 for i in range(n)]

    res = []
    a, b  = s // n , s % n

    for i in range(n):
        res.append(a)

    idx = len(res) -1

    for i in range(b):
        res[idx] +=1
        idx -=1
    return res

print(solution(2, 9))
# print(solution(2, 1))
print(solution(2, 8))


