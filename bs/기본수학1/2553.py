import math
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n = int(input())

print([i for i in(list(str(math.factorial(n)))) if i !="0"][-1])
