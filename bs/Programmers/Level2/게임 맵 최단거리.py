# from collections import deque
#
# def solution(maps):
#     n, m = len(maps), len(maps[0])
#     visited = [[-1]*m for _ in range(n)]
#     visited[0][0] = 1
#     move = [(0,1), (1,0), (0,-1), (-1,0)]
#     q = deque([(0, 0)])
#
#     while q:
#         x, y = q.popleft()
#
#         if x==n-1 and y==m-1:
#             return visited[x][y]
#
#         for a, b in move:
#             dx, dy = x+a, y+b
#
#             if n>dx>=0 and m>dy>=0 and maps[dx][dy] == 1 and visited[dx][dy] == -1:
#                 q.append((dx,dy))
#                 visited[dx][dy] = visited[x][y] + 1
#
#     return -1


from collections import deque

def solution(maps):
    N, M = len(maps) , len(maps[0])
    visited = [[-1]*M for _ in range(N)]
    visited[0][0] = 1
    move = [(0,1), (0,-1),(-1,0),(1,0)]

    q = deque([(0,0)])

    while q:

        x, y = q.popleft()
        if x == N-1 and y == M - 1:
            return visited[x][y]
        for a, b in move:
            dx, dy = x+a , y+b # 들어갈 곳
            if N > dx >=0 and M > dy >=0 and visited[dx][dy] == -1 and maps[dx][dy] == 1:
                q.append((dx,dy))
                visited[dx][dy] = visited[x][y] + 1

    return -1





from collections import deque

def solution2(maps):
    N,M = len(maps), len(maps[0])

    visited = [[-1]*M for _ in range(N)]
    visited [0][0] = 1 # 시작점은  밟아서 1
    move = [(0,1),(0,-1),(1,0),(-1,0)]

    q = deque([(0,0)]) # 시작점

    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1 :
            return visited[x][y]
        for a, b in move:
            x_move, y_move = x + a, y + b
            if N > x_move >=0 and M > y_move >= 0 and visited[x_move][y_move] == -1 and maps[x_move][y_move] == 1:
                q.append((x_move,y_move))
                visited[x_move][y_move] = visited[x][y] + 1
    return -1


print(solution2([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
