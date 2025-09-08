import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().rsplit(" ")))
dp = [2] * N
for i in range(N-2):
    if (lst[i] <= lst[i + 1] <= lst[i + 2]) or (lst[i] >= lst[i + 1] >= lst[i + 2]):
        continue
    dp[i] = dp[i-1] + 1

print(max(dp))

