import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())
res = sum([[1,2] for i in range(N//2)],[])
if N%2 : res+=[3]
print(*res)

