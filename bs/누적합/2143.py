import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

Asum = [[0] * (n + 1) for _ in range(n + 1)]
BSum = [[0] * (m + 1) for _ in range(m + 1)]

Adict = defaultdict(int)
Bdict = defaultdict(int)


for i in range(1, n + 1):
    for j in range(i, n + 1):
        temp = Asum[i][j - 1] + A[j - 1]
        Asum[i][j] = temp
        Adict[temp] += 1

for i in range(1, m + 1):
    for j in range(i, m + 1):
        temp = BSum[i][j - 1] + B[j - 1]
        BSum[i][j] = temp
        Bdict[temp] += 1

res = 0

for num, count in Adict.items():
    if t - num in Bdict:
        res += count * Bdict[t - num]
print(res)