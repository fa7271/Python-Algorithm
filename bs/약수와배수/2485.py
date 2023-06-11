import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(100000)


def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a


N = int(sys.stdin.readline())

lst = [int(sys.stdin.readline().rstrip()) for i in range(N)]
res =[]
for i in range(1,N):
    res.append(lst[i]-lst[i-1])

sets = list(set(res))
x = sets[0]

for i in range(1,len(sets)):
    x = gcd(x,sets[i])

cnt = 0
for i in res:
    cnt += i // x-1
print(cnt)