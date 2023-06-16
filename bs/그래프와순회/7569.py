import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque
sys.setrecursionlimit(10**6)
N,M,H = map(int,sys.stdin.readline().split())

move = [(0,1),(0,-1),(1,0),(-1,0),(0+H,0),(0-H,0)] # 이동방향 상하좌우
Q = deque([])
graph = []
for i in range(H):
    tmp = []
    for j in range(M):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(N):
            if tmp[j][k] == 1:
                Q.append([i,j,k])
    graph.append(tmp)
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while Q:
    x,y,z = Q.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0<=nx<H and 0<=ny<M and 0<=nz<N and graph[nx][ny][nz]==0:
            Q.append([nx,ny,nz])
            graph[nx][ny][nz] = graph[x][y][z]+1
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)

