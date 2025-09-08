import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(2)]
    if n > 1:
        # 첫 번째 그림 뜯어냈을 때
        dp[0][1] += dp[1][0]
        # 두 번째 그림 뜯어냈을 때
        dp[1][1] += dp[0][0]

    # 지그재그로 뜯기 vs 한번 건너 뛰기
    for i in range(2, n):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))
