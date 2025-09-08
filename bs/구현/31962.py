import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, x = map(int, sys.stdin.readline().rstrip().split(" "))
times = sorted([list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)],
               key=lambda x: (-x[0], x[1]))
res = -1
for s, t in times:
    if s + t <= x:
        print(s)
        break
else:
    print(-1)
