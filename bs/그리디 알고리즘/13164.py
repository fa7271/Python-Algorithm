import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
be = [lst[i] - lst[i-1] for i in range(1,len(lst))]
be.sort()
print(be,n-k)
print(sum(be[:n-k]))

# 1(2)3(2)5(1)6(4)10
# 13 56 10
# 1224
