import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

target = int(input())
m = int(input())
if m != 0:
    button = list(map(int, sys.stdin.readline().rstrip().split()))
else:
    button = []
res = abs(100 - target)
for i in range(1000001):
    num = str(i)
    for temp_i in num:
        if int(temp_i) in button:
            break
    else:
        res = min(res, len(str(i)) + abs(i - target))
print(res)
