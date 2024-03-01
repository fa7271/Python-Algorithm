import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, p, q = map(int,sys.stdin.readline().split(" "))
dp = defaultdict(int)
dp[0] = 1

def dfs(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = dfs(n // p) + dfs(n // q)
    return dp[n]
print(dfs(n))
