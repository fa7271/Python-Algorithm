import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split(" "))
graph = [list(map(int, input())) for _ in range(n)]
result = 0
# 정사각형 크기
for k in range(n + 1):
    # x 좌표
    for x in range(n):
        # y좌표
        for y in range(m):
            if x+k < n and y + k < m and graph[x][y] == graph[x][y + k] == graph[x + k][y] == graph[x + k][y + k]:
                result = max((k + 1) ** 2, result)
print(result)
# 002,012,022,032 102,112,132,
# 003,013,023
