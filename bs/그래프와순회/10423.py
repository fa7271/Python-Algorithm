import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, k = map(int, sys.stdin.readline().rstrip().split(" "))
parents = [i for i in range(n + 1)]
powerStation = list(map(int, sys.stdin.readline().rstrip().split(" ")))

for i in powerStation:
    parents[i] = 0


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


arr = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

res = 0
for i in range(len(arr)):
    u, v, e = arr[i]
    if find(u) != find(v):
        union(u, v)
        res += e
print(res)
