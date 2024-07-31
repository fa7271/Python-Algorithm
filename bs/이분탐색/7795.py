import bisect
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    a = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    b = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    res = 0

    for num in a:
        res += bisect.bisect_left(b, num)
    print(res)