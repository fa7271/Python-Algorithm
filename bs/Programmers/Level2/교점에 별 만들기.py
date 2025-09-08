from itertools import combinations

def meet_spot(x, y):
    a,b,c = x  # ax+by=c
    d,e,f = y  # dx+ey=f
    if a*e == b*d:
        return
    x = (b * f - c * e) / (a * e - b * d)
    y = (c * d - a * f) / (a * e - b * d)
    if x== int(x) and y == int(y) :
        return int(x), int(y)

def solution(line):
    xy_spot = set() # 교점에 들어갈것들
    for a, b in list(combinations(line,2)):
        spot = meet_spot(a,b)
        if spot:
            xy_spot.add(spot)

    y_spot = sorted(xy_spot, key=lambda x : x[1]) # y최소 최대값
    x_spot = sorted(xy_spot, key=lambda x : x[0]) # x 최소 최대

    min_x, max_x =x_spot[0][0],x_spot[-1][0]
    min_y, max_y =y_spot[0][1],y_spot[-1][1]

    board = [['.'] * (max_x - min_x +1) for _ in range(max_y - min_y +1)]

    for x,y in xy_spot:
        board[max_y - y][x-min_x] = "*"
    res = []
    for i in board:
        res.append("".join(i))
    return list(map("".join,board))

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
def study(n):
    lst = [[0]*n for _ in range(10)]
    return "".join(lst)
print(study(5))



