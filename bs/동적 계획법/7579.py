import bisect
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
memories = [0] + list(map(int, sys.stdin.readline().rstrip().split(" ")))
costs = [0] + list(map(int, sys.stdin.readline().rstrip().split(" ")))

Len = sum(costs)

dp = [0] * (Len+1)

for i in range(1, N):
    memory = memories[i]
    cost = costs[i]
    for j in range(Len, cost - 1, -1):
        dp[j] = max(dp[j - cost] + memory, dp[j])
print(bisect.bisect_left(dp,M))

