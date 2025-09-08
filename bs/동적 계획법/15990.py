import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

dp = [[0 for _ in range(3)] for _ in range(100001)]

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # i보다 1 작은 수 중에 2와 3으로 끝나는 경우 그 다음수는 1로 마무리
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    # 2로 끝나는경우
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    # 3 으로 끝나는 경우
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

T = int(input())
for i in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
