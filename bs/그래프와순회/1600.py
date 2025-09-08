import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

k = int(input())
w, h = map(int, input().split(" "))
graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(h)]
monkey_move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
horse_move = [(-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1)]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
# x,y, 남은횟수

Q = deque([(0, 0, k)])
while Q:
    x, y, count = Q.popleft()
    if x == h - 1 and y == w - 1:
        print(visited[x][y][count])
        break
    if count > 0:
        for dx, dy in horse_move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < h and 0 <= ny < w :
                if graph[nx][ny] == 0 and visited[nx][ny][count - 1] == 0:
                    visited[nx][ny][count - 1] = visited[x][y][count] + 1
                    Q.append((nx, ny, count - 1))
    for dx, dy in monkey_move:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 0 and visited[nx][ny][count] == 0:
                visited[nx][ny][count] = visited[x][y][count] + 1
                Q.append((nx, ny, count))
else:
    print(-1)
