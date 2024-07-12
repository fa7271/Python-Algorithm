import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
a = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
x = int(input())
left = 0
right = n-1
count = 0
while left < right:
    if a[left] + a[right] < x:
        left += 1
    elif a[left] + a[right] > x:
        right -= 1
    else:
        count += 1
        left += 1
print(count)