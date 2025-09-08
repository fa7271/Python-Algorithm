import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,input().split(" "))
nums = list(map(int,input().split(" ")))

now = 0
for i in range(K):
    now += nums[i]
maxn = now

for i in range(K,N):
    now += nums[i]
    now -= nums[i-K]
    maxn = max(maxn,now)

print(maxn)
