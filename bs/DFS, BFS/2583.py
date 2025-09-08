import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

M,N,K = map(int,sys.stdin.readline().split(" "))
maps = [[0 for i in range(N)] for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split(" "))

    for i in range(y1,y2):
        for j in range(x1,x2):
            maps[i][j] = 1
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(x,y):
    q = deque([(x,y)])
    maps[x][y] = 1
    cnt = 1
    while q:
        x1, y1 = q.popleft()
        for dx, dy in move:
            nx = x1 + dx
            ny = y1 + dy
            if 0 <=nx<M and 0<=ny<N and maps[nx][ny] == 0:
                q.append((nx,ny))
                maps[nx][ny] = 1
                cnt += 1
    return cnt

cnt = 0
area = []
for i in range(M):
    for j in range(N):
        if maps[i][j] == 0:
            area.append((bfs(i,j)))
            cnt += 1
area.sort()

print(len(area))
print(*area)