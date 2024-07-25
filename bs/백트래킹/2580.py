import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])


# 가로 체크
def row(node, n):
    for x in range(9):
        if n == graph[node][x]:
            return False
    return True


# 세로 체크
def col(node, n):
    for y in range(9):
        if n == graph[y][node]:
            return False
    return True


# 사각형 체크
def square(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == graph[x // 3 * 3 + i][y // 3 * 3 + j]:
                return False
    return True


def dp(depth):
    if depth == len(blank):
        for i in graph:
            print(*i)
        exit(0)
    for i in range(1, 10):
        x, y = blank[depth]
        if col(y, i) and row(x, i) and square(x, y, i):
            graph[x][y] = i
            dp(depth + 1)
            graph[x][y] = 0
dp(0)
