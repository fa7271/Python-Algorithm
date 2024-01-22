import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n, m = map(int, sys.stdin.readline().split(" "))
graph = [list(map(str, sys.stdin.readline())) for _ in range(n)]
rx, ry, bx, by, end_x, end_y, = 0, 0, 0, 0, 0, 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == "R":
            rx, ry = x, y
        if graph[x][y] == "B":
            bx, by = x, y
        if graph[x][y] == "O":
            end_x, enx_y = x, y

visited = set()
Q = deque()
Q.append((rx, ry, bx, by, 1))
visited.add((rx, ry, bx, by))
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def move(x, y, dx, dy):
    count = 0
    while graph[x + dx][y + dy] != "#" and graph[x][y] != "O":
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    while Q:
        rx, ry, bx, by, count = Q.popleft()
        if count > 10:
            break
        for dx, dy in moves:
            nrx, nry, rc = move(rx, ry, dx, dy)
            nbx, nby, bc = move(bx, by, dx, dy)

            #    같이 빠지면 안됨
            if graph[nbx][nby] == "O":
                continue

            if graph[nrx][nry] == "O":
                return count
            #     같은 지점일수는 없음
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                Q.append((nrx, nry, nbx, nby, count + 1))
    return -1
print(bfs())