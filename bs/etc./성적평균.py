n, m = map(int, sys.stdin.readline().split(" "))
dp = [0] + list(map(int, sys.stdin.readline().split(" ")))
for i in range(1, n+1): #
    dp[i] += dp[i-1]
for _ in range(m):
    left, right = map(int, input().split(" "))
    result = (dp[right] - dp[left-1]) / (right - left + 1)
    print(f'{result:.2f}')
