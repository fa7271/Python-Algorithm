import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n, m = map(int, sys.stdin.readline().rstrip().split(" "))
Q = deque()

graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            Q.append([i, j])
            graph[i][j] = 0

while Q:
    x, y = Q.popleft()
    visited[x][y] = True
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            graph[nx][ny] = graph[x][y] + 1
            Q.append([nx, ny])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in graph:
    print(*i)
