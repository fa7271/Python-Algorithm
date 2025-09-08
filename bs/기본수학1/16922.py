import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from itertools import combinations_with_replacement

n = int(input())
number_set = set()
number = {"i":1,
          "v":5,
          "x":10,
          "l":50}
numbers = ["i","v","x","l"]
lst = list(combinations_with_replacement(numbers,n))
for i in lst:
    num = 0
    for x in "".join(i):
        num += number[x]
    number_set.add(num)
print(len(number_set))