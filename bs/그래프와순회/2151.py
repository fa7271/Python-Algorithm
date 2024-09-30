import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 4개의 방향에서 빛이 날라옴, 각좌표마다 날라오는 빛의 방향마다 가져야함. 3차원?
# 각 좌표 마다의 도착하는 빛의 방향 별로 거울 갯수 필요 최신화
# 다익스? 굳이? 최단거리니까


N = int(input())

graph = [list(map(str, input())) for _ in range(N)]
mirrors = []
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 방향 순서 변경 (우, 하, 좌, 상)
for x in range(N):
    for y in range(N):
        if graph[x][y] == "#":
            mirrors.append((x, y))
# 시작
sx, sy = mirrors[0]
graph[sx][sy] = "Start"


def bfs(sx, sy):
    Q = deque()
    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    for direction in range(4):
        Q.append((sx, sy, direction))
        visited[sx][sy][direction] = 1
    while Q:
        current_x, current_y, current_direction = Q.popleft()
        dx, dy = move[current_direction]
        nx, ny = current_x, current_y
        while True:
            nx = nx + dx
            ny = ny + dy
            # print(current_x, current_y, nx, ny,Q)
            if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == "*":
                break
            if graph[nx][ny] == "!":
                # 가던 방향
                if not visited[nx][ny][current_direction]:
                    Q.append((nx, ny, current_direction))
                    visited[nx][ny][current_direction] = visited[current_x][current_y][current_direction]
                # 가다가 오른쪽
                if not visited[nx][ny][(current_direction + 1) % 4]:
                    Q.append((nx, ny, (current_direction + 1) % 4))
                    visited[nx][ny][(current_direction + 1) % 4] = visited[current_x][current_y][current_direction] + 1
                # 가다가 왼쪽
                if not visited[nx][ny][(current_direction - 1) % 4]:
                    Q.append((nx, ny, (current_direction - 1) % 4))
                    visited[nx][ny][(current_direction - 1) % 4] = visited[current_x][current_y][current_direction] + 1
            elif graph[nx][ny] == "#":
                return visited[current_x][current_y][current_direction] - 1


print(bfs(sx, sy))
