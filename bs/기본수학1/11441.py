import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
lst = list(map(int,sys.stdin.readline().rstrip().split(" ")))
m = int(input())
arr = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]

dp = [0] * (n+1)
for i in range(1,n+1):
    dp[i] = dp[i-1] + lst[i-1]
for left, right in arr:
    if left == right:
        print(lst[left - 1])
    else:
        print(dp[right] - dp[left - 1])
