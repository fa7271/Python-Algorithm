import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(input())
move = [(0,1),(0,-1),(1,0),(-1,0)]
 # 가로 세로 K갯수
def bfs(a,b):
    Q = deque([(a,b)])
    visited[a][b] = 0 # 1을 0 으로 방문했음
    while Q:
        x,y = Q.popleft()
        for sx, sy in move:
            dx, dy = x + sx, y + sy
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if visited[dx][dy] == 1:
                Q.append((dx,dy))
                visited[dx][dy] = 0

for i in range(T):
    M, N, K = map(int,input().split())
    visited = [[0]*(M) for _ in range(N)]
    cnt = 0
    for j in range(K):
        x, y = map(int, input().split(" "))
        visited[y][x] = 1
    for a in range(N):
        for b in range(M):
            if visited[a][b] == 1:
                bfs(a,b)
                cnt += 1

    print(cnt)
