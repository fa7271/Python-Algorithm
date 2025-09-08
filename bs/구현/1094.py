import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

x = int(input())
x = list(map(int, bin(x)[2::]))

print(x.count(1))