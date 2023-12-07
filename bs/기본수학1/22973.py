import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


target = abs(int(input()))
if target == 0:
    print(0)
elif target % 2 ==0:
    print(-1)
else:
    count = 0
    while target > 0:
        target = target >> 1
        count += 1
    print(count)
