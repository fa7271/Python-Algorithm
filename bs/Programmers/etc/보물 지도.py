def solution(n, m, hole):
    maps = [[0]*n for _ in range(m)]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    shoes = [(0,2),(0,-2),(2,0),(-2,0)]

    visited =[[[False] * 2 for _ in range(m) ] for _ in range(n)]
    visited[0][0][False] = True
    print(visited[0][0])
    visited[0][0][True] = True
    print(visited[0][0])
    for x, y in hole:
        maps[y-1][x-1] = -1


# print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))