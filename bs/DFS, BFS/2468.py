import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())

maps = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(N)]
def dfs(x,y,k):
    move = [(1,0),( -1,0),(0,-1),(0,1)]
    visited[x][y] = True
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] > k and not visited[nx][ny]:
            dfs(nx, ny, k)
lst = []
for k in range(max(map(max, maps))):
    count = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                count += 1
    lst.append(count)
print(max(lst))