import sys

sys.stdin = open('/Python/h.txt', 'r')

d, k = map(int, sys.stdin.readline().rstrip().split(" "))
dp = [1, 1] + [0 for _ in range(d - 2)]

while True:
    for i in range(2, d):
        dp[i] = dp[i - 1] + dp[i - 2]
    if dp[d - 1] == k:
        print(dp[0], dp[1], sep="\n")
        exit()
    if dp[-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    else:
        dp[1] += 1
