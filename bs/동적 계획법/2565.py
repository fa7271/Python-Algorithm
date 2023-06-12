import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
dp = [1] *N

lst = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(N)]
lst.sort(key=lambda x:x[0])
print(lst)
for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N- max(dp))