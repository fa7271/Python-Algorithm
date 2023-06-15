import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N =int(sys.stdin.readline())
time= list(map(int,sys.stdin.readline().rstrip().split(" ")))
time.sort()

dp = [0]*(N)
dp[0] = time[0]
for i in range(1,N):
    dp[i] =dp[i-1] + time[i]

print(sum(dp))

res = 0
for i in range(1,N+1):
    res += sum(time[0:i])
print(res)