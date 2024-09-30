import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n = int(input())
if n % 6 == 2:
    for i in range(2, n + 1, 2):
        print(i)
    print(3)
    print(1)
    for i in range(7, n + 1, 2):
        print(i)
    print(5)
elif n % 6 == 3:
    for i in range(4, n + 1, 2):
        print(i)
    print(2)
    for i in range(5, n + 1, 2):
        print(i)
    print(1)
    print(3)
else:
    for i in range(2, n + 1, 2):
        print(i)
    for i in range(1, n + 1, 2):
        print(i)
# https://en.wikipedia.org/wiki/Eight_queens_puzzle