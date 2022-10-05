

def solution(n):
    tri = [[0 for i in range(1, n+1)] for i in range(1, n+1)]
    num = 1
    x,y =-1, 0
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            elif i % 3 == 2: # 위쪽 대각선
                x -= 1
                y -= 1
            tri[x][y] = num
            num += 1
    res = []

    for i in tri:
        for j in i:
            if j != 0:
                res.append(j)
    return res


print(solution(5))



