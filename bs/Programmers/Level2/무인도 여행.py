import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    global totalSum
    answer = []
    maps = [list(map) for map in maps]
    totalSum = 0
    print(maps)
    def dfs(a, b):
        global totalSum
        maps[a][b] = 'X'

        move = [(1,0),(-1,0),(0,1),(0,-1)]

        for i, j in move:
            mx = b + i
            my = a + j

            if 0 <= my < len(maps) and 0 <= mx < len(maps[0]) and maps[my][mx] != "X":
                totalSum += int(maps[my][mx])
                print(totalSum)
                dfs(my, mx)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if 0 <= i < len(maps) and 0 <= j < len(maps[0]) and maps[i][j] != "X":
                totalSum = int(maps[i][j])
                dfs(i, j)
                if totalSum != 0:
                    answer.append(totalSum)

    if len(answer) == 0:return [-1]
    else:return sorted(answer)

print(solution(	["X591X", "X1X5X", "X231X", "1XXX1"]))