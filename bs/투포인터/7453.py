import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

dicAB = defaultdict(int)
for a in A:
    for b in B:
        ab = a + b
        dicAB[ab] += 1
res = 0
for c in C:
    for d in D:
        cd = (c + d) * (-1)
        if cd in dicAB:
            res += dicAB[cd]
print(res)
