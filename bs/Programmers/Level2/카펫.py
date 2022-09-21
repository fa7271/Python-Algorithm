def solution(brown, yellow):
    total = brown + yellow
    res = []

    for i in range(1,total+1):
        if total % i == 0:
            res.append([i, total//i])
    # for i in range(len(res)):
    #     if res[i][0] >= res[i][1]:
    #         return res[i]

    for x, y in res:
        if(x -2) * ( y -2 ) == yellow:
            return [y,x]
print(solution(24,24))