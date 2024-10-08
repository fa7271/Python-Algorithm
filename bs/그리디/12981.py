import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

balls = list(map(int, sys.stdin.readline().rstrip().split()))

res = 0
lst = []
for ball in balls:
    a = ball // 3
    b = ball % 3
    res += a
    if b:
        lst.append(ball % 3)

if len(lst) == 1:
    res += 1
elif len(lst) > 1:
    res += max(lst)
print(res)
