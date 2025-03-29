import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())


def solution():
    left, right, start = map(int, sys.stdin.readline().rstrip().split(" "))
    x = abs(start - left)
    y = abs(start - right)
    near = min(x,y)
    res = 0
    if x < y:
        res += 1
    res += near*2
    return res

for _ in range(t):
    print(solution())
