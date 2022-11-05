import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


res = sorted([int(input()) for _ in range(5)])
print(sum(res)// len(res), res[2])
