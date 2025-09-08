import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())
left = list(map(int,sys.stdin.readline().rstrip().split(" ")))
right =  list(map(int,sys.stdin.readline().rstrip().split(" ")))

left.sort()
right.sort(reverse=True)

res = 0

for i in range(N):
    res += left[i]*right[i]
print(res)