import sys
from itertools import combinations
from collections import defaultdict, deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, g, r = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
possible_start_spot = []
res = -1e9

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            possible_start_spot.append((x, y))


def find():
    flower = 0
    while Q:
        a, b, color, time = Q.popleft()
        # 이미 꽃이 피어있다면 continue
        if visited[a][b] == 1:
            continue
        for dx, dy in move:
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                if not visited[nx][ny]:  # 아직 배양액이 퍼지지 않은 경우
                    visited[nx][ny] = (color, time + 1)
                    Q.append((nx, ny, color, time + 1))
                elif visited[nx][ny] == 1:
                    continue
                elif visited[nx][ny][0] != color and visited[nx][ny][1] == time + 1:
                    flower += 1
                    visited[nx][ny] = 1  # 꽃 표시

    return flower


# 배양액을 놓을 수 있는 위치의 조합을 구함
for total in combinations(possible_start_spot, g + r):
    for green in combinations(total, g):
        visited = [[0] * m for _ in range(n)]
        Q = deque()

        # 초록색 배양액
        for gx, gy in green:
            visited[gx][gy] = (1, 0)
            Q.append((gx, gy, 1, 0))

        # 빨간색 배양액
        red_candidates = set(total) - set(green)
        for red in combinations(red_candidates, r):
            for rx, ry in red:
                visited[rx][ry] = (-1, 0)
                Q.append((rx, ry, -1, 0))

            # 시뮬레이션
        res = max(res, find())
print(res)
