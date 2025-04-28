import math
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

h, w, n, m = map(int, input().split())
a = math.ceil(h / (n + 1))
b = math.ceil(w / (m + 1))
print(a * b)
