import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split(" "))
x, y  = list(map(int,input().split(" ")))
enemy = [list(map(int,input().split(" "))) for i in range(m)]
board = [[0]*n for _ in range(n)]

board[x-1][y-1] = 1
move = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
def bfs(x,y):
    Q = deque([(x, y)])
    board[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                Q.append([nx,ny])
bfs(x-1,y-1)
for x, y in enemy:
    print(board[x-1][y-1] , end = " ")