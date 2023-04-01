def solution(park, routes):
    answer = []
    start = []

    for i in range(len(park)):
        if 'S' in park[i]:
            start = [i, park[i].find('S')]
            break
    print(start)
    for route in routes:
        dir, move = route.split(' ')
        move = int(move)

        if dir == 'E':
            loc = start[1] + move
            if loc >= len(park[0]):
                continue
            if 'X' in park[start[0]][start[1]+1:loc+1]:
                continue
            else:
                start[1] = loc

        elif dir == 'W':
            loc = start[1] - move
            if loc < 0:
                continue
            if 'X' in park[start[0]][loc:start[1]]:
                continue
            else:
                start[1] = loc

        elif dir == 'S':
            loc = start[0] + move
            if loc >= len(park):
                continue
            if 'X' in [park[i][start[1]] for i in range(start[0]+1,loc+1)]:
                continue
            else:
                start[0] = loc

        elif dir == 'N':
            loc = start[0] - move
            if loc < 0:
                continue
            if 'X' in [park[i][start[1]] for i in range(loc,start[0])]:
                continue
            else:
                start[0] = loc

    return start


print(solution(	["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
# print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))

