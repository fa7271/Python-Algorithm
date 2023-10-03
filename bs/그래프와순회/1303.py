import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split()) # 가로n 세로m
board = [list(input()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
move = [(0,1),(0,-1),(1,0),(-1,0)]
res = [0,0]
def bfs(a,b):
    visited[a][b] = True
    compare = board[a][b]
    Q = deque([(a,b)])
    count = 1
    while Q:
        x,y = Q.popleft()
        for dx,dy in move:
            nx = x + dx # 비교대상 세로
            ny = y + dy # 비교대상 가로
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == compare:
                visited[nx][ny] = True
                count += 1
                Q.append((nx,ny))
    return count
for i in range(m): # 세로 m,
    for j in range(n): # 가로 n
        if not visited[i][j]:
            cnt = bfs(i,j)
            if board[i][j] =="W":
                res[0] += cnt**2
            else:
                res[1] += cnt**2
print(*res,sep="\n")
