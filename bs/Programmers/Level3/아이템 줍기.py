from collections import deque
import matplotlib.pyplot as plt
import numpy


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 102 for _ in range(102)]
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # 속 색칠
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 0
                # 테두리  색칠
                elif graph[x][y] != 0:
                    plt.scatter(x, y)
                    graph[x][y] = 1
    plt.show()

    characterX = characterX * 2
    characterY = characterY * 2
    itemY = itemY * 2
    itemX = itemX * 2

    Q = deque()
    Q.append((characterX,characterY))
    visited = [[1] * 102 for _ in range(102)]
    visited[characterX][characterY] = 0

    while Q:
        x, y = Q.popleft()
        if x == itemX and y == itemY :
            print(visited[x][y] // 2)
            break
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 < nx <= 102 and 0 < ny <= 102 and graph[nx][ny] == 1 and visited[nx][ny] == 1:
                Q.append((nx, ny))
                visited[nx][ny] += visited[x][y]

print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))  # 17
