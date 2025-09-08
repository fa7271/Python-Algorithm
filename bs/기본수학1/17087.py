import math
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,sys.stdin.readline().split(" "))
lst = list(map(int,sys.stdin.readline().split(" ")))
dis = []
for i in lst:
    dis.append(abs(m-i))

res = dis[0]
for i in dis[1:n]:
    res = math.gcd(i, res)
print(res)