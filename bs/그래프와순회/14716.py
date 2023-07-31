import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int,sys.stdin.readline().split(" "))
lst = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
visited= [[False] * M for _ in range(N)]

Q = deque()
def bfs(a,b):
    Q.append([a,b])
    visited[a][b] = True
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 1 and visited[nx][ny] == False:
                Q.append([nx,ny])
                visited[nx][ny] = True

count = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1 and visited[i][j] == False:
            bfs(i,j)
            count += 1

print(count)

