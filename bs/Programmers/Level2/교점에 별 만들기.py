from itertools import combinations

def meet_spot(x, y):
    a,b,c = x  # ax+by=c
    d,e,f = y  # dx+ey=f
    if a*e == b*d:
        return
    x = (b * f - c * e) / (a * e - b * d)
    y = (e * d - a * f) / (a * e - b * d)
    if x== int(x) and y == int(y) :
        return int(x), int(y)

def solution(line):

    xy_spot = set()
    for a, b in list(combinations(line,2)):
        spot = meet_spot(a,b)
        if spot:
            xy_spot.add(spot)
    print(xy_spot)
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
# print(solution([[1, -1, 0], [2, -1, 0]]))
# print(solution([[1, -1, 0], [2, -1, 0]]))

