import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(str, input())) for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for x in range(n):
    for y in range(m):
        if graph[x][y] == "R":
            rx, ry = x, y
        elif graph[x][y] == "B":
            bx, by = x, y
Q = deque()
count = 0
Q.append((rx, ry, bx, by, count))


def moving(now_x, now_y, x, y):
    move = 0
    nx = now_x
    ny = now_y
    while True:
        if graph[nx + x][ny + y] != "#" and graph[nx + x][ny + y] != "O":
            nx += x
            ny += y
            move += 1
        else:
            break
    return nx, ny, move


while Q:
    rx, ry, bx, by, count = Q.popleft()
    if count > 10:
        continue
    for dx, dy in move:
        r_nx, r_ny, r_step = moving(rx, ry, dx, dy)
        b_nx, b_ny, b_step = moving(bx, by, dx, dy)
        if graph[b_nx + dx][b_ny + dy] == "O":
            continue

        if graph[r_nx + dx][r_ny + dy] == "O" and count < 10:
            print(1)
            exit()
        # 똑같은 지역에 도착함
        # 그럼 카운트 낮은곳이 한칸 위에 있음
        if r_nx == b_nx and r_ny == b_ny:
            if r_step > b_step:
                r_nx -= dx
                r_ny -= dy
            else:
                b_nx -= dx
                b_ny -= dy
        # 둘다 못 움직이는 경우
        if rx == r_nx and ry == r_ny and bx == b_nx and by == b_ny:
            continue
        Q.append((r_nx, r_ny, b_nx, b_ny, count + 1))
print(0)
