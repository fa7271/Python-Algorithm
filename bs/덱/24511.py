import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque

n = int(input())
A = list(map(int,sys.stdin.readline().split(" ")))
B = list(map(int,sys.stdin.readline().split(" ")))
M = int(input())
C = list(map(int,sys.stdin.readline().split(" ")))

res = deque()
for qs in range(n):
    if A[qs] == 0:
        res.appendleft(B[qs])

for i in range(M):
    res.append(C[i])
    print(res.popleft(), end=' ')