import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
list = sorted([input() for _ in range(n)],
              key=lambda x: (len(x), sum(int(c) for c in x if c.isdigit()), x))
print(*list, sep="\n")

# X
# 1BC
# 2AB
# A11
# B11
# 2000000
