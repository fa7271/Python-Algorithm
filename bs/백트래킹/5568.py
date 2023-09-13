import sys
from itertools import permutations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
k = int(input())
lst = [str(sys.stdin.readline().rstrip()) for i in range(n)]
sets =set()
for per in list(permutations(lst,k)):
    sets.add("".join(per))
print(len(sets))

