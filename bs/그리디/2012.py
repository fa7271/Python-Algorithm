import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

rank = sorted([int(sys.stdin.readline()) for i in range(n)])
answer = 0
for i in range(1, n + 1):
    answer += abs(i - rank[i - 1])
print(answer)
