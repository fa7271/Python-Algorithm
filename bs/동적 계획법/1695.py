import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(100000)
import sys
import sys

def solution(sequence):
    n = len(sequence)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if sequence[i] == sequence[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                print(i,j,dp[i+1][j],dp[i][j-1])
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

N = int(input())
sequence = list(map(int, input().split()))

print(N - solution(sequence))
