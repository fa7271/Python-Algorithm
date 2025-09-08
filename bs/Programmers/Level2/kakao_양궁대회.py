def solution(n, info):
    point = 0
    for x,y in enumerate(reversed(info)):
        if y != 0:
            point += x
    print(point)
print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
