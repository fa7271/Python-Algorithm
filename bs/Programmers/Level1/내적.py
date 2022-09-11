def solution(a, b):
    res = []
    for a, b in zip(a, b):
        print(a*b)
        res.append(a*b)
    return(sum(res))

    return sum([a * b for a,b in zip(a,b)])



print(solution([1,2,3,4],[-3,-1,0,2]))
