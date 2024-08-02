import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * (m + 1) for _ in range(n + 1)]

res = [0, 0]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(a, b):
    visited[a][b] = True
    Q = deque([(a, b)])
    left, right = 0, 0
    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != "#" and not visited[nx][ny]:
                visited[nx][ny] = True
                Q.append((nx, ny))
                if graph[nx][ny] == "o":
                    left += 1
                elif graph[nx][ny] == "v":
                    right += 1
    if left > right:
        return [left, 0]
    else:
        return [0, right]


for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            if graph[x][y] == "#":
                count = bfs(x, y)
                res[0] += count[0]
                res[1] += count[1]
print(*res)
