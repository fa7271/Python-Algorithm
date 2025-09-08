from collections import deque
def solution(maps):

    def bfs(start,end,start2,end2):
        move = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
        visited[start][end] = 0
        print(visited)
        Q = deque([(start,end)])

        while Q:
            x, y = Q.popleft()
            if x == start2 and y == end2:
                return visited[start2][end2]
            for a, b in move:
                nx, ny = x+a, y+b
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0])  and visited[nx][ny] == -1 and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx,ny))
        return -1

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                S = (i,j)
            if maps[i][j] == 'L':
                L = (i,j)
            if maps[i][j] == "E":
                E = (i,j)

    answer = -1
    answer2 = bfs(S[0],S[1],L[0],L[1])
    answer3 = bfs(L[0],L[1],E[0],E[1])
    if answer2 != -1 and answer3 != -1:
        answer = answer2 + answer3
    return answer



print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
# print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
