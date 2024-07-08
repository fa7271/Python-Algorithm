import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

move = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

while True:
    l, r, c = map(int, sys.stdin.readline().rstrip().split(" "))
    if l == r == c == 0:
        break

    graph = []
    for _ in range(l):
        graph.append([list(input().strip()) for _ in range(r)])
        temp = input()
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]

    q = deque()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    start = (i, j, k, 0)
                    visited[i][j][k] = True
                if graph[i][j][k] == 'E':
                    end = (i, j, k)

    q.append(start)

    while q:
        floor, x, y, count = q.popleft()
        if (floor, x, y) == end:
            print(f'Escaped in {count} minute(s).')
            break
        for df, dx, dy in move:
            nf = df + floor
            nx = dx + x
            ny = dy + y
            if 0 <= nf < l and 0 <= nx < r and 0 <= ny < c and not visited[nf][nx][ny]:
                if graph[nf][nx][ny] == "." or graph[nf][nx][ny] == "E":
                    visited[nf][nx][ny] = True
                    q.append((nf, nx, ny, count + 1))

    else:
        print("Trapped!")
