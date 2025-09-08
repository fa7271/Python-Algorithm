import sys
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

lst = []
for i in range(9):
    lst.append(int(input()))
res = []
for i in list(combinations(lst, 7)):
    if sum(i) == 100:
        print(*sorted(i), sep="\n")
        break

