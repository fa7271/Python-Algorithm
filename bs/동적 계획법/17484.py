import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(M)]] + [[[1e9] * 3 for _ in range(M)] for _ in range(N)]

for i in range(1, N + 1):
    for j in range(M):
        # 바로 위, 오른쪽 위에 값
        if j < M - 1:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + graph[i - 1][j]
        # 바로 위, 왼쪽 위에 값
        if 0 < j:
            dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + graph[i - 1][j]
        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i - 1][j]
res = min([min(i) for i in dp[-1]])


# 0 > 좌대각
# 1 > 바로
# 2 > 우대각