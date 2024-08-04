import sys
from math import gcd

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

print("1"*gcd(a,b))
