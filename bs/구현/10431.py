import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# https://www.acmicpc.net/problem/8979

n, k = map(int, input().split())

lst = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    if lst[i][0] == k:
        idx = i
for j in range(n):
    if lst[idx][1:] == lst[j][1:] :
        print(j+1)
        break
