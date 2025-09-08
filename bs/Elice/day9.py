import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 순서대로 모아 단어 ELICE

import heapq
import sys

INF = float('inf')


def dijkstra(start, grid, N):
    pq = [(0, start[0], start[1])]
    dist = [[INF] * N for _ in range(N)]
    dist[start[0]][start[1]] = 0

    while pq:
        d, x, y = heapq.heappop(pq)
        if d > dist[x][y]:
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nd = d + grid[x][y] + grid[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))
    return dist


def solution():
    N = int(input())
    grid = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]
    letters = [[x-1, y-1] for x, y in (map(int, sys.stdin.readline().split()) for _ in range(5))]

    res = 0
    idx = 0
    start = (0, 0)
    E1, L, I, C, E2 = letters

    dist_start = dijkstra(start, grid, N)
    dist_E1 = dijkstra(E1, grid, N)
    dist_E2 = dijkstra(E2, grid, N)
    dist_L = dijkstra(L, grid, N)
    dist_I = dijkstra(I, grid, N)
    dist_C = dijkstra(C, grid, N)
    path1 = (
            dist_start[E1[0]][E1[1]] +
            dist_E1[L[0]][L[1]] +
            dist_L[I[0]][I[1]] +
            dist_I[C[0]][C[1]] +
            dist_C[E2[0]][E2[1]]
    )
    path2 = (
            dist_start[E2[0]][E2[1]] +
            dist_E2[L[0]][L[1]] +
            dist_L[I[0]][I[1]] +
            dist_I[C[0]][C[1]] +
            dist_C[E1[0]][E1[1]]
    )
    return min(path1, path2)

print(solution())

