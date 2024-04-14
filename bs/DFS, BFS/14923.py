import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split(" "))
hx, hy = map(int, sys.stdin.readline().split(" "))
ex, ey = map(int, sys.stdin.readline().split(" "))
graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

# 방문 배열, 0번째는 통과 1번째는 벽부수고 통과
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(x, y):
    Q = deque([(x, y, 0)])
    visited[x][y][0] = 1
    while Q:
        dx, dy, wall = Q.popleft()
        if dx == ex - 1 and dy == ey - 1:
            return visited[dx][dy][wall] - 1

        for a, b in move:
            nx, ny = a + dx, b + dy

            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny] and not visited[nx][ny][wall]:
                Q.append((nx, ny, wall))
                visited[nx][ny][wall] = visited[dx][dy][wall] + 1

            elif 0 <= nx < n and 0 <= ny < m and graph[nx][ny] and not visited[nx][ny][wall] and not wall:
                Q.append((nx, ny, wall+1))
                visited[nx][ny][wall+1] = visited[dx][dy][wall] + 1

    return -1

print(bfs(hx - 1, hy - 1))