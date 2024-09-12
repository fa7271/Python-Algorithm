import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
# 차이
temp = sorted([lst[i] - lst[i - 1] for i in range(1, n)], reverse=True)
print(sum(temp[k-1::]))
