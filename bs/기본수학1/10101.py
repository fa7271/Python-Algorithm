import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

import sys

angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    if angle[0] == angle[1] == angle[2]:
        print('Equilateral')
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print("Error")