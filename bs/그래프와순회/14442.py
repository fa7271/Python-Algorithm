import sys

from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, k = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
Q = deque([(0, 0, k)])
visited[0][0][k] = 1
while Q:
    x, y, count = Q.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][count])
        exit()
    for dx, dy in move:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and count > 0 and visited[nx][ny][count - 1] == 0:
                visited[nx][ny][count - 1] = visited[x][y][count] + 1
                Q.append((nx, ny, count - 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][count] == 0:
                visited[nx][ny][count] = visited[x][y][count] + 1
                Q.append((nx, ny, count))
else:
    print(-1)
