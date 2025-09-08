import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

nA, nB = map(int, input().split())
M = int(input())
result = 0

# 간선 확인
if nA % 2 == 1 and nB % 2 == 1:
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().rstrip().split(" "))
        if (x - 1) % 2 == 0 and (y - 1) % 2 == 0 :
            result += 1
            break
result += nA // 2 + nB // 2
print(result)
