import math
import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


T = int(input())

for _ in range(T):
    arr =list(map(int,sys.stdin.readline().split(" ")))
    n = arr[0] ; del arr[0]
    res = 0
    for i in list(combinations(arr,2)):
        x, y = i[0],i[1]
        res += math.gcd(x,y)
    print(res)




