import sys
from math import gcd

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())
arr = list(map(int,sys.stdin.readline().split(" ")))
x = int(input())

a = 0; b = 0
for num in arr:
    if gcd(num,x) == 1:
        a += num
        b += 1
print(a / b)



