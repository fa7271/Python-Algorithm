import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split())
S = list(map(int,sys.stdin.readline().split()))

D = list(map(int,sys.stdin.readline().split()))

for i in range(m):
    res = [0] * n
    for j in range(n):
        # res 는 이전 수열, S = 이후 수열
        res[D[j]-1] = S[j]
    S = res
print(*res)
