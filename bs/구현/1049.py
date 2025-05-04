
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
brands = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

INF = 10**9
dp = [INF] * 101
dp[0] = 0

for i in range(1, n + 1):
    for pack, single in brands:
        # 낱개 구매
        dp[i] = min(dp[i], dp[i - 1] + single)
        # 패키지 구매 (i가 6 이상일 때만)
        if i >= 6:
            dp[i] = min(dp[i], dp[i - 6] + pack)
        else:
            # i < 6인데 패키지로 덮어써도 되면
            dp[i] = min(dp[i], pack)

print(dp[n])