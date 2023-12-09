import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(2000)

n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def dfs(left, right, depth):
    if left > right:
        return 0
    elif dp[left][right]:
        return dp[left][right]
    else:
        dp[left][right] = max(
            (dfs(left + 1, right, depth + 1) + lst[left] * depth),
            (dfs(left, right - 1, depth + 1) + lst[right] * depth)
        )
    return dp[left][right]

print(dfs(0, n - 1, 1))
