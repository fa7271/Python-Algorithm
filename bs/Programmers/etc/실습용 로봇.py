def solution(command):

    start = [0,0]
    dir = [(0,1), # 위
           (1,0), # 오른쪽
           (0,-1),# 아래
           (-1,0)] # 왼쪽
    idx = 0
    for i in command:
        if i == "G":
           start[0] += dir[idx][0]
           start[1] += dir[idx][1]
        elif i == "B":
            start[0] -= dir[idx][0]
            start[1] -= dir[idx][1]
        elif i == "L":
            idx = (idx+3) % 4
        else:
            idx = (idx+1) % 4

    return start

print(solution("GRGLGRG"))
# print(solution("GRGRGRB"))