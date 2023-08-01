import sys
from math import gcd

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A,B = map(int,sys.stdin.readline().split(" "))
C,D = map(int,sys.stdin.readline().split(" "))

E, F = B*D,(A*D)+(C*B)
x = gcd(E,F)

print(F // x, E // x)