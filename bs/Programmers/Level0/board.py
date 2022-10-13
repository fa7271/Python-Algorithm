
def solution(n):
    res = []
    for i in range(1,n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
            if count >= 3:
                res.append(i)
                break
    return len(res)
print(solution(10))
