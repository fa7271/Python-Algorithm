import math
import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(input())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))
    res = 0
    for x,y in list(combinations(arr[1:], 2)):
        res += math.gcd(x, y)
    print(res)
