import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
res = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(a, b):
    Q = deque([(a, b)])
    visited[a][b] = 1

    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 아직 치즈 못만남
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[nx][ny] + 1


while True:
    visited = [[0] * m for _ in range(n)]

    # start 0,0 fix
    bfs(0, 0)
    res += 1
    air = 0
    for x in range(n):
        for y in range(m):
            if visited[x][y] >= 2:
                graph[x][y] = 0
    temp_res = sum(1 for i in range(n) for j in range(m) if graph[i][j] == 0)
    if temp_res == (n * m):
        print(res)
        exit()
