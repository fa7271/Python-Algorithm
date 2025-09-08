import sys
from collections import deque

T = int(input())
move = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

def bfs(a,b):
    queue = deque([(a,b)])
    while queue:
        x, y = queue.popleft()
        if x == na and y == nb:
            return  board[x][y] -1
        for xx, yy in move:
            nx,ny = x+xx, y+yy
            if 0 <= nx < N and 0 <= ny <N and board[nx][ny] == 0:
                queue.append((nx,ny))
                board[nx][ny] = board[x][y] + 1
for i in range(T):
    N = int(input())
    a, b = map(int,input().split(" "))
    na, nb = map(int,input().split(" "))

    board = [[0] * N for _ in range(N)]
    board[a][b] = 1

    print(bfs(a,b))
