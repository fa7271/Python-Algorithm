import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
tips =sorted([int(input()) for x in range(n)], reverse=True)
res = [x for x in enumerate(tips)]
print(sum([(y-x) for x,y in res if y - x > 0]))
