import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, l = map(int, sys.stdin.readline().split(" "))
H = sorted(list(map(int, sys.stdin.readline().split(" "))))
for i in range(n):
    if H[i] <= l:
        l += 1
    else:
        break
print(l)
