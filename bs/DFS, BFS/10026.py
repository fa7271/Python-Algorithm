import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
map = [list(sys.stdin.readline().rstrip()) for i in range(N)]
visited = [[False] * N for _ in range(N)]



move = [(1,0),( -1,0),(0,-1),(0,1)] #상,하,좌,우
def dfs(x, y):
    now_color = map[x][y]
    visited[x][y] = True
    for dx,dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and visited[nx][ny] == False:
            if now_color == map[nx][ny]: # 다음 색칠한 것과 같으면
                dfs(nx, ny)
tur = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] ==False:
            dfs(i, j)
            tur += 1
print(tur, end = " ")

for i in range(N):
    for j in range(N):
        if map[i][j] == "G":
            map[i][j] = "R"
visited = [[False] * N for i in range(N)]

tur = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] ==False:
            dfs(i, j)
            tur += 1
print(tur)







