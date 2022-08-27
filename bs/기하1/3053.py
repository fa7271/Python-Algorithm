import sys
sys.stdin = open('/Python/h.txt', 'r')
import math
# input = sys.stdin.readline
# input = int(sys.stdin.readline())


R = int(sys.stdin.readline())

print("{0:.6f}".format(math.pi*(R**2)))
print("{0:.6f}".format((R**2)*2))
