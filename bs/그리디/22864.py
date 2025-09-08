import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

A, B, C, M = map(int,sys.stdin.readline().split(" "))

count = 0
res = 0
tired =0
while count < 24:
    if tired + A <= M:
        res += B
        tired += A
    else:
        tired -= C
        if tired <= 0:
            tired = 0
    count += 1
print(res)





