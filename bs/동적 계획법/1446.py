import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, dis = map(int, sys.stdin.readline().split(" "))
dp = [i for i in range(dis+1)]

lst = sorted([list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)], key = lambda x:x[0])

for i in range(dis + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for start, end, d in lst:
        if i == start and end <= dis and dp[i] + d < dp[end]:
            dp[end] = dp[i] + d
print(dp[dis])

# for i in lst:
#     start, end, e = i
#     dp[end] = min(dp[end], dp[start] + e)
# for i in range(1, 10001):
#     dp[i] = min(dp[i], dp[i-1] + 1)