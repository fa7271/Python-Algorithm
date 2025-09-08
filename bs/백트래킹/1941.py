import sys
from collections import deque
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(5)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
positions = [(i, j) for i in range(5) for j in range(5)]
combis = list(combinations(positions, 7))
count = 0


def checkS(combi):
    return sum(1 for x, y in combi if graph[x][y] == "S") >= 4


# 다 연결되어있는지 확인
def checkBFS(combi):
    visited = [False] * 7
    Q = deque([(combi[0])])
    visited[0] = True

    while Q:
        x, y = Q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if (nx, ny) in combi and not visited[combi.index((nx, ny))]:
                visited[combi.index((nx, ny))] = True
                Q.append((nx, ny))
    return False if False in visited else True
res = 0
for combi in combis:
    if checkS(combi):
        if checkBFS(combi):
            res += 1

print(res)
