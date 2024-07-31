import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
lst = [int(i) for i in sys.stdin.readline().split(" ")]

dp = [1] * N
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
num = max(dp)
res = []
for i in range(len(dp)-1,-1,-1):
    if dp[i] == num:
        res.append(lst[i])
        num -=1
res.reverse()

print(max(dp))
print(*res)

