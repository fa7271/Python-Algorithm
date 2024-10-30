import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
k = int(input())

# [i개의색중][j개의 색 선택]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    # 아무것도 안 뽑음
    dp[i][0] = 1
    # 1장만 뽑으면 됨 => n길이만큼
    dp[i][1] = i
for i in range(2, n + 1):
    for j in range(2, k + 1):
        # i = n 이면 동그라미니까 좌 우 선택 못함
        if i == n:
            dp[i][j] = dp[i - 3][j - 1] + dp[i - 1][j]
        #  i번째 뽑으면 왼쪽꺼 못 뽑으니까
        #  i-2개 중에서 j-1 개
        #  ++++
        #  i-1개 중에서 j개
        else:
            dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j]
        dp[i][j] %= 1000000003
print(dp[n][k])
