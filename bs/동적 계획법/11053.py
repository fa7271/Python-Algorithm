import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
lst = [int(i) for i in sys.stdin.readline().split(" ")]

dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(max(dp))
