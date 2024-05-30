import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
a = list(map(int, sys.stdin.readline().split(" ")))

sets = set()
sets.add(a[0] + a[0])

count = 0

for x in range(1, n):
    for y in range(x):
        if a[x] - a[y] in sets:
            count += 1
            break

    for y in range(x+1):
        sets.add(a[x] + a[y])
print(count)
# a+b+c = d
# a+b = d-c