import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A, B, N, M = map(int, sys.stdin.readline().split(" "))

dp = [-1] * 100001
dp[N] = 0
Q = deque()
Q.append(N)

while Q:
    node = Q.popleft()
    for nx in ([node + 1, node - 1, node + A, node - A, node + B, node - B, node * A, node * B]):
        if 0 <= nx <= 100000 and dp[nx] == -1:
            Q.append(nx)
            dp[nx] = dp[node]+1
            if nx == M:
                break
print(dp[M])
