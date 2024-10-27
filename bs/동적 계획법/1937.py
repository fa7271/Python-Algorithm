import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dp = [[-1] * n for _ in range(n)]


def dfs(x, y):
    # 메모제이션 되어있음
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))  # 1을 더해 최대값 갱신
    return dp[x][y]


res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))
print(res)
