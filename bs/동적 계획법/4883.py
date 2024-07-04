import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
count = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][0] = graph[1][0] + graph[0][1]  # 좌대각
    dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][2] + graph[0][1])  # 바로내려오기, 오아
    dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1] + graph[0][2])  # 바로내려오기, 오아
    if n >= 2:
        for i in range(2, n):
            dp[i][0] = graph[i][0] + min(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = graph[i][1] + min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
            dp[i][2] = graph[i][2] + min(dp[i][1], dp[i - 1][1], dp[i - 1][2])
    print(count, dp[-2][1], sep=". ")
    count += 1
