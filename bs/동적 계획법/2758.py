import math
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# lotto = [i for i in range(1, m + 1)]

# idx = round(math.sqrt(m))

#dp[x][y] = x개의 로또, y까지의 범위의 숫자.
#: dp[i개로또][j까지의 숫자] = dp[i개로또][j-1 숫자] + dp[i-1개로또][j//2]
# 즉 j-1 까지 선택하는 경우 (j를 사용하지 않음)
# *2해서 접근할 수 있는 갯수 (j 사용)
dp = [[0] * 2001 for _ in range(11)]

# 로또 0 개 선택하는 경우
dp[0] = [1] * 2001
# 로또 1개 선택하는 경우
dp[1] = [i for i in range(2001)]

# 로또 2개 이상
for i in range(2, 11):
    # 목표숫자
    for j in range(1, 2001):
        # j 숫자를 선택안하고 i개 만들기 + j를 사용하고 i개 만들기
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j // 2]
t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split(" "))
    print(dp[n][m])
