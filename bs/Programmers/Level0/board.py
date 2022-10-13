
def solution(n):
    res = []
    for i in range(1,n+1):
        j = 1
        while j < i:
            count = 2
            print(count)
            if i % j == 0:
                count += 1
            if count >= 3:
                res.append(j)
                break
            j += 1
    print(res)
print(solution(10))
