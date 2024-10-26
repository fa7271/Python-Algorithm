import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, k = map(int, input().split())

graph = [list(map(str, input())) for _ in range(n)]
word = input().rstrip()
dp = [[[-1 for _ in range(len(word))] for _ in range(m)] for _ in range(n)]
res = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, idx):
    # 이미 메모제이션 되어있음\
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]
    #  글자 완성
    if idx == len(word) - 1:
        return 1

    dp[x][y][idx] = 0
    for i in range(1, k + 1):
        for dx, dy in move:
            nx = x + (i * dx)
            ny = y + (i * dy)
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == word[idx + 1]:
                dp[x][y][idx] += dfs(nx, ny, idx + 1)


    return dp[x][y][idx]

print(graph)

for r in range(n):
    for c in range(m):
        if graph[r][c] == word[0]:
            res += dfs(r, c, 0)
print(res)
