import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, s = map(int, sys.stdin.readline().split(" "))
lst = list(map(int, sys.stdin.readline().split(" ")))

left = 0
right = 0
sum = lst[0]
length = 1e9

while left <= right:
    if sum < s:
        right += 1
        if right < n:
            sum += lst[right]
        else:
            break
    else:
        length = min(length, right-left+1)
        sum -= lst[left]
        left += 1

if length == 1e9:
    print(0)
else:
    print(length)