import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,sys.stdin.readline().split())
lst = sorted([int(sys.stdin.readline()) for i in range(N)])
start = 1; end = lst[-1]
res = 0
while start<=end:
    mid = (start+end)//2
    count = sum(i//mid for i in lst)

    if count >= K:
        res = mid
        start = mid+1

    else:
        end = mid-1

print(res)
