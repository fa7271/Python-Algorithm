import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, l, r, x = map(int, sys.stdin.readline().split(" "))

lst = list(map(int, sys.stdin.readline().split(" ")))
count = 0
for i in range(2, n + 1):
    for com in list(combinations(lst, i)):
        if l <= sum(com) <= r and max(com) - min(com) >= x:
            count += 1

print(count)
