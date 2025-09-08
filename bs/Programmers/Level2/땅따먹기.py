def solution(land):
    res = []
    print(land[0][:0])
    print(land[0][1:])

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:]) # 그전에 쓴 열 제거 하려고 슬라이씽 사용
            print(land)
    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))