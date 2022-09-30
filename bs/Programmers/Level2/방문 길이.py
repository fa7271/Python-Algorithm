
def solution(dirs):
    start = set()
    x = 0; y = 0
    for d in dirs:
        if d == 'U' and y < 5:
            start.add(((x, y), (x, y+1)))
            y += 1

        elif d == 'D' and y > -5:
            start.add(((x, y-1), (x, y)))
            y -= 1

        elif d == 'R' and x < 5:
            start.add(((x, y), (x+1, y)))
            x += 1

        elif d == 'L' and x > -5:
            start.add(((x-1, y), (x, y)))
            x -= 1
    return len(start)
    # count = 0
    #
    # start =[]
    # start.append([0,0])
    # for i in dirs:
    #     if i == "L":
    #         start.append([ start[-1][0] -1, start[-1][1] ])
    #     elif i == "R":
    #         start.append([ start[-1][0] +1, start[-1][1] ])
    #     elif i == "U":
    #         start.append([ start[-1][0] , start[-1][1] +1 ])
    #     elif i == "D":
    #         start.append([ start[-1][0] , start[-1][1] -1 ])
    # print(start)
    # set_list = list(set(map(tuple,start)))
    # print(set_list)
    # for x, y in set_list:
    #     if abs(x) > 5 or abs(y) > 5:
    #         count += 1
    # return len(set_list) - count

print(solution("LULLLLLLUD"))