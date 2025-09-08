
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int,sys.stdin.readline().split(" "))
board = [list(input().strip()) for _ in range(N)]
move = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(N):
    for j in range(M):
        if board[i][j] == ".":
            board[i][j] = 0
        elif board[i][j] == "#":
            board[i][j] = 1
Q =deque()
def bfs(x, y):
    Q.append([x, y])
    visited[x][y] = True
    v, k = 0, 0
    while Q:
        x, y = Q.popleft()
        if board[x][y] == 'v':
            v += 1
        elif board[x][y] == 'k':
            k += 1
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0<= ny < M and board[nx][ny] != 1 and visited[nx][ny] == False :
                Q.append((nx,ny))
                visited[nx][ny] = 1
    if v >= k:
        k = 0
    else:
        v = 0
    return [v,k]


V,K = 0,0
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] != 1 and visited[i][j] == False:
            v, k = bfs(i,j)
            V += v
            K += k
print(K,V)
